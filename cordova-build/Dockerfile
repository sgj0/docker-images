FROM alvrme/alpine-android:android-37.1-jdk21

ARG GRADLE_VERSION=8.14.4

ADD https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip /tmp/gradle-${GRADLE_VERSION}-bin.zip

RUN apk add --update --no-cache rsync nodejs npm jq \
 && npm install --location=global pnpm cordova \
 && mkdir /opt/gradle \
 && unzip -d /opt/gradle /tmp/gradle-${GRADLE_VERSION}-bin.zip \
 && rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

ENV GRADLE_HOME=/opt/gradle/gradle-${GRADLE_VERSION}
ENV PATH=${PATH}:${JAVA_HOME}/bin
ENV PATH=${PATH}:${GRADLE_HOME}/bin
