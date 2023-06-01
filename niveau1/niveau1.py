from stegano import lsb

# fonction pour encrypter le message
def caesar_encrypt(real_text, shift):
    encrypted_text = [chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() 
                      else chr((ord(char) - 97 + shift) % 26 + 97) if char.islower() 
                      else char for char in real_text]
    return ''.join(encrypted_text)

# Function pour cacher un message pas une photo
def create_stegano_image(input_image, hidden_message, output_image):
    secret = lsb.hide(input_image, hidden_message)
    secret.save(output_image)

# Message pour la recru
message = "Bonjour, recrue. Votre premiere tache commence ici. Trouvez les informations cachees dans l'image nommee clue.png dans ce meme repertoire."
# Shift for Caesar cipher
shift = 3
# Encrypter le message
encrypted = caesar_encrypt(message, shift)

# ecrire le message dans un fichier
with open('ciphertext.txt', 'w') as f:
    f.write(''.join(encrypted))

# Messagh a etre integre a l'image
hidden_message = "01253{CIA_felicite_vos_efforts._La_prochaine_mission_vous_attend_dans_le_trafic_reseau.}"
# Creer l'image
create_stegano_image("input_image.png", hidden_message, "clue.png")

