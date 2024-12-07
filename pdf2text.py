import PyPDF2
import pdfplumber
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os

def extract_text_from_pdf(pdf_path):
    try:
        # Essayer d'utiliser PyPDF2 pour extraire le texte
        text = ""
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                if page.extract_text():
                    text += page.extract_text() + "\n"
                else:
                    text += "[Texte non disponible sur cette page]\n"
        
        # Si PyPDF2 ne peut pas extraire correctement le texte, utiliser pdfplumber
        if "[Texte non disponible sur cette page]" in text or not text.strip():
            text = ""
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
                    else:
                        text += "[Texte non disponible sur cette page]\n"

        # Si pdfplumber ne peut toujours pas extraire le texte, utiliser OCR avec pytesseract
        if "[Texte non disponible sur cette page]" in text or not text.strip():
            text = ""
            # Convertir le PDF en images, une image par page
            images = convert_from_path(pdf_path)
            for i, image in enumerate(images):
                # Utiliser pytesseract pour extraire le texte de chaque image
                page_text = pytesseract.image_to_string(image, lang='fra')
                if page_text.strip():
                    text += page_text + "\n"
                else:
                    text += f"[Texte non disponible sur la page {i + 1}]\n"
        
        return text
    except Exception as e:
        return f"Une erreur s'est produite : {e}"

# Demande à l'utilisateur le chemin vers son fichier PDF
pdf_path = input("Entrez le chemin vers votre fichier PDF : ")
texte_extrait = extract_text_from_pdf(pdf_path)

# Affiche le texte extrait
print(texte_extrait)

# Si tu veux sauvegarder le texte dans un fichier texte :
sauvegarder = input("Voulez-vous sauvegarder le texte extrait dans un fichier texte ? (oui/non) : ").strip().lower()
if sauvegarder == 'oui':
    try:
        fichier_sortie = input("Entrez le nom du fichier de sortie (par exemple 'texte_extrait.txt') : ")
        with open(fichier_sortie, 'w', encoding='utf-8') as text_file:
            text_file.write(texte_extrait)
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier texte : {e}")
