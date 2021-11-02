import ffmpeg
import demozoo
from pyrnalist.pyrnalist import report


def platform_to_hashtag(p):
    match p['name']:
        case 'Acorn Archimedes': return ['#acorn']
        case 'Amiga AGA': return ['#amiga', '#amigaaga', '#aga']
        case 'Amiga OCS/ECS': return ['#amiga', '#amigaocs', '#amigaecs']
        case 'Amiga PPC/RTG': return ['#amiga', '#amigappc', '#amigartg']
        case 'Amstrad CPC': return ['#amstrad', '#amstradcpc']
        case 'Amstrad Plus': return ['#amstrad', '#amstradplus']
        case 'Android': return ['#mobile', '#android']
        case 'Apple II' | 'Apple II GS': return ['#apple', '#apple2', '#appleii']
        case 'Atari 2600 Video Computer System (VCS)': return ['#atari', '#atari2600', '#atarivcs']
        case 'Atari 7800 ProSystem': return ['#atari']
        case 'Atari 8 bit': return ['#atari', '#atarixlxe']
        case 'Atari Falcon': return ['#atari']
        case 'Atari Jaguar': return ['#atari']
        case 'Atari Lynx': return ['#atari']
        case 'Atari ST/E': return ['#atari', '#atariste']
        case 'Atari TT': return ['#atari']
        case 'BBC Micro': return []
        case 'BeOS': return []
        case 'Browser': return []
        case 'Calculator': return []
        case 'ColecoVision': return []
        case 'Commodore 128': return []
        case 'Commodore 16/Plus 4': return []
        case 'Commodore 64': return ['#c64', '#commodore', '#commodore64']
        case 'Commodore 64-DTV': return []
        case 'Commodore PET': return []
        case 'Console Handheld': return []
        case 'Custom Hardware': return []
        case 'Electronika BK-0010/11M': return []
        case 'Enterprise': return []
        case 'Flash': return []
        case 'FreeBSD': return []
        case 'Gamepark 32': return []
        case 'Gamepark GP2X': return []
        case 'Intellivision': return []
        case 'Java': return []
        case 'Javascript': return []
        case 'KC 85/Robotron KC 87': return []
        case 'Linux': return []
        case 'MS-Dos': return ['#pc', '#pcdos', '#dos', '#msdos']
        case 'MSX': return []
        case 'Mac OS X': return []
        case 'Mobile': return []
        case 'NEC PC Engine': return []
        case 'NeoGeo': return []
        case 'Nintendo 3DS': return []
        case 'Nintendo 64 (N64)': return []
        case 'Nintendo DS (NDS)': return []
        case 'Nintendo Entertainment System (NES)': return []
        case 'Nintendo GameBoy (GB)': return []
        case 'Nintendo GameBoy Advance (GBA)': return []
        case 'Nintendo GameBoy Color (GBC)': return []
        case 'Nintendo GameCube (NGC)': return []
        case 'Nintendo SNES/Super FamiCom': return []
        case 'Nintendo Wii': return []
        case 'Oric': return []
        case 'PICO-8': return []
        case 'PMD 85': return []
        case 'Paper': return []
        case 'Raspberry Pi': return []
        case 'SAM Coupé': return []
        case 'Sega Dreamcast': return []
        case 'Sega Master System': return []
        case 'Sega Megadrive/Genesis': return []
        case 'Sharp MZ': return []
        case 'Sony Playstation 1 (PSX)': return []
        case 'Sony Playstation 2 (PS2)': return []
        case 'Sony Playstation 3 (PS3)': return []
        case 'Sony Playstation Portable (PSP)': return []
        case 'TIC-80': return []
        case 'Thomson': return []
        case 'VIC-20': return []
        case 'VTech Laser 200 / VZ 200': return []
        case 'Vector-06C': return []
        case 'Vectrex': return []
        case 'Windows': return ['#pc', '#windows', '#win32']
        case 'XBOX': return []
        case 'XBOX360': return []
        case 'ZVT PP01': return []
        case 'ZX Spectrum': return ['#zx', '#spectrum', ]
        case 'ZX Spectrum Enhanced': return []
        case 'ZX81': return []
        case _: return []

def get_platform_hashtags(data):
    tags = []
    for platform in data['platforms']:
        tags.append(platform_to_hashtag(platform))
    return [item for sublist in tags for item in sublist]

