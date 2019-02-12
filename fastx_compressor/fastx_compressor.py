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
        blocks[counter % RECORD_LENGTH] += line
        counter += 1
        if counter // RECORD_LENGTH == block_size:
            for temp in blocks:
                finishedString += temp
            
            finishedString = "# BLOCK_SIZE " + str(block_size) +"\n" + finishedString

            yield finishedString
            finishedString = ""
            blocks = ["", "", "", ""]
            counter = 0

    for temp in blocks:
        finishedString += temp

    totalSize = counter // RECORD_LENGTH
    totalSize = str(totalSize)
    totalSize = "# BLOCK_SIZE " + totalSize + "\n"
    finishedString = totalSize + finishedString

    yield finishedString


def deblock_fastq_file(fastq_file):
    """Rebuilds original file"""
    counter = 0

    for line in fastq_file:
        if counter == 0:
            numberOfBlocks = int(line.split()[2])
            numberOfLines = numberOfBlocks * RECORD_LENGTH + 1
            blocks = [""] * numberOfBlocks
            counter += 1

        else:
            blocks[(counter - 1) % numberOfBlocks] += line
            counter += 1

            if counter % numberOfLines == 0:
                counter = 0
                finishedString = ""
                for temp in blocks:
                    finishedString += temp

                yield finishedString
