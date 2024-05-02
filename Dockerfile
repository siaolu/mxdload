# Dockerfile
# Version 0.51

FROM python:3.9

WORKDIR /app

# Copy Python script modules
COPY yThRDL.py /app/yThRDL.py
COPY media_info.py /app/media_info.py
COPY main.py /app/main.py

# Install dependencies
RUN pip install pytube requests

CMD ["python", "main.py"]
