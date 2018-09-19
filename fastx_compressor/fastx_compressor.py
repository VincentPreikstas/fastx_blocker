# -*- coding: utf-8 -*-



"""Main module."""

"VERSION 1"



def block_fastq_file(fastq_file, block_size=1000):
    #globalish variables
    BLOCK_LENGTH = 4
    finishedString = ""
    blocks = ["", "", "", ""]
    counter = 0


    for line in fastq_file:
        blocks[counter % 4] += line
        counter += 1
        #Check for when block size achieved
        if (counter / BLOCK_LENGTH == block_size):
            for temp in blocks:
                finishedString += temp
            
            finishedString = "Total in block: " + str(block_size) +"\n" + finishedString

            #yield block and reset variables for next block
            yield finishedString
            finishedString = ""
            blocks = ["", "", "", ""]
            counter = 0

            

    #build final incomplete block
    for temp in blocks:
        finishedString += temp
    totalSize = counter / BLOCK_LENGTH

    totalSize = int(totalSize)

    totalSize = str(totalSize)
    totalSize = "Total in block: " + totalSize + "\n"
    finishedString = totalSize + finishedString





    yield finishedString


def deblock_fastq_file(fastq_file, block_size=1000):
    blocks = ["", "", "", ""]
