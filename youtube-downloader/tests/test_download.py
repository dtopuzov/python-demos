"""
Download youtube videos as mp3.
"""

import pytest

from data.playlist import get_playlist
from pages.youtube import YouTube320


@pytest.mark.parametrize("video", get_playlist())
def test_download(browser, video):
    youtube = YouTube320(browser)
    youtube.download(video)
