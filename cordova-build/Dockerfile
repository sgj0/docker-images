FROM alvrme/alpine-android:android-36.1-jdk21

ADD https://services.gradle.org/distributions/gradle-8.14.2-bin.zip /tmp/gradle-8.14.2-bin.zip

RUN apk add --update --no-cache rsync nodejs npm jq \
 && npm install --location=global pnpm cordova \
 && mkdir /opt/gradle \
 && unzip -d /opt/gradle /tmp/gradle-8.14.2-bin.zip \
 && rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

ENV ANDROID_SDK_ROOT=/opt/sdk
ENV JAVA_HOME=/usr/lib/jvm/jdk
ENV GRADLE_HOME=/opt/gradle/gradle-8.14.2
ENV PATH=${PATH}:${JAVA_HOME}/bin
ENV PATH=${PATH}:${GRADLE_HOME}/bin
