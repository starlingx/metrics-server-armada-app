FROM node:14.15.5-alpine3.13

WORKDIR /usr/src/app

COPY src/package*.json ./

RUN npm install

COPY src/ .

CMD [ "node", "sample-application.js" ]