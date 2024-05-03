from media_fxops import ytURLprocess, ytURLChanPtrResetReset, ytURLChannelQuery, ytURLChanDetect
from media_xfops import download_media_menu
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

if __name__ == "__main__":
    main_menu()
