# Dockerfile
# Version 0.52

FROM python:3.9
WORKDIR /app

# Copy Python script modules
COPY youtube_downloader.py /app/youtube_downloader.py
COPY webpage_media_extractor.py /app/webpage_media_extractor.py
COPY youtube_url_processor.py /app/youtube_url_processor.py
COPY media_downloader.py /app/media_downloader.py
COPY mxdload_main.py /app/mxdload_main.py

# Install dependencies
RUN pip install pytube requests beautifulsoup4

CMD ["python", "mxdload_main.py"]