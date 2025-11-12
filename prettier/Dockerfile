FROM node:lts-alpine

COPY app /opt/prettier

WORKDIR /opt/prettier

RUN npm install @prettier/plugin-php @prettier/plugin-xml prettier prettier-plugin-java prettier-plugin-nginx prettier-plugin-sh prettier-plugin-sql prettier-plugin-toml \
  && npm cache clean --force \
  && rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

WORKDIR /work

ENTRYPOINT ["/opt/prettier/node_modules/.bin/prettier", "--config=/opt/prettier/.prettierrc.js", "--cache-location=/tmp/prettier"]

CMD ["--help"]
