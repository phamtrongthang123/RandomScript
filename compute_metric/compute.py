import argparse

parser = argparse.ArgumentParser(description='description!')
parser.add_argument('-p','--precision', metavar='<precision value>', type=float,help='precision value')
parser.add_argument('-r','--recall', metavar='<recall value>', type=float,help='recall value')
parser.add_argument('-tp','--true_positive', metavar='<true positive value>', type=float,help='true positive value')
parser.add_argument('-fp','--false_positive', metavar='<false positive value>', type=float,help='false positive value')
parser.add_argument('-tn','--true_negative', metavar='<true negative value>', type=float,help='true negative value')
parser.add_argument('-fn','--false_negative', metavar='<false negative value>', type=float,help='false negative value')
args = parser.parse_args()

results ={'precision': None, 
'recall': None,
'f1_score': None,
}

print_results = {'precision': 'Precision: ', 
'recall': 'Recall: ',
'f1_score': 'F1-score: ',
}

if args.precision is not None:
    results['precision'] = args.precision

if args.recall is not None: 
    results['recall'] = args.recall
    
if args.true_positive is not None and args.false_positive is not None:
    results['precision'] = args.true_positive / (args.true_positive + args.false_positive)

if args.true_negative is not None and args.false_negative is not None:
    results['recall'] = args.true_negative / (args.true_negative + args.false_negative)

try:
    results['f1_score'] = 2*results['precision']*results['recall'] / (results['precision'] + results['recall'])
except:
    pass

for k,v in results.items():
    if v is not None:
        print(print_results[k], round(v,2))

