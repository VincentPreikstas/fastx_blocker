# -*- coding: utf-8 -*-

"""Main module."""

"VERSION 1"

def block_fastq_file(fastq_file, block_size=1000):
    blocks = ["", "", "", ""]
    counter = 0
    for line in fastq_file:
        blocks[counter % 4] += line
        counter += 1
            

    finishedString = ""
    for temp in blocks:
        finishedString += temp




    return finishedString
