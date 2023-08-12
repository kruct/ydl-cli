@echo off
cd updaterCore
echo [ydl-cli updater] Downloading: Latest ydl-cli release from "github.com"
updaterCore https://github.com/ydl-team/ydl-cli/archive/refs/heads/main.zip
exit