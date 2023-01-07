FROM nginx:1.21-alpine
COPY nginx.conf /etc/nginx/templates/default.conf.template
COPY src /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]