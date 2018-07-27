import itertools
def permu(word):
    a = list(itertools.permutations(word))
    q = ""
    q += "Total Permtaion Possible : "+str(len(a))+"\n"
    for i in a:
        q += "\n"+str(i)
    return q
