@echo off
cls
echo [ydl-cli] Installing "ffmpeg" via "Chocolatey"
echo.
choco feature enable -n allowGlobalConfirmation
choco install ffmpeg-full
cls

startMain