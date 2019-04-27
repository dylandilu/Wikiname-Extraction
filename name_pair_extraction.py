# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import argparse
import os
def gaz_mine(il,dir_out,database):
    f_out=open(os.path.join(dir_out,'name_pair_%s_typing.txt'%il),'w')
    f=open(database)
    for oneline in f:
        if oneline.strip().split('\t')[0]==il:
            f_out.write('%s\t%s\t%s\n'%(oneline.strip().split('\t')[3],oneline.strip().split('\t')[4],oneline.strip().split('\t')[2]))
    f_out.close()
    f.close()



if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Extracting bi-lingual lexicion from Panlex')
    parser.add_argument('--target_language', default='zho', help='identify the 3-digit language code for target language')
    parser.add_argument('--output_dir', default='data/lexicons/', help='identify the path of the folder to save the extracted lexicon')
    parser.add_argument('--database', default='data/all-data.uniq', help='path of processed sqlite database of panlex')
    args = parser.parse_args()

    gaz_mine(args.target_language, args.output_dir, args.database)
