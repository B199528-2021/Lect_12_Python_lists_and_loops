#!/usr/local/bin/python3

import shutil
import os


shutil.copy("../Lect_11/remote_exon01.fasta", ".")

print(sorted(os.listdir()))

print(open('remote_exon01.fasta').read().split())

AJ223353_seq = open('remote_exon01.fasta').read().split()[1]
print(len(AJ223353_seq))

print(AJ223353_seq[-3:])

print(len(AJ223353_seq[0:30]))

windowsize = 30
offset = 3

segment_starts = list(range(0,len(AJ223353_seq)-windowsize+1,offset))
segment_starts = list(range(0,len(AJ223353_seq),offset))
print(segment_starts)

basic_fasta_header = '_window' + str(windowsize) + '_offset' + str(offset)

alloutfilename = 'AJ223353_coding_all' + basic_fasta_header + '.fasta'
with open(alloutfilename, 'w') as allsegments :
 allsegments.write('')
# Create a blank list to hold the segments
 segments_made = []
# Create a possible yes/no switching variable, i.e. a conditional
 fileswanted = 1
# The for loop
 for seg_bits in segment_starts :
     tempseq = AJ223353_seq[seg_bits :seg_bits+windowsize].upper()
     segments_made = segments_made + [tempseq]
# percentage GC content, convert float to integer value
     tempGC = int(100 * (tempseq.count('G') + tempseq.count('C'))/len(tempseq) )
# make a fasta header line
     descriptionline = 'AJ223353_coding_'+str(len(segments_made))+'_'+tempseq+basic_fasta_header
     fastaheader = '>'+descriptionline
     print(len(segments_made),'\t',tempseq,'\t',tempGC)
# Question : do we want files written? Answer will be either True or False ('maybe' is NOT an option!)
     if fileswanted == 1 :
# open the segment fastafiles
        with open(descriptionline+'.fasta', 'w') as segmentfile :
# output to files
          segmentfile.write(fastaheader+'\n'+tempseq)
          allsegments.write(fastaheader+'\n'+tempseq+'\n\n')
     else :
        allsegments.close()

print(segmentfile.closed)
print(allsegments.closed)

print('\n'.join(segments_made[0:10]))

print(' then '.join(segments_made[0:3]))

for these in 1,2,3 :
    open(alloutfilename).read().split('>')[these]

print('\n'.join(open(alloutfilename).read().split('\n\n')[0 :3]))

my_file = open(alloutfilename)
for line in my_file :
    print(line.rstrip('\n\n'))

print(dir())

print('os' in dir())

print(os.getcwd())

print(len(os.listdir()))

print(os.listdir()[0])
print(os.listdir()[1])

import glob
print(glob.glob('*.dna'))
print(len(glob.glob('*.dna')))
print(glob.glob('*.txt'))
