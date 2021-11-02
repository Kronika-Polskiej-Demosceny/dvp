# -*- coding: utf-8 -*-
import json
import click
import os
from pathlib import Path
from dotenv import load_dotenv
import imagemagick
import ffmpeg
from pytimeparse import parse as timeparse
from pyrnalist import report
from process import get_1080p_video, extract_1m_loop, extract_cover_photos
import info

DVP_VERSION = '0.0.1'

@click.group()
@click.pass_context
def cli(ctx):
    ffmpeg.check_binaries()
    imagemagick.check_binaries()

    ctx.ensure_object(dict)
    ctx.obj['INPUT'] = input

def validate_timedelta(ctx, param, value):
    seconds = timeparse(value)
    if seconds:
        return seconds
    try:
        return int(value)
    except:
        raise click.BadParameter("format must be HH:MM:SS, MM:SS or SS")

@cli.command()
@click.pass_context
@click.option('-i', '--input', type=click.Path(file_okay=True,dir_okay=False,writable=False,readable=True), default=os.path.join(click.get_app_dir("dvp"), "data"))
@click.option('-c', '--coverat', type=click.UNPROCESSED, callback=validate_timedelta, default="0")
@click.option('-l', '--loopat', type=click.UNPROCESSED, callback=validate_timedelta, default="0")
def process(ctx, input, coverat, loopat):
    report.header('dvp', 'process', DVP_VERSION)
    report.info(f'Processing file: {input}')
    input = get_1080p_video(input)
    extract_cover_photos(input, int(coverat))
    extract_1m_loop(input, int(loopat))
    report.footer()

@cli.command()
@click.pass_context
@click.option('-i', '--input', type=click.Path(file_okay=True,dir_okay=False,writable=False,readable=True), default=os.path.join(click.get_app_dir("dvp"), "data"))
@click.option('-u', '--url', type=str)
def getinfo(ctx, input, url):
    report.header('demoscene video processor', 'getinfo', DVP_VERSION)
    report.info(f'Getting info for file: {input} from: {url}')
    info.get(input, url)
    report.footer()

if __name__ == '__main__':
    load_dotenv()
    cli(obj={}, auto_envvar_prefix='DVP')