def type_to_hashtag(t):
    match t['name']:
        case 'Demo': return ['#demo']
        case 'Game': return []
        case 'Graphics': return []
        case 'Artpack': return []
        case 'ASCII': return []
        case 'ASCII Collection': return []
        case 'Photo': return []
        case 'ANSI': return []
        case 'Executable Graphics': return []
        case '4K Executable Graphics': return []
        case 'Intro': return []
        case 'BBStro': return []
        case 'Cracktro': return []
        case '32b Intro': return []
        case '64b Intro': return []
        case '128b Intro': return []
        case '256b Intro': return []
        case '512b Intro': return []
        case '1K Intro': return []
        case '2K Intro': return []
        case '4K Intro': return []
        case '8K Intro': return []
        case '16K Intro': return []
        case '32K Intro': return []
        case '40k Intro': return []
        case '64K Intro': return ['#intro', '#intro64']
        case '96K Intro': return []
        case '100K Intro': return []
        case 'Invitation': return []
        case 'Magazine': return []
        case 'Diskmag': return []
        case 'Papermag': return []
        case 'Textmag': return []
        case 'Music': return []
        case 'Executable Music': return []
        case '32K Executable Music': return []
        case '64K Executable Music': return []
        case 'Music Pack': return []
        case 'Streaming Music': return []
        case 'Tracked Music': return []
        case 'Musicdisk': return []
        case 'Chip Music Pack': return []
        case 'Pack': return []
        case 'Docsdisk': return []
        case 'Performance': return []
        case 'Report': return []
        case 'Slideshow': return []
        case 'Tool': return []
        case 'Video': return []
        case 'Votedisk': return []
        case _: return []
    
def get_type_hashtags(data):
    tags = []
    for platform in data['platforms']:
        tags.append(type_to_hashtag(platform))
    return [item for sublist in tags for item in sublist]


COMMON_HASHTAGS = ['#video', '#preservation',  '#classic', '#aesthetic', '#retrostyle', '#style', '#nostalgia', '#design', '#retro', '#vintage', '#art', '#oldschool', '#demoscene']
def get_hashtags(data):
    tags = [COMMON_HASHTAGS, get_type_hashtags(data), get_platform_hashtags(data)]
    return ' '.join([item for sublist in tags for item in sublist])

def get_title(data):
    return data['title']

def get_all_releasers(data):
    return "^".join(map(lambda x: x['name'], data['author_nicks']))

PC_PLATFORM_NAMES = ['Mac OS X', 'MS-Dos', 'Linux', 'FreeBSD', 'Windows']
def get_platform_name(data):
    if data in PC_PLATFORM_NAMES:
        return f'PC {data}'
    return data

def get_video_quality(data):
    r_frame_rate = data['r_frame_rate'].split('/')
    height = data['height']
    frame_rate = int(r_frame_rate[0])
    if len(r_frame_rate) > 1:
        frame_rate = int(frame_rate / int(r_frame_rate[1]))
    return f'{height}p{frame_rate}'

def ordinal_suffix_of(i):
    i = int(i)
    j = i % 10
    k = i % 100
    if j == 1 and k != 11: return f'{i}st'
    if j == 2 and k != 12: return f'{i}nd'
    if j == 3 and k != 13: return f'{i}rd'
    return f'{i}th'

MONTH_NAMES = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]
def format_date(data):
    if not data:
        return None

    parts = [int(x) for x in data.split('-')]
    match len(parts):
        case 1: return f'in {parts[0]}'
        case 2: return f'in {MONTH_NAMES[parts[1]-1]} {parts[0]}'
        case 3: return f'on {ordinal_suffix_of(parts[2])} {MONTH_NAMES[parts[1]-1]} {parts[0]}'

def get_party_info(data):
    if not data or len(data) < 1:
        return None
    
    placing = data[0]
    place = placing.get('position')
    place_info = f'{ordinal_suffix_of(place)} ' if place and place <= 3 else ''
    party_name = placing['competition']['party']['name']
    compo_name = placing['competition']['name']
    return f'{place_info}in the {party_name} "{compo_name}" competition'

def get_party_info_short(data):
    if not data or len(data) < 1:
        return None
    
    placing = data[0]
    place = placing.get('position')
    place_info = f'{ordinal_suffix_of(place)} ' if place and place <= 3 else ''
    party_name = placing['competition']['party']['name']
    return f'{place_info}in the {party_name}'

def get_release_info_full(data):
    release_info = format_date(data.get('release_date'))
    party_info = get_party_info(data.get('competition_placings'))
    if release_info and party_info: return f'{release_info} · {party_info}'
    elif release_info: return release_info
    elif party_info: return party_info
    else: return ''

def get_release_info_short(data):
    info = []
    party_info = get_party_info_short(data.get('competition_placings'))
    if party_info:
        info.append(party_info)
    else:
        year = data['release_date'].split('-')[0]
        info.append(year)

    if data.get('types') and len(data['types']) > 0:
        info.append(data['types'][0]['name'])

    if data.get('platforms') and len(data['platforms']) > 0:
        name = get_platform_name(data['platforms'][0]['name'])
        info.append(name)

    return ' · '.join(info)


