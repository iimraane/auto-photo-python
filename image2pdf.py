from PIL import Image
import os

def images_to_pdf(image_folder, output_pdf_path):
    # Vérifier que le fichier de sortie a l'extension .pdf
    if not output_pdf_path.lower().endswith('.pdf'):
        output_pdf_path += '.pdf'

    # Récupérer la liste des fichiers dans le dossier spécifié
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff'))]
    
    if not image_files:
        print("Aucune image trouvée dans le dossier spécifié.")
        return

    # Trier les fichiers par nom (facultatif, utile si les images doivent être dans un ordre particulier)
    image_files.sort()

    # Créer une liste d'objets Image
    images = []
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        image = Image.open(image_path).convert('RGB')
        images.append(image)

    # Sauvegarder la première image et ajouter les autres dans le PDF
    if images:
        images[0].save(output_pdf_path, save_all=True, append_images=images[1:])
        print(f"PDF créé avec succès : {output_pdf_path}")
    else:
        print("Aucune image valide à ajouter au PDF.")

# Fonction principale pour rendre l'utilisation plus conviviale
def main():
    # Demander à l'utilisateur d'entrer le chemin du dossier d'images
    dossier_images = input("Veuillez entrer le chemin vers votre dossier contenant les images : ").strip()
    
    # Vérifier si le dossier existe
    if not os.path.isdir(dossier_images):
        print("Le dossier spécifié n'existe pas. Veuillez réessayer.")
        return

    # Demander à l'utilisateur d'entrer le chemin de sortie du fichier PDF
    fichier_pdf_sortie = input("Veuillez entrer le chemin de sortie pour le fichier PDF (incluez le nom du fichier, ex : sortie.pdf) : ").strip()
    
    # Générer le PDF à partir des images
    images_to_pdf(dossier_images, fichier_pdf_sortie)

if __name__ == "__main__":
    main()