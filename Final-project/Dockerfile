FROM alpine:latest

WORKDIR /app

COPY ../python/requests/requirements.txt requirements.txt
COPY ./view.py view.py
COPY ./templates/ templates/

RUN python3 -m venv venv
ENV PATH="/app/venv/bin:$PATH"

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["view.py"]