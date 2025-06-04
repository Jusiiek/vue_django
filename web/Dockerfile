FROM node:22

RUN apt-get update && apt-get install make

WORKDIR /app
COPY package.json yarn.lock ./
RUN corepack enable && yarn install
COPY . .

CMD ["make", "dev_run"]
