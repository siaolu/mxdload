import os
import requests
from urllib.parse import urlparse
from pytube import YouTube, Playlist

class yThRDL:
    """
    Module: yThRDL
    Purpose: Provides methods for downloading YouTube videos and handling media files.
    Version: 0.50a
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
        yt = YouTube(url)
        if resolution == 'highest':
            stream = yt.streams.get_highest_resolution()
        else:
            stream = yt.streams.filter(res=resolution).first()
        stream.download()

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
        playlist = Playlist(playlist_url)
        for video in playlist.video_urls:
            yThRDL.download_youtube_video(video, download_location)

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
        response = requests.get(url)
        file_extension = yThRDL.get_file_extension(url)
        file_path = os.path.join(download_location, f"downloaded_file.{file_extension}")
        yThRDL.save_file(file_path, response.content)

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
        if '.' in path:
            extension = path.split('.')[-1]
        else:
            extension = 'binary'
        return extension

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
        with open(file_path, 'wb') as file:
            file.write(content)

    @staticmethod
    def is_youtube_url(url):
        """
        Checks if the given URL is a YouTube video URL.

        Args:
            url (str): The URL to check.

        Returns:
            bool: True if the URL is a YouTube video URL, False otherwise.
        """
        # Logic to check if the URL is a YouTube video URL
        # For demonstration purposes, let's assume simple string matching
        if 'youtube.com' in url:
            return True
        return False
