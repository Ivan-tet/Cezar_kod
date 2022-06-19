from cezar import szyfrowania, deszyfrowania


liczba = [83,97,22,55,53,12,8,57,1,60,62,74,40,26,45,86,49,89,25,69,61,48,87,95,23,78,35,47,37,85,96,32,7,10,90,43,67,27,3,91,84,31,5,50,82,71,68,4,92,38,41,11,65,17,99,24,88,9,76,59,21,66,93,70,15,30,29,98,20,64,33,14,51,13,58,18,16,19,28,75,56,72,54,6,77,46,100,34,80,52,73,81,94,42,79,36,2,63,39,44]
litery= ['m','l','k','o','p','i','u','t','y','r','e','r','g','d','b','c','n','f','h','r','n','d','j','c','n','d','s','a','q','w','e','r','t','u','f','j','g','h','p','r','h','d','y','f','b','c','n','f','m','e','s','k','a','z','o','e','p','r','l','f','j','c','b','d','n','j','r','l','q','z','a','q','w','s','x','e','d','c','r','f','v','t','g','b','y','h','n','u','j','m','i','k','o','l','p','x','z','a','s','d']
def test_szyfrowania_5(benchmark):
    benchmark.pedantic(szyfrowania, args=[['s','e','f','g','t'],[1,2,3,4,5]], rounds=20)

def test_deszyfrowania_5(benchmark):
     benchmark.pedantic(deszyfrowania, args=[['s','e','f','g','t'],[1,2,3,4,5]], rounds=20)

def test_szyfrowania_10(benchmark):
    benchmark.pedantic(szyfrowania, args=[['q','w','e','r','t','y','u','i','o','p'], [2,3,4,5,6,7,8,9,1,0]], rounds=20)

def test_deszyfrowania_10(benchmark):
    benchmark.pedantic(deszyfrowania, args=[['q','w','e','r','t','y','u','i','o','p'], [2,3,4,5,6,7,8,9,1,0]], rounds=20)

def test_szyfrowania_100(benchmark):
    benchmark.pedantic(szyfrowania, args=[litery,liczba], rounds=20)

def test_deszyfrowania_100(benchmark):
    benchmark.pedantic(deszyfrowania, args=[litery,[liczba]], rounds=20)



