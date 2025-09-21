FROM alpine

RUN apk add --update --no-cache icecast \
  && rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

CMD ["icecast", "-c", "/etc/icecast.xml"]

EXPOSE 8000
