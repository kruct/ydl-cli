import os
import subprocess
import youtube_dl

def download_youtube_video(video_url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': '%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=True)
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
    video_url = input("[ydl-cli] Enter the YouTube video URL or ID you want to download: ")
    video_filename = download_youtube_video(video_url)
    combine_audio_video(video_filename)

if __name__ == "__main__":
    main()
