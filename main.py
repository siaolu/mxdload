from media_info import get_media_info
from yThRDL import yThRDL

def mainrun():
    """
    Main function to drive the primary execution of the script.
    """
    # Example usage:
    url = input("Enter the URL: ")
    media_info = get_media_info(url)
    print("Available media files:")
    for media in media_info:
        print(media)
        file_type = media['type']
        file_url = media['url']
        if file_type == 'video' and yThRDL.is_youtube_url(file_url):
            yThRDL.download_youtube_video(file_url)
        elif file_type in ['audio', 'image']:
            yThRDL.download_media_file(file_url, file_type)

if __name__ == "__main__":
    mainrun()

