from collections import defaultdict

# creo un file con dati
with open("vendite.txt", "w") as f:
    f.write("apple,10\npear,5\napple,3\nbanana,2\norange,7\norange,\n\npear,4\n")

# leggo il file
with open("vendite.txt") as f:
    raw = [line.strip().split(",") for line in f]

# tieni solo righe con 2 elementi
clean = [line for line in raw if len(line) == 2]

# tieni solo righe ben formate
data = [(p, q) for p, q in clean if p and q.isdigit()]
    
print(data)

# lista prodotti e quantità
prodotti = [p for p, _ in data]
quantita = [int(q) for _, q in data]

# conteggio con defaultdict
totali = defaultdict(int)
for p, q in data:
    totali[p] += int(q)

frequenze = {}
tot_q = sum(totali.values())

for p, q in totali.items():
    frequenze[p] = q / tot_q

'''# try/except esempio
try:
    prezzo = totali["kiwi"]
except KeyError:
    prezzo = None'''

totali = dict(sorted(totali.items(), key=lambda x: x[1], reverse=True))
frequenze = dict(sorted(frequenze.items(), key=lambda x: x[1], reverse=True))

print("-"*30)
print("## Totali vendite ##")
for p, _ in totali.items():
    print(f"{p}:   {totali[p]} ({frequenze[p]*100:.1f}%)")
    
print("-"*30)


print("Totali vendite:", totali)
print("Frequenze prodotti:", frequenze)
#print("Prezzo kiwi:", prezzo)
print("Media quantità:", sum(quantita) / len(quantita))
print("Top prodotto:", max(totali, key=totali.get))
