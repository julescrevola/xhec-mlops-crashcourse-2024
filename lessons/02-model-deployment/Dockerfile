FROM python:3.9.16-slim

WORKDIR /02-model-deployment

# Install the application dependencies
COPY requirements_app.txt ./
RUN pip install -r requirements_app.txt

# Copy in the source code
COPY . .
EXPOSE 8080

CMD ["uvicorn", "web_service.main:app", "--host", "0.0.0.0", "--port", "8080"]
