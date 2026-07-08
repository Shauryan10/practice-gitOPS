FROM nginx:alpine

COPY index.html /usr/share/nginx/.

EXPOSE 80
