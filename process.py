import ffmpeg
import imagemagick
from pathlib import Path
from pyrnalist.pyrnalist import report

def get_1080p_video(file_path):
    info = ffmpeg.get_video_info(file_path)
    width = int(info['width'])
    height = int(info['height'])

    if height == 1080 and width == 1920:
        return file_path

    return resize_video_to_1080p(file_path, (width, height), (1920, 1080))

FHD_ASPECT_RATIO=0.5625
def resize_video_to_1080p(file_path, source_size, target_size):
    report.verbose('Resizing video file to 1080p')
    (source_width, source_height) = source_size
    (target_width, target_height) = target_size

    video_filter = []
    source_aspect = source_height/source_width
    if source_aspect > FHD_ASPECT_RATIO:
        # pad width
        new_width = int(source_height/FHD_ASPECT_RATIO)
        video_filter.append(f"pad={new_width}:{source_height}:(ow-iw)/2:(oh-ih)/2:color=black")
    elif source_aspect < FHD_ASPECT_RATIO:
        # pad height
        new_height = int(source_width*FHD_ASPECT_RATIO)
        video_filter.append(f"pad={source_width}:{new_height}:(ow-iw)/2:(oh-ih)/2:color=black")
    else:
        # do not pad, just resize
        pass
    video_filter.append("scale=1920:1080")

    file_path = Path(file_path)
    new_file_path = file_path.with_stem(f'{file_path.stem}_1080p')
    if not new_file_path.exists():    
        ffmpeg.filter_video(str(file_path), video_filter, str(new_file_path))
    return new_file_path

def extract_cover_photos(file_path, coverat):
    report.verbose('Extracting cover files')
    base_file_path = Path(file_path).with_suffix('.jpg')
    landscape_path = base_file_path.with_stem(f'{base_file_path.stem}_landscape')
    portrait_path = base_file_path.with_stem(f'{base_file_path.stem}_portrait') 
    pouet_path = base_file_path.with_stem(f'{base_file_path.stem}_pouet')
    if not landscape_path.exists():
        ffmpeg.extract_image(str(file_path), coverat, str(landscape_path))
    if not portrait_path.exists():
        imagemagick.convert(str(landscape_path), str(portrait_path), filters=['-resize', 'x654', '-gravity', 'center', '-crop', '420x654+0+0', '+repage'])
    if not pouet_path.exists():
        imagemagick.convert(str(landscape_path), str(pouet_path), filters=['-resize', '400x300', '-quality', '60'])


def extract_1m_loop(file_path, loopat):
    report.verbose('Extracting 1m video loop')
    file_path = Path(file_path)
    loop_path = file_path.with_stem(f'{file_path.stem}_1m_loop')
    if not loop_path.exists():
        ffmpeg.extract_1m_loop(str(file_path), loopat, str(loop_path))