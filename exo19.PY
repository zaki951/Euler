"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def jourSuivant(jour1 , mois , bissextile):
    jours = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
    if mois == "fevrier":
        if bissextile :
            nb = 29 - 4 * 7
        else :
            nb = 28 - 4 * 7
    elif mois in ["septembre","avril", "juin" , "novembre"] :
        nb = 30 - 4 * 7
    else :
        nb = 31 - 4 * 7
    taille = len(jours)
    if nb + jour1 < taille :
        return jours[nb + jour1]
    else :
        return jours[nb + jour1 - 7]


def main():
    cpt = 0
    jours = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
    moisListe = ["janvier","fevrier","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre"]
    jour = "mercredi" #
    for i in range(1901, 2001):
        for mois in moisListe :
            if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
                jour = jourSuivant(jours.index(jour), mois,True)
            else :
                jour = jourSuivant(jours.index(jour), mois,False)

            if jour == "dimanche":
                cpt += 1
    print(cpt)
if __name__ == '__main__':
    main()
    
