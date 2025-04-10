import json
from urllib.parse import urlparse, parse_qs, urlencode
from urllib.request import urlopen
from typing import Optional, List, Dict, Any

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    raise ImportError(
        "`youtube_transcript_api` not installed. Please install it using `pip install youtube_transcript_api`"
    )


class YouTubeTools:
    def __init__(
        self,
        get_video_captions: bool = True,
        get_video_data: bool = True,
        get_video_timestamps: bool = True,
        languages: Optional[List[str]] = None,
        proxies: Optional[Dict[str, Any]] = None,
    ):
        self.languages = languages or ["en"]
        self.proxies = proxies
        if get_video_captions:
            self.get_youtube_video_captions = self.get_youtube_video_captions
        if get_video_data:
            self.get_youtube_video_data = self.get_youtube_video_data
        if get_video_timestamps:
            self.get_video_timestamps = self.get_video_timestamps

    def get_youtube_video_id(self, url: str) -> Optional[str]:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname

        if hostname == "youtu.be":
            return parsed_url.path[1:]
        if hostname in ("www.youtube.com", "youtube.com"):
            if parsed_url.path == "/watch":
                query_params = parse_qs(parsed_url.query)
                return query_params.get("v", [None])[0]
            if parsed_url.path.startswith("/embed/") or parsed_url.path.startswith("/v/"):
                return parsed_url.path.split("/")[2]
        return None

    def get_youtube_video_data(self, url: str) -> str:
        if not url:
            return "No URL provided"

        try:
            video_id = self.get_youtube_video_id(url)
        except Exception:
            return "Error getting video ID from URL, please provide a valid YouTube URL"

        try:
            params = {"format": "json", "url": f"https://www.youtube.com/watch?v={video_id}"}
            oembed_url = "https://www.youtube.com/oembed?" + urlencode(params)

            with urlopen(oembed_url) as response:
                response_text = response.read()
                video_data = json.loads(response_text.decode())
                clean_data = {
                    "title": video_data.get("title"),
                    "author_name": video_data.get("author_name"),
                    "author_url": video_data.get("author_url"),
                    "type": video_data.get("type"),
                    "height": video_data.get("height"),
                    "width": video_data.get("width"),
                    "version": video_data.get("version"),
                    "provider_name": video_data.get("provider_name"),
                    "provider_url": video_data.get("provider_url"),
                    "thumbnail_url": video_data.get("thumbnail_url"),
                }
                return json.dumps(clean_data, indent=4)
        except Exception as e:
            return f"Error getting video data: {e}"

    def get_youtube_video_captions(self, url: str) -> str:
        if not url:
            return "No URL provided"

        try:
            video_id = self.get_youtube_video_id(url)
        except Exception:
            return "Error getting video ID from URL, please provide a valid YouTube URL"

        try:
            kwargs = {"languages": self.languages}
            if self.proxies:
                kwargs["proxies"] = self.proxies

            captions = YouTubeTranscriptApi.get_transcript(video_id, **kwargs)
            if captions:
                return " ".join(line["text"] for line in captions)
            return "No captions found for video"
        except Exception as e:
            return f"Error getting captions for video: {e}"

    def get_video_timestamps(self, url: str) -> str:
        if not url:
            return "No URL provided"

        try:
            video_id = self.get_youtube_video_id(url)
        except Exception:
            return "Error getting video ID from URL, please provide a valid YouTube URL"

        try:
            kwargs = {"languages": self.languages}
            if self.proxies:
                kwargs["proxies"] = self.proxies

            captions = YouTubeTranscriptApi.get_transcript(video_id, **kwargs)
            timestamps = []
            for line in captions:
                start = int(line["start"])
                minutes, seconds = divmod(start, 60)
                timestamps.append(f"{minutes}:{seconds:02d} - {line['text']}")
            return "\n".join(timestamps)
        except Exception as e:
            return f"Error generating timestamps: {e}"
