FROM python:3.10.4-alpine as BUILDER

WORKDIR /build

RUN pip install --upgrade pip
RUN pip install --upgrade wheel

COPY requirements ./requirements
RUN pip wheel --wheel-dir /build/wheels -r requirements/dev.txt

###################################
# Build the docker image
###################################

FROM python:3.10.4-alpine as RUNNER

WORKDIR /app

COPY --from=BUILDER /build/wheels /wheels
COPY --from=BUILDER /build/requirements .

RUN pip install --no-index /wheels/*

COPY ./start /start
RUN chmod +x /start

COPY . .