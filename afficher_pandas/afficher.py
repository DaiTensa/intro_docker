import pandas as pd




# demander 4 élément
menu = """
Veuillez entrez un élément
"""

count_element = 0
liste_element = []

while count_element < 4:
    user_choice = input(menu)
    liste_element.append(user_choice)
    count_element += 1

print("Voici la liste de course")
df = pd.DataFrame(liste_element, columns=['Numbers'])
print(df)
print(type(df))