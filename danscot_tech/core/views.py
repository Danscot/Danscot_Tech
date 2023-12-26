import io

from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect

import pytube

from pytube import *

# Create your views here.

def home(request):

    return render(request, 'home.html')


def video_query(query):
    # Search for videos

    urls = Search(query).results

    return urls


def downloader(request):

    urls = []

    download_url = str

    if request.method == "POST":

        query = request.POST.get('search')

        if query == None:

            urls = video_query("Rema")

            brain(urls)

        else:

            urls = video_query(query)

            brain(urls)

    context = {

        'urls': urls,
    }

    return render(request, 'downloader.html', context)

def brain(urls):

    for video in urls:

        youtube_url = f'https://www.youtube.com/watch?v={video.video_id}'

        yt = YouTube(youtube_url)

        video.download_link = yt.streams.first().url






