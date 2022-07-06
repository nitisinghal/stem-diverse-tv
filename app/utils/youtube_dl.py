import youtube_dl


def youtube_dl_extract_info(video_id):
    ydl = youtube_dl.YoutubeDL()

    full_video_url = "%s%s" % ("https://www.youtube.com/watch?v=", video_id)

    with ydl:
        result = ydl.extract_info(full_video_url, download=False)
    return result


def youtube_dl_extract_format(info, format_id):
    result = []
    for i in info.get("formats"):
        if int(i.get("format_id")) == format_id:
            result.append(i.get("url"))
    if not result:
        result.append({"message": f"Requested format '{format_id}' is not available"})
    return result
