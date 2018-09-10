# -*- coding: utf-8 -*-

"""Main module."""

"VERSION 1.2"

def block_fastq_file(fastq_file, block_size=1000):
    blocks = ["", "", "", ""]
    counter = 0
    for line in fastq_file:
        blocks[counter % 4] += "\n" + line
        counter += 1
            

    finishedString = ""
    for temp in blocks:
        finishedString += "\n" + temp

    finishedString.lstrip()


    return finishedString


"VERSION 1.1.1"

"""

def block_fastq_file(fastq_file, block_size=1000):
    blocks = ["", "", "", ""]
    counter = 0
    (fastq_file) as x:
        for line in x:
            if counter != 3:
                blocks[counter] = blocks[counter] + \n + line
                counter ++
            else:
                blocks[counter] = blocks[counter] + \n + line
                counter = 0
    finishedString = ""
    for temp in blocks:
        finishedString = finishedString + \n + temp

    finishedString.lstrip()


    return finishedString
"""

"VERSION 1.1"
"""
def block_fastq_file(fastq_file, block_size=1000):
    blocks = ["", "", "", ""]
    counter = 0
    (fastq_file) as x:
        for line in x:
            if counter == 0:
                blocks[counter] = blocks[counter] + \n + line
                counter ++
            elif counter == 1:
                blocks[counter] = blocks[counter] + \n + line
                counter++
            elif counter == 2:
                blocks[counter] = blocks[counter] + \n + line
                counter++
            else:
                blocks[counter] = blocks[counter] + \n + line
                counter = 0
    finishedString = ""
    for temp in blocks:
        finishedString = finishedString + \n + temp

    finishedString.lstrip()


    return finishedString

"""

"VERSION 1"

"""

def block_fastq_file(fastq_file, block_size=1000):
    firstString = ""
    secondString = ""
    thirdString = ""
    fourthString = ""
    counter = 0
    with open(fastq_file) as x:
        for line in x:
            if counter == 0:
                firstString = firstString + \n + line
                counter++
            elif counter == 1:
                secondString = secondString + \n + line
                counter++
            elif counter == 2:
                thirdString = thirdString + \n + line
                counter++
            else:
                fourthString = fourthString + \n + line
                counter = 0
    finishedString = firstString + \n + secondString + \n + thirdString + \n + fourthString

    return finishedString

"""         



"Yield lines from a blocked fastq file starting with the header line."
