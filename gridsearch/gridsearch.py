#!/bin/python

import sys
from collections import OrderedDict

def find_string_indeces(find_string, search_string):
  find_len = len(find_string)
  search_len = len(search_string)

  start_indeces = []
  for i in range(search_len - find_len + 1):
    if search_string[i: i + find_len] == find_string:
      start_indeces.append(i)

  return start_indeces

t = int(raw_input().strip())
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in xrange(R):
        G_t = str(raw_input().strip())
        G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in xrange(r):
        P_t = str(raw_input().strip())
        P.append(P_t)

    print 'G'
    print G
    print 'P'
    print P

    match_dict = OrderedDict()
    for g_i, g in enumerate(G):
      for p_i, p in enumerate(P):
        match_dict[(g_i, p_i)] = find_string_indeces(p, g)
        # match_dict[search_row, find_row] : char_index

    # print match_dict
    for key in match_dict:
      if len(match_dict[key]) == 0:
        del match_dict[key]
        
    rows = set()
    input_rows = set()

    target_len = len(p)
    print 'target_len'
    print target_len

    row_counter = {}
    for key in match_dict:
      rows.add(key[0])
      input_rows.add(key[1])

      if match_dict[key]

      

print find_string_indeces('def', 'abcdefghijk')
print find_string_indeces('def', 'abcdefghijkdef')
print match_dict
print rows
print input_rows