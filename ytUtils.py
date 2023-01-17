from youtube_dl import YoutubeDL


def get_yt_url_infos(url):
    try:
        video_infos = YoutubeDL().extract_info(
            url=url,
            download=False
        )
    except:
        return None


    return video_infos
