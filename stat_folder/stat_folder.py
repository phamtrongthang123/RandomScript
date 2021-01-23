from pathlib import Path
from tabulate import tabulate
import os
import argparse
parser = argparse.ArgumentParser(description='Only one argument is folder name!')
parser.add_argument('-f','--folder', metavar='f', type=str,help='folder name')
parser.add_argument('-d', '--depth',default=1, type=int,help='depth recurrent')
args = parser.parse_args()

folder_name = Path(args.folder)
max_depth = args.depth
class colors: 
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg: 
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg: 
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size

def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.2f%s%s" % (num, 'Yi', suffix)

def size_with_color(s):
    return colors.bold + colors.fg.orange + s + colors.reset

def folder_with_color(f):
    return colors.bold + colors.fg.blue + f + colors.reset

def make_bold(s):
    return colors.bold + s + colors.reset
print(make_bold("Folder size: "),size_with_color(sizeof_fmt(get_size(folder_name))))

def listing_folder(folder_name, cur_depth):
    print("")
    print(make_bold("Child list of"), folder_with_color(str(folder_name)))
    t = []
    all_cur = [x for x in folder_name.iterdir()]
    for f in all_cur:    
        if f.is_dir():
            child_folder_s_file = [x for x in f.iterdir()]
            number_of_file = len(child_folder_s_file)
            size_c = size_with_color(sizeof_fmt(get_size(f)))
            t.append([folder_with_color(str(f)),'folder', size_c, number_of_file])
        else:
            t.append([f,'file', size_with_color(sizeof_fmt(get_size(f)))])
    t.sort(key=lambda x: x[1], reverse=True)
    print(tabulate(t, headers=[make_bold(x) for x in ['Name','Type', 'Size', 'Number of file (for folder)']]))
    # count from 1
    next_depth = cur_depth + 1
    if next_depth > max_depth:
        return 
    else:
        for f in all_cur:
            if f.is_dir():
                listing_folder(f, next_depth)

    
listing_folder(folder_name, 1)