
N,l = map(int,raw_input().split())
 
countries = []
for i in xrange(l):
    a,b = map(int,raw_input().split())
    #print a, b
    ppl  = set()
    ppl.add(a)
    ppl.add(b)
    found = (False, set())
    for country in countries:
        if (not found[0]) and len(country.intersection(ppl)) > 0:
            country.update(ppl)
            found = (True, country)
        elif found[0] and len(country.intersection(ppl)) > 0:
            found[1].update(country)
            countries.remove(country)
    if not found[0]:
        countries.append(ppl)

result = long(1)
result *= N 
result *= (N-1)
result /= 2

for country in countries:
    m = len(country)
    result -= (m * (m-1)/2)
    #print result
    
print result

