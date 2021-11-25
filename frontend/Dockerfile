FROM node:14.5.0

ENV UI_PATH /frontend

WORKDIR $UI_PATH

COPY package*.json ./
RUN npm install

COPY . .

CMD ["npm", "run", "start"]