import datetime
import sh


def check_binaries():
    sh.ensure("ffmpeg")
    sh.ensure("ffprobe")


def get_file_info(file_path):
    result = sh.execute(
        [
            "ffprobe",
            "-v",
            "error",
            "-hide_banner",
            "-i",
            file_path,
            "-show_format",
            "-show_streams",
        ]
    )
    info = {"format": {}, "streams": []}
    lines = iter(result.stdout.splitlines())
    while (line := next(lines, None)) is not None:
        if line == "[FORMAT]":
            while (line := next(lines, None)) is not None and line != "[/FORMAT]":
                datum = line.split("=")
                info["format"][datum[0]] = datum[1]
        elif line == "[STREAM]":
            stream = {}
            while (line := next(lines, None)) is not None and line != "[/STREAM]":
                datum = line.split("=")
                stream[datum[0]] = datum[1]
            info["streams"].append(stream)
    return info


def get_video_info(file_path):
    info = get_file_info(file_path)
    video_streams = filter(lambda i: i["codec_type"] == "video", info["streams"])
    return next(iter(video_streams or []), None)


def extract_image(file_path, timestamp, output_path):
    timestamp = str(datetime.timedelta(seconds=timestamp))
    result = sh.execute(
        [
            "ffmpeg",
            "-y",
            "-ss",
            timestamp,
            "-i",
            file_path,
            "-vframes",
            "1",
            "-q:v",
            "2",
            output_path,
        ]
    )
    # TODO: Error handling


def extract_1m_loop(file_path, timestamp, output_path):
    timestamp = str(datetime.timedelta(seconds=timestamp))
    result = sh.execute(
        [
            "ffmpeg",
            "-y",
            "-ss",
            timestamp,
            "-i",
            file_path,
            "-t",
            "00:59",
            "-codec",
            "copy",
            output_path,
        ]
    )
    # TODO: Error handling


def filter_video(file_path, video_filters, output_path):
    vf = ", ".join(video_filters)
    result = sh.execute(
        ["ffmpeg", "-y", "-i", file_path, "-vf", vf, "-c:a", "copy", output_path]
    )
