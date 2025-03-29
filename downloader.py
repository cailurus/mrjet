from typing import Optional
from logger import logger
import m3u8
import re
from request_handler import RequestHandler
from pym3u8downloader import M3U8Downloader


class MovieDownloader:
    def __init__(self):
        self.request_handler = RequestHandler()

    def _get_last_variant(self, m3u8_content: str) -> Optional[str]:
        playlist = m3u8.loads(m3u8_content)
        if playlist.is_variant:
            last_variant = playlist.playlists[-1].uri
            return last_variant
        else:
            return None

    def _get_uuid(self, html: str) -> Optional[str]:
        uuid_match = re.search(r"m3u8\|([a-f0-9\|]+)\|com\|surrit\|https\|video", html)
        uuid_result = uuid_match.group(1)
        if not uuid_result:
            logger.error("Failed to extract UUID from HTML.")
            return None
        uuid = "-".join(uuid_result.split("|")[::-1])
        return uuid

    def _get_movie_id(self, url: str) -> Optional[str]:
        movie_id = url.split("/")[-1]
        if not movie_id:
            logger.error("Failed to extract movie ID from URL.")
            return None
        return movie_id

    def download(self, url: str) -> None:
        page_html = self.request_handler.get(url).decode("utf-8")
        uuid = self._get_uuid(page_html)
        movie_id = self._get_movie_id(url)

        m3u8_url = f"https://surrit.com/{uuid}/playlist.m3u8"
        m3u8_html = self.request_handler.get(m3u8_url).decode("utf-8")
        res_part = self._get_last_variant(m3u8_html)

        video_url = f"https://surrit.com/{uuid}/{res_part}"

        downloader = M3U8Downloader(
            input_file_path=video_url,
            output_file_path=f"output/{movie_id}.mp4",
        )

        downloader.download_playlist()
