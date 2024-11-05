import os
import shutil

DOWNLOAD_PATH = "./downloads/"

def ensure_download_directory():
    """Ensure the download directory exists."""
    if not os.path.exists(DOWNLOAD_PATH):
        os.makedirs(DOWNLOAD_PATH)

def clear_download_directory():
    """Clear the download directory."""
    if os.path.exists(DOWNLOAD_PATH):
        shutil.rmtree(DOWNLOAD_PATH)
    ensure_download_directory()

def get_format_string(resolution: str, isAudio: bool) -> str:
    """Constructs the yt-dlp format string based on resolution and options."""
    if resolution == "best":
        if isAudio:
            return "bestaudio"
        else:
            return "bestvideo+bestaudio/best"

    # Map resolution string to yt-dlp format string
    if isAudio:
        return "bestaudio"
    else:
        return f"bestvideo[height={resolution[:-1]}]+bestaudio/best"