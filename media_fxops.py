"""
module: media_fxops.py 
 
"""

from urllib.parse import urlparse, parse_qs

def ytURLprocess(url):
    """
    Dynamically detects whether the URL is to a YouTube base site or a specific video.

    Args:
        url (str): The URL to be processed.

    Returns:
        bool: True if the URL is to a YouTube base site, False otherwise.
    """
    parsed_url = urlparse(url)
    if parsed_url.netloc in ['youtube.com', 'www.youtube.com']:
        path = parsed_url.path
        if path == '/' or path.startswith('/watch') or path.startswith('/playlist') or path.startswith('/channel'):
            return True
    return False

def ytURLChanPtrResetReset(video_url):
    """
    Locates the playlist ID the video belongs to and locates the primary YouTube Channel endpoint.

    Args:
        video_url (str): The URL of the video.

    Returns:
        tuple: A tuple containing the playlist ID (str) and primary YouTube Channel endpoint (str), or (None, None) if not found.
    """
    parsed_url = urlparse(video_url)
    query_params = parse_qs(parsed_url.query)
    
    playlist_id = query_params.get('list', [None])[0]
    
    if parsed_url.path.startswith('/channel/'):
        channel_id = parsed_url.path.split('/')[-1]
        channel_endpoint = f'https://www.youtube.com/channel/{channel_id}'
    else:
        channel_endpoint = None
    
    return playlist_id, channel_endpoint

def ytURLChannelQuery(channel_endpoint):
    """
    Queries a YouTube channel for the different playlists and videos per playlist.

    Args:
        channel_endpoint (str): The primary YouTube Channel endpoint.

    Returns:
        dict: A dictionary containing playlists and videos per playlist.
        None: If an error occurs or the channel endpoint is invalid.
    """
    if not channel_endpoint or 'youtube.com/channel/' not in channel_endpoint:
        return None
    
    # Logic to query a YouTube channel for playlists and videos using the YouTube API
    # Placeholder code for demonstration purposes
    channel_id = channel_endpoint.split('/')[-1]
    playlists = get_channel_playlists(channel_id)  # Placeholder function
    
    channel_data = {}
    for playlist in playlists:
        playlist_id = playlist['id']
        videos = get_playlist_videos(playlist_id)  # Placeholder function
        channel_data[playlist_id] = [video['id'] for video in videos]
    
    return channel_data

def ytURLChanDetect(url):
    """
    Detects if the URL is a link to a YouTube channel, playlist, or video.

    Args:
        url (str): The URL to be checked.

    Returns:
        str: The type of URL detected ('channel', 'playlist', 'video') or 'unknown' if not detected.
    """
    parsed_url = urlparse(url)
    path = parsed_url.path
    
    if parsed_url.netloc in ['youtube.com', 'www.youtube.com']:
        if path.startswith('/channel/'):
            return 'channel'
        elif path.startswith('/playlist'):
            return 'playlist'
        elif path.startswith('/watch'):
            return 'video'
    
    return 'unknown'