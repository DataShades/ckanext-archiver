import click

import ckanext.archiver.utils as utils

def get_commands():
    return [archiver]


@click.group()
def archiver():
    pass

@archiver.command()
def init():
    utils.cmd_init()
