t1=0.7
t2=0.4
t3=0.2 
pj=100 
ass=0.3
TVA=0.18
nbr_t_km = float(input("entrez le nombre total dekilometres :"))
nbr_jours = int(input("entrez le nombre de jours de location:"))
cout_km=0
if nbr_t_km <= 100:
    cout_km = nbr_t_km * t1
elif 100 < nbr_t_km <= 1000:
    cout_km = 100 * t1 + (nbr_t_km - 100) * t2
else:
    cout_km = 100 * t1 + 900 * t2 + (nbr_t_km - 1000) * t3
