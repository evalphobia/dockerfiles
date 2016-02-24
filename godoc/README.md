godoc 
====

docker-compose file for private godoc server.

# Usage

- 1. replace `assets/github_private_key` (github private key file) to clone your private repository
- 2. replace `assets/list.txt` for godoc
    - supported only public/private github repository
- 3. replace `environment` on `docker-compose.yml`
    - GODOC_OPTS: options for godoc (`godoc -http=:6060 -src $GODOC_OPTS`)
    - PRIVATE_KEY_PASS: github private key's pass phrase
- 4. build and up docker

example:

```bash
# 1.
    $ cp $HOME/.ssh/id_rsa assets/github_private_key
    $ chmod 400 assets/github_private_key

# 2.
    $ : > assets/list.txt
    $ echo "github.com/golang/go" >> assets/list.txt
    $ echo "github.com/golang/mobile" >> assets/list.txt

# 3.
    $ vi docker-compose.yml

# 4.
    $ docker-compose build
    $ docker-compose up
```
