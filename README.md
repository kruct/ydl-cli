# ydl-cli
A modular script to download videos from multiple sites via CLI

## Recommended pre-requisites
 - The most recent version of Python
 - A Windows 10 environment
 
## Installation
On this repository page, click the "Code" button and then click "Download ZIP". When the download finishes, extract the downloaded ZIP to any folder and run the "RUN.cmd" file inside that folder. Is it easy?

## Downloading a video by ID or URL
In the script window, just put the link of the video you want to download (see below the supported sites), and press Enter to start the download.

## Supported sites
- YouTube (tested)
- YouTube Music (tested)
- SoundCloud (tested)
- Spotify (only works if the content is not DRM-protected)
- Deezer (only the 30sec music preview)
- PornHub (tested, just ignore that, but it works ok)
> Making this compatibility list is quite complicated, but if I discover one more compatible site I will update this list as soon as possible.

## External sources
The script uses these sources and libraries:
```
chocolatey, yt_dlp, ffmpeg
```