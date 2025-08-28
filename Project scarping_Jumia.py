import requests
from bs4 import BeautifulSoup
import csv

def scrape_function(recherche_name):
    product_data = []
    for i in range(1, 51):
        url = f"https://www.jumia.ma/catalog/?q={recherche_name}&page={i}#catalog-listing"
        headers = {
            "User-Agent": "Mzilla/5.0o (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            products = soup.find_all('article', {'class': 'prd _fb col c-prd'})
            
            for product in products:
                produit_name = product.find('h3', {'class': 'name'})
                if produit_name:
                    product_name = produit_name.text.strip()
                else:
                    product_name = "Nom non disponible"
                
                s_prix_en_dh = product.find('div', {'class': 'prc'})
                if s_prix_en_dh:
                    prix_en_dh = s_prix_en_dh.text.strip()
                else:
                    prix_en_dh = "Prix non disponible"
                link_element = product.find('a', href=True)
                if link_element and 'href' in link_element.attrs:
                    link = "https://www.jumia.ma" + link_element['href']
                else:
                    link = "Lien non disponible"
                product_data.append({
                    'name': product_name,
                    'price': prix_en_dh,
                    'link': link
                })
            colors = ["\033[1;31m", "\033[1;32m", "\033[1;33m", "\033[1;34m", "\033[1;35m", "\033[1;36m"]
            color = colors[i % len(colors)]
            percent = i * 2
            if percent not in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
                continue
            else:
                print(f'\r{color}🚀 Scraping from Page: {percent:>3}% [{"█" * (i-3)}{" " * (10 - i)}]\033[0m', end="", flush=True)
            #print(f'\r🚀 Scraping from Page: {i:>2} [{"#" * i}{" " * (50 - i)}]', end="", flush=True)
            
        else:
            print(f"Site not Working hh : {response.status_code}")
            return None
    return product_data
  
print("\n\033[1;35m✨ Début du scraping... Prêt à décoller ! 🚀\033[0m\n")

recherche_name = input('Entre le nom du produit que tu veux Scarper sur Jumia : ')
afficher_en_terminal= input('Afficher les donnees sur le terminal ? (Y/N) : ')
products = scrape_function(recherche_name)
    
with open(f'{recherche_name}_Jumia_Products.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Nom', 'Prix', 'Lien'])
        for product in products:
            writer.writerow([product['name'], product['price'], product['link']])

if afficher_en_terminal == 'Y' or afficher_en_terminal == 'y':
    for product in products:
        print('Produit:', product['name'])
        print('Prix:', product['price'])
        print('Lien:', product['link'])
        print('--'*50)
else:
    print('')
print(f"Les données ont été enregistrées dans le fichier {recherche_name}_Jumia_Products.csv .")

print("\n\n\033[1;32m✅ Scraping terminé avec succès ! Données prêtes à l'emploi. 🎉\033[0m\n")

