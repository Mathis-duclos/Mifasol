# 🎶 Mifasol - Downloadeur d'OST

Mifasol est une application permettant de télécharger des OST depuis le site [KHInsider](https://downloads.khinsider.com/). Fini la corvée de télécharger les pistes une par une ! ^^

## ✨ Fonctionnalités

* **Toute l'OST en un téléchargement :** Collez simplement l'URL de l'album, Mifasol s'occupe du reste.
* **Organisation auto :** Crée un dossier portant le nom exact du jeu directement dans le dossier Téléchargements.
* **Multiplateforme :** Fonctionne nativement sur macOS et Windows. (Théoriquement utilisable sur Linux avec Python)
* **Respectueux des serveurs :** Pause de 2 secondes entre chaque musique pour ne pas surcharger les serveurs et éviter le bannissement d'IP.

## 🚀 Installation

### 🍏 Sur macOS
1. Téléchargez `Mifasol.app.zip` et dézippez-le.
2. Glissez `Mifasol.app` dans le dossier *Applications*.

*Lors du premier lancement, macOS bloquera l'application car elle provient d'un développeur non identifié. Faites un **Clic droit > Ouvrir** sur l'application, puis cliquez sur "Ouvrir" dans la boîte de dialogue. Ou allez dans Réglages Système > Confidentialité et sécurité. Cherchez Mifasol et cliquez sur "Ouvrir quand même".*

### 🪟 Sur Windows
1. Téléchargez le fichier `Mifasol.exe`.
2. Placez-le où vous le souhaitez (mais triez vos applis svp) et double-cliquez dessus pour le lancer. 

*Si Windows Defender affiche un avertissement, cliquez sur "Informations complémentaires" puis sur "Exécuter quand même".*

## 🛠️ Compiler le code

Si vous souhaitez modifier le code ou compiler l'application vous-même, voici la marche à suivre. 

### Prérequis
* Python 3.12 ou supérieur installé sur votre machine.

### 1. Cloner le projet et préparer l'environnement
```bash
git clone https://github.com/mathis-duclos/Mifasol.git
cd Mifasol

# Création de l'environnement virtuel
python3 -m venv env   # Sur Mac
py -m venv env        # Sur Windows

# Activation
source env/bin/activate        # Sur Mac
.\env\Scripts\activate         # Sur Windows

# Installation des dépendances
pip install requests beautifulsoup4 customtkinter pyinstaller
```

## ℹ️ Informations et compatibilité
### 🍎 macOS

Mifasol a été testé sur :

* macOS Tahoe 26.3.1 (a) (25D771280a) sur MacBook Pro M3 Pro
* macOS Tahoe bêta 26.4 (25E5233c) sur Mac Mini M4
* macOS Tahoe 26.0.1 (25A362) sur MacBook Air M4

*Je n'ai pas pu le tester sur des versions antérieures de macOS ou des Mac Intel et ne suis donc pas capable d'affirmer s'il fonctionne correctement dessus.*

### 🪟 Windows

Mifasol a été testé sur :

* Windows 11 Famille 24H2 (VM)
* Windows 10 Famille 22H2 (AMD)

*Je n'ai pas pu le tester sur des versions antérieures de Windows et ne suis donc pas capable d'affirmer s'il fonctionne correctement dessus.*

## ⚠️ Avertissement
Ce script est fourni à des fins éducatives et de confort personnel. Veuillez respecter les conditions d'utilisation du site KHInsider. Ne retirez pas les délais (sleep) dans le code pour télécharger le site de manière agressive, au risque de voir votre adresse IP définitivement bloquée.
