# develop stage
FROM node:lts-alpine as develop-stage
WORKDIR /app
COPY package*.json ./
RUN npm install @vue/cli-service
RUN npm install 
COPY . .

# RUN cd node_modules && ls 

# build stage
FROM develop-stage as build-stage
RUN yarn build

# production stage (not used yet)
FROM node:lts-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
#CMD ["nginx", "-g", "daemon off;"]