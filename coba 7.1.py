d = {"Segitiga" : "L = 0.5*a*t",
     "Persegi" : "L = s**2",
     "PersegiPanjang" : "L = p*l",
     "Lingkaran" : "L = pi*r**2",
     "JajarGenjang" : "L = a*t"}



print ( """

        No |  Nama Bangun   |   Rumus
        ---|----------------|-----------------
        1  | Segitiga       | %s
        2  | Persegi        | %s
        3  | PersegiPanjang | %s
        4  | Lingkaran      | %s
        5  | JajarGenjang   | %s


    """%(d['Segitiga'], d['Persegi'], d['PersegiPanjang'], d['Lingkaran'], d['JajarGenjang'])
        )
