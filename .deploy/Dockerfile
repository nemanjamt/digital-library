FROM node:22.11

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY tsconfig.json ./
COPY src/ ./src/

RUN npx tsc

EXPOSE 3000

CMD ["node", "build/app.js"]
