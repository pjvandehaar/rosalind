#!/usr/bin/env python3

# TODO: Sometimes the correct solution has blanks in all 4 lines.
# Use dynamic programming to solve this.

# Get best const-length alignment for first w,x,y,z bases of each seq.
# Could we work greedily from this sum?
# ie, find the w,x,y,z that generates the highest score with a sum of 2.
# Now try the four different extensions to that.  Take the best one.
# Will that fall into nasty traps?  Like just extending the two that perfectly match too long?
# I think so.



import sys
import itertools

seqs = [line.strip() for line in sys.stdin.readlines() if not line.startswith('>')]
assert all(base in 'ATCG' for seq in seqs for base in seq)

def score(alignment):
    return sum(score_pair(a,b) for a,b in itertools.combinations(alignment, 2))
def score_pair(a, b):
    return -sum(a != b for a,b in zip(a,b))
assert score([
    'ATAT-CCG',
    '-T---CCG',
    'ATGTACTG',
    'ATGT-CTG',
]) == -18


def get_buffered_seqs(seq, length):
    skip_point_sets = itertools.combinations(range(length), length - len(seq))
    for skip_point_set in skip_point_sets:
        tmp = seq
        for skip_point in skip_point_set:
            tmp = tmp[:skip_point] + '-' + tmp[skip_point:]
        yield tmp
assert 15 == len(list(get_buffered_seqs('ASDF', 6)))

def get_max_elem_and_val(it, key =lambda x:x):
    max_elem = next(it)
    max_val = key(max_elem)
    for elem in it:
        val = key(elem)
        if val >= max_val: # Maybe?
            max_elem, max_val = elem, val
    return (max_elem, max_val)

max_seq_len = max(len(seq) for seq in seqs)+1

# Get all ways of buffering each seq out
buffered_seqs = [list(get_buffered_seqs(seq, max_seq_len)) for seq in seqs]

for buffered_seq in buffered_seqs:
    print(buffered_seq)
    print(len(buffered_seq))
    assert len(set(buffered_seq)) == len(buffered_seq)
    print('')

# Then use itertools.product(*somelists)
best_alignment, best_score = get_max_elem_and_val(itertools.product(*buffered_seqs), key=score)
print(best_score)
print('\n'.join(best_alignment))

print('')
for line in best_alignment:
    print(' '.join(line))
