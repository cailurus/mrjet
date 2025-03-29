from typing import Optional
from logger import logger
from curl_cffi import requests
import time


class RequestHandler:
    def __init__(self):
        self.RETRY = 3
        self.DELAY = 2
        self.TIMEOUT = 10
        self.HEADERS = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        }

    def get(
        self,
        url: str,
    ) -> Optional[bytes]:
        for attempt in range(self.RETRY):
            try:
                response = requests.get(
                    url=url,
                    headers=self.HEADERS,
                    timeout=self.TIMEOUT,
                    verify=False,
                )
                return response.content
            except Exception as e:
                logger.error(
                    f"Failed to fetch data (attempt {attempt + 1}/{self.RETRY}): {e} url is: {url}"
                )
                time.sleep(self.DELAY)
        logger.error(f"Max retries reached. Failed to fetch data. url is: {url}")
        return None

    def post(
        self,
        url: str,
        data: dict,
    ) -> Optional[requests.Response]:
        for attempt in range(self.RETRY):
            try:
                response = requests.post(
                    url=url,
                    data=data,
                    headers=self.HEADERS,
                    timeout=self.TIMEOUT,
                    verify=False,
                )
                return response
            except Exception as e:
                logger.error(
                    f"Failed to post data (attempt {attempt + 1}/{self.RETRY}): {e} url is: {url}"
                )
                time.sleep(self.DELAY)
        logger.error(f"Max retries reached. Failed to post data. url is: {url}")
        return None
