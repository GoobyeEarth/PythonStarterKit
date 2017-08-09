# -*- coding: utf-8 -*-
import click

from app.modules.sample_module import SampleModule


@click.group()
def cmd():
    pass


@cmd.command()
def sample():
    obj = SampleModule()
    print(obj.sample("sample"))


def main():
    cmd()


if __name__ == '__main__':
    main()
