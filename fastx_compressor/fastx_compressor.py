# -*- coding: utf-8 -*-



"""Main module."""

"VERSION 1"

RECORD_LENGTH = 4

def block_fastq_file(fastq_file, block_size=1000):
    """Yield blocks from the file."""
    finishedString = ""
    blocks = ["", "", "", ""]
    counter = 0


    for line in fastq_file:
        blocks[counter % 4] += line
        counter += 1
        if counter // BLOCK_LENGTH == block_size:
            for temp in blocks:
                finishedString += temp
            
            finishedString = "# BLOCK_SIZE " + str(block_size) +"\n" + finishedString

            yield finishedString
            finishedString = ""
            blocks = ["", "", "", ""]
            counter = 0

    for temp in blocks:
        finishedString += temp

    totalSize = counter // BLOCK_LENGTH
    totalSize = str(totalSize)
    totalSize = "# BLOCK_SIZE " + totalSize + "\n"
    finishedString = totalSize + finishedString

    yield finishedString


def deblock_fastq_file(fastq_file, block_size=1000):
    blocks = ["", "", "", ""]