def get_credits(data):
    credits = {}
    for datum in data['credits']:
        name = datum['nick']['name']
        credit = datum['category']
        role = datum.get('role')
        if role:
            credit = f'{credit} ({role})'
        credits.setdefault(name,[]).append(credit)
    result = []
    for author in sorted(credits.keys()):
        all_roles = ', '.join(credits.get(author))
        result.append(f'{author} - {all_roles}')
    return '\n'.join(result)


def get_external_links(data):
    urls = [link['url'] for link in data['external_links'] if link['link_class'] != 'YoutubeVideo']
    urls.insert(0, data['demozoo_url'])
    return '\n'.join(urls)


def get_youtube_link(data):
    link = [link['url'] for link in data['external_links'] if link['link_class'] == 'YoutubeVideo']
    return link[0] if link and len(link) > 0 else ''


def get_extras(data):
    extras = []
    if 'release_date' in data:
        year = data['release_date'].split('-')[0]
        extras.append(year)
    if 'platforms' in data and len(data['platforms']) > 0:
        type = data['platforms'][0]['name']
        extras.append(get_platform_name(type))
    extras_string = ''
    if len(extras) > 0:
        extras_string = f' ({", ".join(extras)})'
    return extras_string

class yt:
    name = 'YouTube'
    def content(self, demozoo_info, video_info): return [self.__get_title(demozoo_info, video_info), self.__get_description(demozoo_info)]
    def __get_title(self, demozoo_info, video_info):
        title = get_title(demozoo_info)
        all_releasers = get_all_releasers(demozoo_info)
        extras_string = get_extras(demozoo_info)
        video_info = get_video_quality(video_info)
        return f'{title} / {all_releasers}{extras_string} | {video_info}'
    def __get_description(self, demozoo_info): return f'Released {get_release_info_full(demozoo_info)}\n\nCredits:\n{get_credits(demozoo_info)}\n\nYou can find original production at:\n{get_external_links(demozoo_info)}\n'


class ttfb:
    name = 'Twitter/Facebook'
    def content(self, demozoo_info, video_info): return [self.__get_description(demozoo_info)]
    def __get_description(self, demozoo_info):
        title = get_title(demozoo_info)
        releasers = get_all_releasers(demozoo_info)
        info = get_release_info_short(demozoo_info)
        youtube_link = get_youtube_link(demozoo_info)
        hashtags = get_hashtags(demozoo_info)
        return f'{title} / {releasers}\n{info}\n\n{youtube_link}\n\n{hashtags}'


class igfeed:
    name = 'Instagram Feed'
    def content(self, demozoo_info, video_info): return [self.__get_description(demozoo_info)]
    def __get_description(self, demozoo_info):
        title = get_title(demozoo_info)
        releasers = get_all_releasers(demozoo_info)
        info = get_release_info_short(demozoo_info)
        hashtags = get_hashtags(demozoo_info)
        return f'{title} / {releasers}\n{info}\n\nMore on IGTV.\n\n{hashtags}'

class igtv:
    name = 'Instagram TV'
    def content(self, demozoo_info, video_info): return [ self.__get_title(demozoo_info, video_info), self.__get_description(demozoo_info)]
    def __get_title(self, demozoo_info, video_info):
        title = get_title(demozoo_info)
        releasers = get_all_releasers(demozoo_info)
        extras = get_extras(demozoo_info)
        return f'{title} / {releasers}{extras}'

    def __get_description(self, demozoo_info):
        info = get_release_info_full(demozoo_info)
        credits = get_credits(demozoo_info)
        links = get_external_links(demozoo_info)
        hashtags = get_hashtags(demozoo_info)
        return f'Released {info}\n\nCredits:\n{credits}\n\nYou can find original production at:\n{links}\n\n{hashtags}'

def get_hashtags_for_tktk_limit(data, content):
    return get_hashtags(data)

class tktk:
    name = 'TikTok'
    def content(self, demozoo_info, video_info): return [self.__get_description(demozoo_info)]
    def __get_description(self, demozoo_info):
        title = get_title(demozoo_info)
        releasers = get_all_releasers(demozoo_info)
        release_date = demozoo_info.get('release_date')
        year = f' ({release_date.split("-")[0]})' if release_date else ''
        content = f'{title} / {releasers}{year} · '
        hashtags = get_hashtags_for_tktk_limit(demozoo_info, content)
        return f'{content}{hashtags}'

SOCIAL_MEDIA_ACCOUNTS = [ yt, ttfb, igfeed, igtv, tktk ]
def get(file_path, url):
    video_info = ffmpeg.get_video_info(file_path)
    demozoo_info = demozoo.get_production_info(url)

    for c in SOCIAL_MEDIA_ACCOUNTS:
        instance = c()
        report.list(instance.name, instance.content(demozoo_info, video_info))
    