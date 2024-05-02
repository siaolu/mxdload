# mxdload
# YouTube Media Downloader

This script allows you to download media files (videos, audio, images) from YouTube and other URLs. It provides a modular and maintainable Python solution with a Dockerized environment for easy deployment.

## Features

- Download YouTube videos in various resolutions.
- Download entire YouTube playlists.
- Download media files (audio, video, images) from any URL.
- Modular design for easy maintenance and extensibility.
- Dockerized environment for seamless deployment.

## Usage

### Prerequisites

- Docker installed on your system.
- Internet connection for downloading media files.

### Setup

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your_username/youtube-media-downloader.git
    ```

2. Navigate to the project directory:

    ```bash
    cd youtube-media-downloader
    ```

### Running the Script

1. Build the Docker image:

    ```bash
    docker build -t youtube-media-downloader .
    ```

2. Run the Docker container:

    ```bash
    docker run -it --rm youtube-media-downloader
    ```

3. Follow the on-screen prompts to enter the URL of the media file you want to download.

4. The script will download the media file to the `downloads` directory within the container.

### Advanced Options

- You can customize the download location by modifying the `main.py` script or passing arguments to the `yThRDL.download_media_file` method.

- Modify the `buildrun.sh` script to add additional functionality or customize Docker container options.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
