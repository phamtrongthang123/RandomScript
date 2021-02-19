import argparse

parser = argparse.ArgumentParser(description='description!')
parser.add_argument('-f','--folder', metavar='f', type=str,help='folder name')
args = parser.parse_args()