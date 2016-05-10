#!/bin/python

def reduce_form(L):
	K=sorted(L)				# Sort
	D={}
	for i in xrange(len(K)):
		D[K[i]]=i			# Store reduced forms in dictionary ( i.e. keys as elements, values as indices )
	for i in xrange(len(L)):		
		L[i] = D[L[i]]			# Repace elements with their reduced forms
	return L 
