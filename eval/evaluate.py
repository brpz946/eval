from textstat.textstat import textstat as ts
from tqdm import tqdm
import numpy as np

def print_summary(sent_iter1, sent_iter2):
    sent_iter1 = list(sent_iter1)
    sent_iter2 = list(sent_iter2)
    assert len(sent_iter1) == len(sent_iter2)
    metrics = {}
    name_fns = (("Flesch Reading Ease", ts.flesch_reading_ease), ("Gunning Fog", ts.smog_index), 
        ("Automated R Index", ts.automated_readability_index))
    for s1, s2 in tqdm(zip(sent_iter1, sent_iter2), total=len(sent_iter1)):
        for name, fn in name_fns:
            s1_val = fn(s1); s2_val = fn(s2)
            try:
                metrics[name][0].append(s1_val)
                metrics[name][1].append(s2_val)
            except KeyError:
                metrics[name] = [[s1_val], [s2_val]]

    for name, metric in metrics.items():
        avg_val1 = np.mean(metric[0])
        avg_val2 = np.mean(metric[1])
        print("Average value for {:<20} {:<10} {:<10}".format(name, round(avg_val1, 4), round(avg_val2, 4)))
    for name, metric in metrics.items():
        avg_reduce = np.mean(np.array(metric[0]) - np.array(metric[1]))
        print("Average change for {:<20} {}".format(name, round(avg_reduce, 4)))
