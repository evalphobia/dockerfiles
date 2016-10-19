FROM node:6.9-slim

RUN npm install -g kinesalite

EXPOSE 4577

CMD kinesalite  --createStreamMs 10 --deleteStreamMs 10 --port 4577
