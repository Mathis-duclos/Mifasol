import tkinter as tk
from tkinter import scrolledtext
import requests
from bs4 import BeautifulSoup
import os
import urllib.parse
import threading
import time

def telecharger_ost():
    # Désactiver le bouton pendant le téléchargement
    btn_download.config(state=tk.DISABLED)
    url_principale = entry_url.get()
    
    if not url_principale.startswith("http"):
        log("Erreur : Veuillez entrer une URL valide.")
        btn_download.config(state=tk.NORMAL)
        return

    # Lancer le processus dans un Thread séparé pour ne pas figer la fenêtre
    thread = threading.Thread(target=processus_scraping, args=(url_principale,))
    thread.start()

def processus_scraping(url):
    try:
        log("Connexion au site...")
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
        reponse = requests.get(url, headers=headers)
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # Trouver le nom de l'album pour créer le dossier
        titre_h2 = soup.find('h2')
        nom_album = titre_h2.text.strip() if titre_h2 else "Nouvelle_OST"
        nom_dossier = "".join(c for c in nom_album if c.isalnum() or c in " -_").strip()
        
        chemin_telechargements = os.path.expanduser(f"~/Downloads/{nom_dossier}")
        os.makedirs(chemin_telechargements, exist_ok=True)
        log(f"Dossier créé : {nom_dossier}\n")

        # Trouver tous les liens de musique
        tableau = soup.find(id='songlist')
        liens = tableau.find_all('a') if tableau else []
        urls_musiques = []
        for lien in liens:
            href = lien.get('href')
            if href and '.mp3' in href and href not in urls_musiques:
                # Si le lien est relatif, on le complète
                if href.startswith('/'):
                    href = "https://downloads.khinsider.com" + href
                urls_musiques.append(href)

        if not urls_musiques:
            log("Aucune musique trouvée sur cette page.")
            btn_download.config(state=tk.NORMAL)
            return

        log(f"{len(urls_musiques)} pistes trouvées. Lancement du téléchargement...\n")

        # Boucle de téléchargement
        for i, url_piste in enumerate(urls_musiques):
            log(f"[{i+1}/{len(urls_musiques)}] Analyse de la piste...")
            
            # Aller sur la sous-page
            rep_piste = requests.get(url_piste, headers=headers)
            soup_piste = BeautifulSoup(rep_piste.text, 'html.parser')
            lecteur_audio = soup_piste.find('audio')
            
            if lecteur_audio and lecteur_audio.get('src'):
                vrai_lien = lecteur_audio.get('src')
                nom_fichier_brut = vrai_lien.split('/')[-1]
                nom_fichier_propre = urllib.parse.unquote(urllib.parse.unquote(nom_fichier_brut))
                
                chemin_complet = os.path.join(chemin_telechargements, nom_fichier_propre)
                
                log(f" -> Téléchargement : {nom_fichier_propre}")
                
                # Télécharger le fichier MP3
                donnees_mp3 = requests.get(vrai_lien, headers=headers)
                with open(chemin_complet, 'wb') as f:
                    f.write(donnees_mp3.content)
            else:
                log(" -> Lien introuvable pour cette piste.")
            
            # Pause de 2 secondes anti-ban
            time.sleep(2)

        log("\nTERMINÉ ! Toutes les musiques sont dans vos Téléchargements.")
    
    except Exception as e:
        log(f"\nUne erreur est survenue : {e}")
    
    finally:
        btn_download.config(state=tk.NORMAL)

def log(message):
    # Ajouter du texte dans la zone de log et faire défiler vers le bas
    text_log.insert(tk.END, message + "\n")
    text_log.see(tk.END)

# --- CRÉATION DE L'INTERFACE GRAPHIQUE ---
fenetre = tk.Tk()
fenetre.title("Mifasol")
fenetre.geometry("600x400")
fenetre.configure(padx=20, pady=20)

tk.Label(fenetre, text="Collez l'URL de l'album KHInsider ici :", font=("Arial", 14)).pack(anchor="w")

entry_url = tk.Entry(fenetre, width=60, font=("Arial", 12))
entry_url.pack(pady=10, fill="x")

btn_download = tk.Button(fenetre, text="⬇️ TÉLÉCHARGER", font=("Arial", 14, "bold"), command=telecharger_ost, bg="#4CAF50", fg="black")
btn_download.pack(pady=10)

text_log = scrolledtext.ScrolledText(fenetre, width=70, height=15, font=("Courier", 12), bg="black", fg="#00FF00")
text_log.pack(fill="both", expand=True)

# Lancer l'application
fenetre.mainloop()