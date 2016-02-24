FROM golang:1.6.0
MAINTAINER evalphobia

#============
# tools
#============
RUN apt-get update && apt-get install -y --no-install-recommends \
        expect \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#============
# copy private key
#============
COPY assets/github_private_key /root/.ssh/id_rsa

RUN git config --global url.'git@github.com:'.insteadOf 'https://github.com/' \
  && echo 'Host github.com\n\
    StrictHostKeyChecking no' >>   ~/.ssh/config \
  && cat ~/.ssh/config \
  && chmod 400 ~/.ssh/*

#============
# run app
#============
COPY assets/list.txt /root/list.txt

CMD eval `ssh-agent` \
  && expect -c "\
      set timeout 5; \
      spawn ssh-add; \
      expect \"Enter passphrase for\"; send \"$PRIVATE_KEY_PASS\r\"; \
      expect eof; \
      " \
  && for REPO in `cat /root/list.txt`; do\
       if [ ! -d "/go/src/$REPO" ]; then\
         rp=`echo $REPO | sed -e 's@/@:@'`;\
         git clone git@${rp}.git /go/src/$REPO;\
       fi\
     done\
  && godoc -http=:6060 -src $GODOC_OPTS
