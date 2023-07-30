import os
import subprocess

from functools import partial, wraps
from yt_dlp import YouTubeDL

@aiowrap
def extract_info(instance: YoutubeDL, url: str, download=True):
    return instance.extract_info(url, download)

def download_youtube_video(video_url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': '%(title)s.%(ext)s',
    }

    with YoutubeDL(ydl_opts) as ydl:
        info_dict = await extract_info(video_url, download=True)
        video_filename = ydl.prepare_filename(info_dict)

    return video_filename

def combine_audio_video(video_filename):
    output_filename = os.path.splitext(video_filename)[0] + "_ydl_cli.mp4"
    ffmpeg_cmd = ['ffmpeg', '-i', video_filename, '-i', video_filename.replace('.mp4', '.m4a'), '-c', 'copy', output_filename]
    subprocess.run(ffmpeg_cmd)
    os.remove(video_filename)
    os.remove(video_filename.replace('.mp4', '.m4a'))

    print(f"File saved as: {output_filename}")

def main():
    print("[ydl-cli] Made by Lucas Gabriel (lucmsilva) - Only runs on Windows")
    print("[ydl-cli] See new updates at:")
    print("[ydl-cli] https://github.com/ydl-team/ydl-cli/")
    print()
    video_url = input("[ydl-cli] Enter the YouTube video URL or ID you want to download: ")
    video_filename = download_youtube_video(video_url)
    combine_audio_video(video_filename)

if __name__ == "__main__":
    main()
