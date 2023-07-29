title ydl-cli - dependencies installer
echo [ydl-cli] Installing and/or updating dependencies...
echo [ydl-cli] Please wait the download finishes.
echo.
Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle
echo [ydl-cli] Please confirm the installation of "winget" for the installation of a subdependency (ffmpeg).
echo [ydl-cli] If you already have "winget" installed, just close the update window.
echo.
echo [ydl-cli] Anyway, just press Enter to continue. :)
pause >nul
cls
echo [ydl-cli] Installing "ffmpeg"
echo.
winget install ffmpeg
cls
echo [ydl-cli] Installing Python code dependencies...
echo.
pip install -r DEPENDENCIES
cls
RUN_SCRIPT
