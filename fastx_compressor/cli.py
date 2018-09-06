# -*- coding: utf-8 -*-

"""Console script for fastx_compressor."""

import click

from .fastx_compressor import block_fastq_file


@click.command()
@click.argument('block_size', type=int)
@click.argument('fastx_file', type=click.File('r'))
def main(block_size, fastx_file):
    """Console script for fastx_compressor."""
    pass


if __name__ == "__main__":
    main()
