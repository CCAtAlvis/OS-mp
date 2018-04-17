#!/usr/bin/python3

f = open("address.txt", "r")
TLB = dict()

for line in f:
    valDec = int(line, 16)
    valHex = hex(valDec)
    valBin = bin(valDec)

    print(str(valHex)+"\t"+str(valDec)+"\t"+str(valBin))

    pageAddress = 

    for i in range(len(TLB)):
        TLB[i] += 1

        if 


# for (i=0; i<pageCount; ++i) {
#     for (j=0; j<n; j++) {
#         // check if page exist in cache
#         if (LRUStack[j][0] == pageSequence[i]) {
#             hitCount++;
#             flag = 1;
#             LRUStack[j][1] = 1;
#         } else {
#             LRUStack[j][1]++;
#         }
#     }

#     if(!flag) {
#         // now that the page doesn't exist
#         // push it in
#         leastUsed = 0;
#         for (j=0; j<n; ++j) {
#             if (LRUStack[j][1] > LRUStack[leastUsed][1])
#                 leastUsed = j;
#         }

#         LRUStack[leastUsed][0] = pageSequence[i];
#         LRUStack[leastUsed][1] = 1;
#     }

#     flag = 0;
# }
# printf("Hit Count in LFU: %d\n", hitCount);
