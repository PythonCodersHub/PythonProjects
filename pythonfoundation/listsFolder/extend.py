alfa = [1, 2, 3]
beta = ["A", "B", "C"]
print("before extension 11 is :", alfa)
print("before extension 12 is :", beta)
beta.extend(alfa)
print("after extension 11 is :", alfa)
print("before extension 12 is :", beta)

a = ["cars", "bikes"]
b =["ships", "jets"]
b.extend(a)
print(a)
print(b)
#extend

march_txns = [100, 200, 300, 600, 800, 1200]
sept_txns = [100, 200, 300, 600, 800, 12000]
print("March taxations are ", march_txns)
print("Sept taxations are", sept_txns)
sept_txns.extend(march_txns)
print("sept and march taxtions are",  sum(sept_txns))
