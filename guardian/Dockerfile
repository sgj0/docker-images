FROM alpine

RUN apk add --update --no-cache rsync openssh \
  && mkdir /root/.ssh \
  && chmod 0700 /root/.ssh \
  && ssh-keygen -A \
  && sed -i s/^#PasswordAuthentication\ yes/PasswordAuthentication\ no/ /etc/ssh/sshd_config \
  && rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

EXPOSE 22

COPY entrypoint.sh /entrypoint

ENTRYPOINT ["/entrypoint"]
