"""
module: media_info.py 
# 
"""


import requests
from bs4 import BeautifulSoup

def get_media_info(url):
    """
    Retrieves information about the available media files from the given URL.

    Args:
        url (str): The URL of the web page containing the media files.

    Returns:
        list: A list of dictionaries containing information about the media files.
        None: If an error occurs during the process.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        soup = BeautifulSoup(response.content, 'html.parser')

        media_info = []

        # Find all video elements
        video_elements = soup.find_all('video')
        for video in video_elements:
            video_url = video.get('src')
            if video_url:
                media_info.append({'title': video.get('title', 'Untitled Video'), 'url': video_url, 'type': 'video'})

        # Find all audio elements
        audio_elements = soup.find_all('audio')
        for audio in audio_elements:
            audio_url = audio.get('src')
            if audio_url:
                media_info.append({'title': audio.get('title', 'Untitled Audio'), 'url': audio_url, 'type': 'audio'})

        # Find all image elements
        img_elements = soup.find_all('img')
        for img in img_elements:
            img_url = img.get('src')
            if img_url:
                media_info.append({'title': img.get('alt', 'Untitled Image'), 'url': img_url, 'type': 'image'})

        return media_info

    except requests.exceptions.RequestException as e:
        print(f"Error occurred while retrieving media information: {e}")
        return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None