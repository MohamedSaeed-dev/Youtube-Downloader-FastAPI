import os
import zipfile
import yt_dlp
from app.models.videoModel import VideoDownloadOptions, PlaylistDownloadOptions

from app.utils.file_utils import DOWNLOAD_PATH, ensure_download_directory, get_format_string

def download_video(options: VideoDownloadOptions, isAudio: bool) -> str:
    """Download a single video and return the file path."""
    ensure_download_directory()  # Ensure the download directory exists
    format_str = get_format_string(options.resolution.value, isAudio)
    
    ydl_opts = {
        'format': format_str,
        'outtmpl': f"{DOWNLOAD_PATH}%(title)s.%(ext)s",
        'merge_output_format': 'mp4',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(options.url, download=True)
        file_path = ydl.prepare_filename(info)

    return file_path

def download_playlist(options: PlaylistDownloadOptions, isAudio: bool) -> str:
    """Download all videos in a playlist and return the path to the zip file."""
    ensure_download_directory()  # Ensure the download directory exists
    format_str = get_format_string(options.resolution.value, isAudio)
    
    ydl_opts = {
        'format': format_str,
        'outtmpl': f"{DOWNLOAD_PATH}%(playlist)s/%(title)s.%(ext)s",
        'merge_output_format': 'mp4',
        'noplaylist': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(options.url, download=True)

    # Create a zip file of all downloaded videos
    zip_file_path = f"{DOWNLOAD_PATH}playlist_download.zip"
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for root, _, files in os.walk(DOWNLOAD_PATH):
            for file in files:
                # Add files to the zip file
                zipf.write(os.path.join(root, file), file)

    return zip_file_path
