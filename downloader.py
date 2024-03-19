import os
from pytube import YouTube

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        stream.download(save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    save_directory = input("Enter the directory to save the video (default is current directory): ") or "."
    download_video(video_url, save_directory)
