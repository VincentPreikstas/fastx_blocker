# -*- coding: utf-8 -*-

"""Console script for fastx_compressor."""
from sys import stdout
import click

from .fastx_compressor import block_fastq_file
from .fastx_compressor import deblock_fastq_file

@click.command()
@click.argument('block_size', type=int)
@click.argument('fastx_file', type=click.File('r'))
def main(fastx_file, block_size=1000):
    """Console script for fastx_compressor."""
    f = open("precompression.fq", "w+")
    for strblock in block_fastq_file(fastx_file, block_size):
        
        f.write(strblock)
        #stdout.write(strblock)

    f.close()
    fr = open("precompression.fq", "r")
    ff = open("originalFile.fq", "w+")
    for strblock in deblock_fastq_file(fr):

        ff.write(strblock)
        #stdout.write(strblock)

    ff.close()



if __name__ == "__main__":
    main()
