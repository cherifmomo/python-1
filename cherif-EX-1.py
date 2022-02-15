
n = int(input("Donnez le nombre de lignes entre 2 et 9: "))

"verification du nombre avant traitement"
while n < 2 or n > 9:
    print ("Ce nombre n'est pas entre 2 et 9.")
    n = int(input("Donnez le nombre de lignes entre 2 et 9: ")) 

"traitement des données"
for i in range(1,n+1):
         print(" "*(n-i)+(str(i)+" ")*i)
