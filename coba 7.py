d = {"segitiga" : "L = 0.5*a*t",
     "persegi" : "L = s**2",
     "persegiPanjang" : "L = p*l"
     "lingkaran" : "L = pi*r**2",
     "jajarGenjang" : "L = a*t"}

print ("""

    No | Nama Bangun    | Rumus
    ---|----------------|----------------
    1  | segitiga       | %s
    2  | persegi        | %s
    3  | persegiPanjang | %s
    4  | lingkaran      | %s
    5  | jajarGenjang   | %s

"""%(d['segitiga'], d['persegi'], d['persegiPanjang'], d['lingkaran'], d['jajarGenjang']))
