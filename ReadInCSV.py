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
##            print(line)
            print(line, file=fout, end='')

    with open(filename+'.lst', "wt") as fout:
        srcLines = []
        ln = int(0)
        for line in lines:
            ln += 1
            if ln == 1:
                firstLine = line
            elif ln == 2:
                secondLine = line
            elif ln == 3 or ln == 5:
                pass
            elif ln == 4:
                fourthLine = line
                titles = fourthLine.split(",")
                numTitles = len(titles)
                for j in range(numTitles):
                    if j != (numTitles - 1):
                        titles[j] = titles[j].strip('"')
                    else:
                        titles[j] = titles[j].lstrip('"').rstrip('"\n')
                print(titles)
                print(titles, file=fout)
            else:
                fields = line.split('","')
                fields[0] = fields[0].lstrip('"')
                fields[4] = fields[4].rstrip('"\n')
                print(fields)
                print(fields, file=fout)
                srcLines.append(fields)
            

