FROM node:lts-alpine

RUN apk add --update --no-cache alpine-sdk zip shadow git \
  && npm install --location=global npm pnpm npm-check-updates npm-run-all cordova semantic-release semantic-release-xml-updater semantic-release-replace-plugin @semantic-release/changelog @semantic-release/git @semantic-release/github \
  && npm cache clean --force \
  && mkdir -p /app \
  && rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

WORKDIR /app

COPY entrypoint.sh /entrypoint

ENTRYPOINT ["/entrypoint"]

CMD ["tail", "-f", "/dev/null"]
