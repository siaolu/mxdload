from media_info import get_media_info
from yThRDL import yThRDL

def main_menu():
    """
    Displays the main menu options.
    """
    print("\nMain Menu:")
    print("1. Download Media")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        download_media_menu()
    elif choice == "2":
        print("Exiting...")
        exit()
    else:
        print("Invalid choice.")
        main_menu()

def download_media_menu():
    """
    Displays the download media menu options.
    """
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
        print("Invalid choice.")
        download_media_menu()

def download_youtube_video():
    """
    Downloads a YouTube video.
    """
    url = input("Enter the YouTube video URL: ")
    resolution = input("Enter the desired resolution (or 'highest' for highest resolution): ")
    yThRDL.download_youtube_video(url, resolution)
    print("Video downloaded successfully.")
    download_media_menu()

def download_playlist():
    """
    Downloads a YouTube playlist.
    """
    url = input("Enter the YouTube playlist URL: ")
    yThRDL.download_playlist(url)
    print("Playlist downloaded successfully.")
    download_media_menu()

def download_media_file():
    """
    Downloads a media file from a URL.
    """
    url = input("Enter the URL of the media file: ")
    file_type = input("Enter the type of the media file (e.g., 'audio', 'video', 'image'): ")
    yThRDL.download_media_file(url, file_type)
    print("Media file downloaded successfully.")
    download_media_menu()

if __name__ == "__main__":
    main_menu()
