"""

First Install the Library by running the following command in your terminal:

pip install yt-dlp


"""

import yt_dlp as yt

print("Welcome to the Youtube Video Downloader App!! \n")


def DownloadVideo(url):

    ydl_opts = {}

    with yt.YoutubeDL(ydl_opts) as yld:
        yld.download([url])
    print("Video Downloaded Successfully!!!")


while True:

    getPerm = input("Want to Download the Youtube Video(y/n):")
    print()

    if (getPerm.isdigit()):
        print("Invalid input!!")
    else:
        if (getPerm.lower() == "y" or getPerm.lower() == "yes"):
            try:
                getUrl = input("Enter the URL of the Youtube Video:")
                if (getUrl[0:8] != "https://"):
                    print("INVALID URL!!")
                else:
                    DownloadVideo(getUrl)
            except Exception as e:
                print(f"Invalid URL {e}")
        elif (getPerm.lower() == "n") or (getPerm.lower() == "no"):
            print("Program Closed Successfully!")
            break
        else:
            print("INVALID PERMIT!!")