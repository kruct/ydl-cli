import os
import subprocess
import asyncio

from yt_dlp import YoutubeDL
from functools import wraps, partial
from typing import Callable
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError

REPO_ = "https://github.com/ydl-team/ydl-cli/"
BRANCH_ = "main"

def updater():
    print("Checking for updates...")
    print()
    try:
        repo = Repo()
    except GitCommandError:
        return print("<i>Invalid Git Command</i>")
     except InvalidGitRepositoryError:
        repo = Repo.init()
        if "upstream" in repo.remotes:
            origin = repo.remote("upstream")
        else:
            origin = repo.create_remote("upstream", REPO_)
        origin.fetch()
        repo.create_head(BRANCH_, origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)
    if repo.active_branch.name != BRANCH_:
        return print("An error ocurred!")
    try:
        repo.create_remote("upstream", REPO_)
    except BaseException:
        pass
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(BRANCH_)
    try:
        ups_rem.pull(BRANCH_)
    except GitCommandError:
        repo.git.reset("--hard", "FETCH_HEAD")
    print("[ydl-cli] Updated Sucessfully!")
    

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
        info_dict = await extract_info(ydl, video_url, download=True)
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
    updater()
    asyncio.run(main())
