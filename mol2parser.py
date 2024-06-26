# Copyright (C) 2024 Matthew Richardson

'''
The goal of this parser is to maintain interoperability with Biopython's parsing of PDB files while adding information within mol2 files to Biopython structure objects.

'''

import re

class mol2parser:
    def __init__(self):
        pass

    def parse(file):
        
        with open(file, 'r') as mol2file:
    
        parsedData=[]
        sectionCounter=-1
        
        delimiter=re.compile(r'\s+')
        
        for line in mol2file:
            
            line=line.strip()
            
            if line.startswith('@<TRIPOS>'):
                sectionCounter+=1
                parsedData.append([line.removeprefix('@<TRIPOS>')])
                sectionName=parsedData[sectionCounter][0]
            
            elif line:
                line=delimiter.split(line)      
                parsedData[sectionCounter].append(line)
                        

                    




