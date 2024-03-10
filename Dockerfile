FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/app"

WORKDIR /app

RUN useradd -m -r -u 101 user

COPY requirements.txt /app/

RUN chown -R user:user /app && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY request_task.service /etc/systemd/system/fastapi_app.service
COPY request_task.timer /etc/systemd/system/fastapi_app.timer

COPY . .

CMD ["bash", "-c", "systemctl enable fastapi_app.service && systemctl enable fastapi_app.timer && systemctl start fastapi_app.service && systemctl start fastapi_app.timer && uvicorn app.main:app --reload"]