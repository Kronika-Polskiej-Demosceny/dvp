import re
import requests
from pyrnalist.pyrnalist import report

__DEMOZOO_API_URL = 'https://demozoo.org/api/v1/'
__DEMOZOO_PRODUCTION_RE = r"https:\/\/demozoo\.org\/productions\/(\d+)"

def __get_demozoo_production_id_from_url(url):
    matches = re.search(__DEMOZOO_PRODUCTION_RE, url, re.IGNORECASE)
    if not matches:
        report.warn(f'Could not find production id in url: {url}')
        return None
    id = int(matches.group(1))
    report.verbose(f'Found production id: {id}')
    return id

def get_production_info(url):
    id = __get_demozoo_production_id_from_url(url)
    api_url = f'{__DEMOZOO_API_URL}productions/{id}'
    report.verbose(f'Fetching Demozoo API: {api_url}')
    r = requests.get(api_url)
    if r.status_code != 200:
        report.error(f'Failed status code: {r.status_code}')
        return None
    data = r.json()
    id = data['id']
    title = data['title']
    report.verbose(f'Got response for id={id}, title={title}')
    return data