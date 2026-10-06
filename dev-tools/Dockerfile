FROM alpine

RUN apk add --update --no-cache alpine-sdk zip shadow git yq composer nodejs npm php85-pdo_mysql php85-intl php85-gd php85-zip \
  && npm install --location=global npm pnpm npm-check-updates npm-run-all cordova semantic-release semantic-release-replace-plugin @semantic-release/changelog @semantic-release/git @semantic-release/github @semantic-release/exec \
  && npm cache clean --force \
  && mkdir -p /app \
  && adduser -D -h /app dev \
  && rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

WORKDIR /app

COPY entrypoint.sh /entrypoint

ENTRYPOINT ["/entrypoint"]

CMD ["tail", "-f", "/dev/null"]
