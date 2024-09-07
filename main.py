def card_checker():
    newc = [0] * 16
    c_number = input("Entrez un numéro de carte (\033[91m16 caractères.\033[0m): \n") # On impose 16 caractères et on met les caractères en rouge pr que l'user voit bien
    total = 0
    if len(c_number) < 16 or len(c_number) >16: # on vérifie au cas où
        return "Nombre de caractères \033[91mincorrect\033[0m."
    else:
        for i in range(len(c_number)):
            chiffre = int(c_number[i])
            if i% 2 != 0: #on opère seulement sur les chiffres impairs, commençant par 1 
                if chiffre *2 > 9: # si le double est > 9 alors on prend la somme de ses chiffres
                    double = str(chiffre *2)
                    newc[i] = int(double[0]) + int(double[1])
                    
                else:
                    newc[i] = chiffre * 2 # sinon on fait juste le double
            else:
                newc[i] = chiffre 

        for e in newc: # total sans utiliser .sum()
            total += e 

        if total % 10 == 0: # si le modulo finit par 0, donc divisible par 10, alors le numéro de carte est valide
            return f"La carte est valide, le total étant de \033[92m{total}\033[0m. (Formule de Luhn.)" # couleur verte si positif
        else:
            return f"La carte est invalide, le total étant de \033[91m{total}\033[0m. (Formule de Luhn.)" #couleur rouge sinon




print(card_checker())
