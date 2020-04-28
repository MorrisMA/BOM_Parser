import sys
import re

if len(sys.argv) < 2:
    print('Usage: python makeBOM.py filename [options]' \
          '\n\tinput  < "filename".csv.' \
          '\n\toutput > "filename".bom.')
else:
    filename = sys.argv[1]

    with open(filename+'.csv', "rt") as finp:
        lines = finp.readlines()

    '''
        Write out the source file with the comments stripped out.
    '''

    with open(filename+'.bom', "wt") as fout:
        for line in lines:
            print(line)
            print(line, file=fout, end='')
            

