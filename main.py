#!/usr/bin/python3
from random import randint
from tabulate import tabulate

f = open("address.txt", "r")
TLB = dict()
TLB_MAX = 16

tlbHits = 0
tlbMisses = 0
pageFaults = 0

fifoStack = list()

physicalMemoryStart = 512
physicalMemoryEnd = 4096

def getPhysicalAddr(offset = 0):
    return randint(physicalMemoryStart, physicalMemoryEnd) + offset

for line in f:
    valDec = int(line, 16)
    valHex = str(hex(valDec))
    valBin = str(bin(valDec))

    # print(valDec, "\t", valBin)
    logicalAddr = int(valBin[2:len(valBin) - 4], 2)
    offset = int(valBin[-4:], 2)

    if logicalAddr in TLB:
        tlbHits += 1
    else:
        tlbMisses += 1
        if len(TLB) < TLB_MAX:
            fifoStack.append(logicalAddr)
            TLB[logicalAddr] = getPhysicalAddr(offset)
        elif len(fifoStack) != 0 and len(TLB) == TLB_MAX:
                del TLB[fifoStack.pop()]
                fifoStack.append(logicalAddr)
                TLB[logicalAddr] = getPhysicalAddr(offset)

print("Summary:")
print("\nPhysical Mem. Range : %d-%d"%(physicalMemoryStart, physicalMemoryEnd))
print("TLB Length : %d\n"%TLB_MAX)
print("+------------------------+")
print("|       TLB Contents     |")
print("|------------------------|")
print(tabulate(TLB.items(), headers=['Logical', 'Physical'], tablefmt='orgtbl'))    
print("+------------------------+")
print("\nTLB Hits : ", tlbHits)
print("TLB Misses : ", tlbMisses)