FROM node:14.9.0-alpine

WORKDIR /usr/src/app

COPY ./app/package*.json /usr/src/app/
RUN npm install
RUN npm install -g @angular/cli@9.1.12

COPY ./app/ /usr/src/app

EXPOSE 4000

RUN npm run build:ssr
CMD [ "npm", "run", "serve:ssr" ]