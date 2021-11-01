#!/usr/local/bin/python3

import os
import subprocess

with open('input.txt') as mylines :
 my_file_contents = mylines.read().upper().split()
with open('Cleaned_sequences.txt','w') as cleanedseqs :
 for cleanones in my_file_contents :
  cleanedseqs.write(cleanones[14:] + '\n')
  f'{cleanones[14 :]}'

subprocess.call("cat Cleaned_sequences.txt",shell=True)




