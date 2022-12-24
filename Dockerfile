ARG PYTHON_VERSION="3-alpine"

FROM python:${PYTHON_VERSION} AS builder
COPY . /tmp/lesma
RUN apk -U --no-progress add file g++ gcc make && \
  cd /tmp/lesma && \
  python setup.py install

FROM python:${PYTHON_VERSION}
ARG HOST="0.0.0.0"
ARG PORT="7777"
ARG USER="lesma"
ARG STORE="/var/cache/lesma"
COPY --from=builder /usr/local /usr/local
RUN adduser -S -D -h ${STORE} -s /sbin/nologin -G users \
  -g ${USER} ${USER}
ENV \
  LESMA_HOST="${HOST}" \
  LESMA_PORT="${PORT}" \
  LESMA_STORE="${STORE}"
EXPOSE "${PORT}"
VOLUME [ "${STORE}" ]
USER ${USER}
ENTRYPOINT [ "/usr/local/bin/lesma", "wsgi" ]
