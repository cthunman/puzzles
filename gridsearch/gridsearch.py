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

  # print 'G'
  # for row in G:
  #   print row
  # print 'P'
  # for row in P:
  #   print row

  match_dict = OrderedDict()
  index_dict = OrderedDict()
  for g_i, g in enumerate(G):
    for p_i, p in enumerate(P):
      match_dict[(g_i, p_i)] = find_string_indeces(p, g)
      for i in find_string_indeces(p, g):
        if i not in index_dict:
          index_dict[i] = []
        index_dict[i].append((g_i, p_i))

  target_len = len(P)
  is_matched = False
  counter = 0
  last_row_index = -1
  for i in index_dict:
    for v in index_dict[i]:
      if v[1] == 0:
        last_row_index = v[0]
        counter = 1
      elif v[1] == counter:
        if last_row_index == v[0] - 1: 
          last_row_index = v[0] 
          counter = counter + 1
          if counter == target_len - 1:
            is_matched = True
      else:
        counter = 0

  if is_matched:
    print 'YES'
  else:
    print 'NO'
