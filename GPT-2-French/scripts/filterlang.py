#!/usr/bin/env python3

import sys
import os
import multiprocessing
from langdetect import detect_langs

def process_file(filename):
    flangs = []
    infile = os.path.join(indir, filename)
    outfile = os.path.join(outdir, filename)
    try:
        with open(infile, "r") as f:
            flangs = detect_langs(f.read())
        if flangs[0].lang == lang and flangs[0].prob > 0.99999:
            print("Moving %s: %s" %(infile, flangs))
            os.rename(infile, outfile)
        else:
            print("Skipping %s: %s" %(infile, flangs))
    except:
        pass

if len(sys.argv) != 4:
    print("Usage: detectlang.py <language> <input dir> <output dir>")
    sys.exit(1)

lang = sys.argv[1]
indir = sys.argv[2]
outdir = sys.argv[3]
os.makedirs(outdir, exist_ok=True)

with multiprocessing.Pool() as pool:
    pool.map(process_file, os.listdir(indir))
