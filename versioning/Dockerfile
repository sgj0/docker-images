FROM alpine

ADD versioning.py /srv/
ADD pyproject.toml /srv/

RUN apk add --update --no-cache jq yq py3-pip \
  && cd /srv/ \
  && pip install --break-system-packages --editable . \
  && mkdir /work \
  && chmod +x /srv/versioning.py \
  && rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

WORKDIR /work

ENTRYPOINT ["/srv/versioning.py"]
