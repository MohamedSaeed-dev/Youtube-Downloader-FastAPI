from pydantic import BaseModel
from typing import Optional
from enum import Enum

class ResolutionChoices(str, Enum):
    """Enum class for resolution choices."""
    BEST = "best"
    P144 = "144p"
    P240 = "240p"
    P360 = "360p"
    P480 = "480p"
    P720 = "720p"
    P1080 = "1080p"
    P1440 = "1440p"
    P2160 = "2160p"  # 4K

class VideoDownloadOptions(BaseModel):
    url: str
    resolution: Optional[ResolutionChoices] = ResolutionChoices.BEST
    # video_only: Optional[bool] = False
    # audio_only: Optional[bool] = False

class PlaylistDownloadOptions(BaseModel):
    url: str
    resolution: Optional[ResolutionChoices] = ResolutionChoices.BEST
