d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]} #print "HELLO"
a = d['k1'][2]['k2'][1]['tough'][2][0]
print(a.upper())