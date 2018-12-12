ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

#Install nodejs
RUN apk add --update --no-cache nodejs nodejs-npm python3 python3-dev python2 

# Copy data
COPY . /

# Install modules
RUN ["npm", "install", "--loglevel error"]

# Copy data
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
