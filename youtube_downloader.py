"""
module: youtube_downloader.py
version: 0.61
"""
import os
import requests
from urllib.parse import urlparse
from pytube import YouTube, Playlist

class YouTubeDownloader:
    """
    Module: YouTubeDownloader
    Purpose: Provides methods for downloading YouTube videos and handling media files.
    Version: 0.61
    """

    @staticmethod
    def download_youtube_video(url, resolution='highest'):
        """
        Downloads a YouTube video at the specified resolution.

        Args:
            url (str): The URL of the YouTube video.
            resolution (str): The desired resolution of the video. Default is 'highest'.

        Returns:
            None
        """
        try:
            yt = YouTube(url)
            if resolution == 'highest':
                stream = yt.streams.get_highest_resolution()
            else:
                stream = yt.streams.filter(res=resolution).first()

            if stream:
                stream.download()
                print(f"YouTube video downloaded successfully from {url}")
            else:
                print(f"No video stream found for the specified resolution: {resolution}")
        except Exception as e:
            print(f"Error occurred while downloading YouTube video: {str(e)}")

    @staticmethod
    def download_playlist(playlist_url, download_location='./'):
        """
        Downloads all videos from a YouTube playlist.

        Args:
            playlist_url (str): The URL of the YouTube playlist.
            download_location (str): The directory where the downloaded files will be saved. Default is './'.

        Returns:
            None
        """
        try:
            playlist = Playlist(playlist_url)
            for video_url in playlist.video_urls:
                YouTubeDownloader.download_youtube_video(video_url, download_location)
            print(f"YouTube playlist downloaded successfully from {playlist_url}")
        except Exception as e:
            print(f"Error occurred while downloading YouTube playlist: {str(e)}")

    @staticmethod
    def download_media_file(url, file_type, download_location='./'):
        """
        Downloads a media file from the given URL.

        Args:
            url (str): The URL of the media file.
            file_type (str): The type of the media file to download.
            download_location (str): The directory where the downloaded file will be saved. Default is './'.

        Returns:
            None
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes

            file_extension = YouTubeDownloader.get_file_extension(url)
            file_name = f"downloaded_file_{file_type}.{file_extension}"
            file_path = os.path.join(download_location, file_name)

            YouTubeDownloader.save_file(file_path, response.content)
            print(f"Media file downloaded successfully from {url}")
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while downloading media file: {str(e)}")
        except Exception as e:
            print(f"An unexpected error occurred while downloading media file: {str(e)}")

    @staticmethod
    def get_file_extension(url):
        """
        Determines the file extension based on the URL.

        Args:
            url (str): The URL of the media file.

        Returns:
            str: The file extension.
        """
        parsed_url = urlparse(url)
        path = parsed_url.path
        extension = os.path.splitext(path)[1].lstrip('.')
        return extension if extension else 'unknown'

    @staticmethod
    def save_file(file_path, content):
        """
        Saves the downloaded file to the specified file path.

        Args:
            file_path (str): The path where the file will be saved.
            content (bytes): The content of the file to be saved.

        Returns:
            None
        """
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'wb') as file:
                file.write(content)
        except IOError as e:
            print(f"Error occurred while saving file: {str(e)}")