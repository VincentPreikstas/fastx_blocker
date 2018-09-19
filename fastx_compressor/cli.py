# -*- coding: utf-8 -*-

"""Console script for fastx_compressor."""

import click

from .fastx_compressor import block_fastq_file


@click.command()
@click.argument('block_size', type=int)
@click.argument('fastx_file', type=click.File('r'))
def main(fastx_file, block_size=1000):
    """Console script for fastx_compressor."""
    for block in block_fastq_file(fastx_file, block_size):
        print(block)
    



if __name__ == "__main__":
    main()
