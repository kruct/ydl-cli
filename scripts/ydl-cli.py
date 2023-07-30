import os
import asyncio
import subprocess

from yt_dlp import YoutubeDL
from typing import Callable 
from functools import wraps, partial

def aiowrap(func: Callable) -> Callable:
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)

    return run

@aiowrap
def extract_info(instance: YoutubeDL, url: str, download=True):
    return instance.extract_info(url, download)

async def download_youtube_video(video_url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = await extract_info(video_url, download=True)
        video_filename = ydl.prepare_filename(info_dict)

    return video_filename

async def main():
    print("[ydl-cli] Made by Lucas Gabriel (lucmsilva)")
    print("[ydl-cli] See new updates at: https://github.com/ydl-team/ydl-cli/")
    print()
    video_url = input("[ydl-cli] Enter the YouTube video URL or ID you want to download: ")
    print()
    video_filename = await download_youtube_video(video_url)

if __name__ == "__main__":
    asyncio.run(main())
