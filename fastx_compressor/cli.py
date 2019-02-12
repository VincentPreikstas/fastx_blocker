# -*- coding: utf-8 -*-

"""Console script for fastx_compressor."""
from sys import stdout
import click

from .fastx_compressor import block_fastq_file
from .fastx_compressor import deblock_fastq_file

@click.command()
@click.option('--n', default=1000)
@click.argument('fastx_file', type=click.File('r'))
@click.argument('precompressed_file_name')

def precompress(fastx_file, precompressed_file_name, n):
    f = open(precompressed_file_name + ".fq", "w+")
    for strblock in block_fastq_file(fastx_file, n):
        f.write(strblock)
    f.close()

@click.command()
@click.argument('fastx_file_precompressed', type=click.File('r'))
@click.argument('desired_fastx_file_name')

def deprecompress(fastx_file_precompressed, desired_fastx_file_name):
    f = open(desired_fastx_file_name + ".fq", "w+")
    for strblock in deblock_fastq_file(fastx_file_precompressed):
        f.write(strblock)
    f.close()

'''
<<<<<< NOTE FOR DAVID >>>>>>>

Didnt want to remove this part until sure that the main is no longer needed. Also does this have any interaction with the __name__ 
thing? or do we not need the main method call since this is basically just a place to store the functions and the cli.py file is 
never really executed?

'''

'''
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
'''
