FROM python:3-alpine

COPY . /tmp/lesma

ARG HOST="0.0.0.0"
ARG PORT="7777"
ARG STORE="/var/cache/lesma"

RUN apk -U --no-progress add file g++ gcc make && \
  cd /tmp/lesma && \
  python setup.py install && \
  mkdir -p $STORE && \
  chown nobody:nobody $STORE && \
  apk --no-progress del file g++ gcc make && \
  rm -rf /root/.ash_history /tmp/lesma /var/cache/apk/*

ENV LESMA_HOST="$HOST" \
  LESMA_PORT="$PORT" \
  LESMA_STORE="$STORE"

EXPOSE "$PORT"

VOLUME [ "$STORE" ]

USER nobody

ENTRYPOINT [ "/usr/local/bin/lesma", "wsgi" ]
