def disponibilite(prod, prix):
    return prod in prix
    # if prod in prix:
    #     return True
    # else:
    #     return False
    
def prix_moyen(prix):
    if len(prix) != 0: 
        print(prix.items())
        print(prix.values())
        return sum(prix.values()) / len(prix)
        
        # dict_values([229.0, 127.3, 74.5, 184.6])
    
def fourchette_prix(prix):
    produits=[]
    max_produit =prix[0][0]
    min_prodduit=prix[0][0]
    for i in  prix.items():
        if prix[i][1]>max_produit: 
            max_produit=prix[i][1]
        if prix[i][0]<min_prodduit:
            min_prodduit=min_prodduit
    
        
        

base_prix = {"produit 1": 229.0,"produit 2": 127.30,"produit 3": 74.50,"produit 4": 184.60}
prod = "produit 1"
# prod= input(print("entrez vote produit"))
print(disponibilite(prod, base_prix))
print(prix_moyen(base_prix))
print(fourchette_prix(base_prix))