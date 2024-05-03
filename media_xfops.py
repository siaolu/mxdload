"""
module: media_xfops.py 
 
"""


from yThRDL import yThRDL

def download_youtube_video():
    """
    Downloads a YouTube video.
    """
    while True:
        url = input("Enter the YouTube video URL: ")
        if yThRDL.is_valid_youtube_url(url):
            break
        else:
            print("Invalid YouTube video URL. Please try again.")

    while True:
        resolution = input("Enter the desired resolution (or 'highest' for highest resolution): ")
        if resolution == 'highest' or yThRDL.is_valid_resolution(resolution):
            break
        else:
            print("Invalid resolution. Please try again.")

    try:
        yThRDL.download_youtube_video(url, resolution)
        print("Video downloaded successfully.")
    except Exception as e:
        print(f"Error occurred while downloading video: {str(e)}")

def download_playlist():
    """
    Downloads a YouTube playlist.
    """
    while True:
        url = input("Enter the YouTube playlist URL: ")
        if yThRDL.is_valid_playlist_url(url):
            break
        else:
            print("Invalid YouTube playlist URL. Please try again.")

    try:
        yThRDL.download_playlist(url)
        print("Playlist downloaded successfully.")
    except Exception as e:
        print(f"Error occurred while downloading playlist: {str(e)}")

def download_media_file():
    """
    Downloads a media file from a URL.
    """
    url = input("Enter the URL of the media file: ")
    file_type = input("Enter the type of the media file (e.g., 'audio', 'video', 'image'): ")

    try:
        yThRDL.download_media_file(url, file_type)
        print("Media file downloaded successfully.")
    except Exception as e:
        print(f"Error occurred while downloading media file: {str(e)}")

def download_media_menu():
    """
    Displays the download media menu options.
    """
    while True:
        print("\nDownload Media Menu:")
        print("1. Download YouTube Video")
        print("2. Download Playlist")
        print("3. Download Media File from URL")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            download_youtube_video()
        elif choice == "2":
            download_playlist()
        elif choice == "3":
            download_media_file()
        elif choice == "4":
            main_menu()
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    """
    Displays the main menu options.
    """
    # Placeholder for main menu implementation
    pass