FROM node:lts-alpine AS node
FROM alpine

COPY --from=node /usr/lib /usr/lib
COPY --from=node /usr/local/lib /usr/local/lib
COPY --from=node /usr/local/include /usr/local/include
COPY --from=node /usr/local/bin /usr/local/bin

ADD versionning.sh /opt/

RUN apk add --update --no-cache jq yq \
  && npm install --global npm semver \
  && npm cache clean --force \
  && mkdir /work \
  && chmod +x /opt/versionning.sh \
  && rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

WORKDIR /work

ENTRYPOINT ["/opt/versionning.sh"]
