import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from models.videoModel import VideoDownloadOptions, PlaylistDownloadOptions
from services.downloadService import download_video, download_playlist

router = APIRouter()

@router.post("/download/video")
async def download_single_video(options: VideoDownloadOptions, isAudio: bool = False):
    file_path = download_video(options, isAudio)
    
    if not file_path or not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(path=file_path, media_type='video/mp4', filename=os.path.basename(file_path))

@router.post("/download/playlist")
async def download_playlist_endpoint(options: PlaylistDownloadOptions, isAudio: bool = False):
    zip_file_path = download_playlist(options, isAudio)

    if not zip_file_path or not os.path.exists(zip_file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(path=zip_file_path, media_type='application/zip', filename='playlist_download.zip')
