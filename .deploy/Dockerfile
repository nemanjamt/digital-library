FROM node:22.11

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .

RUN mkdir -p /app/reports && npx tsc

EXPOSE 3000

# CMD ["node", "build/app.js"]
CMD ["/bin/bash", "-c", "tail -f /dev/null"]
