from yt_dlp import YoutubeDL

def extract_info(instance: YoutubeDL, url: str, download=True):
    return instance.extract_info(url, download)

def download_youtube_video(video_url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = extract_info(ydl, video_url, download=True)
        video_filename = ydl.prepare_filename(info_dict)
    
    return video_filename

def main():
    print("[ydl-cli] Made by Lucas Gabriel (lucmsilva)")
    print("[ydl-cli] See new updates at: https://github.com/lucmsilva651/ydl-cli/")
    print()
    print("[ydl-cli] Supported platforms on README.md file")
    video_url = input("[ydl-cli] Enter the video URL or ID you want to download: ")
    print()
    video_filename = download_youtube_video(video_url)

main()
