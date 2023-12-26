import pytube

from pytube import *

import os

pytube.innertube._default_clients['ANDROID'] = pytube.innertube._default_clients['WEB']

os.chdir("/home/danscot/Downloads")


class Downloader:

    def __init__(self, url):

        self.url = url

        print(self.url)

        self.youtube_video = YouTube(self.url)

        #self.youtube_video.register_on_progress_callback(self.download_progress)

        size = self.youtube_video.streams.get_by_itag(22).filesize_mb

        print(size)

        title = self.youtube_video.title

        print(title)

        #self.youtube_video.streams.get_by_itag(22).download()

    def download_progress(self, stream, chunk, bytes_remaining):

        bytes_downloaded = stream.filesize - bytes_remaining

        percent = bytes_downloaded * 100 / stream.filesize

        print(f"Download progression : {int(percent)}%")

    def bytes_to_megabytes(self, bytes):

        megabytes = bytes / (1024 * 1024)

        return megabytes

    def download_progress(self, stream, chunk, bytes_remaining):

        bytes_downloaded = stream.filesize - bytes_remaining

        percent = bytes_downloaded * 100 / stream.filesize

        print(f"Download progression : {int(percent)}%")

    def video_querry(self, querry):

        search = Search(str(querry))

        print(search.results)



