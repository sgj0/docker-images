FROM node:lts-alpine

RUN apk add --update --no-cache shadow git \
  && npm install --location=global npm pnpm npm-check-updates npm-run-all cordova \
  && npm cache clean --force \
  && mkdir -p /app \
  && rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

WORKDIR /app

COPY entrypoint.sh /entrypoint

ENTRYPOINT ["/entrypoint"]

CMD ["tail", "-f", "/dev/null"]
