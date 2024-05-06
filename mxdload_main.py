"""
module: mxdload_main.py
version: 1.1
"""
from youtube_url_processor import ytURLprocess, ytURLChanPtrResetReset, ytURLChannelQuery, ytURLChanDetect
from media_downloader import download_media_menu
from youtube_downloader import YouTubeDownloader

def main_menu():
    """
    Displays the main menu options.
    """
    while True:
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

if __name__ == "__main__":
    main_menu()