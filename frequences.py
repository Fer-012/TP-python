from re import T
from unittest import result


def frequences(s):
    print(s.split())
    mots = s.split()
    # La méthode split() de Python est utilisée pour diviser une chaîne en une liste de caractères
    freq = {}
    for mot in mots:
        if mot in freq:
            freq[mot] += 1
        else:
            freq[mot] = 1
    return freq

def trier_par_frequence(s):
    l=s.split()
    e=set(l)
    lres=[]
    for mot in  e:
        lres.append((mot,l.count(mot)))
        lres.sort(reverse=True,key=lambda x :x[1])
    return lres

def plus_frequents(s):
    freq_list = trier_par_frequence(s)
    max_frequets = freq_list[0][1]
    result= [freq_list[0][0]]
    for i in  range(1,len(freq_list)):
        if freq_list[i][1] < max_frequets:
            break
        result.append(freq_list[i][0])
    return result



phrase = 'do re do mi do la la mi la do la'
print(frequences(phrase))
print(trier_par_frequence(phrase))
print(plus_frequents(phrase))