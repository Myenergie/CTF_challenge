#!/bin/bash

NUMERO_ETUDIANT="2211233"
SCRIPT_DIRECTORY="/path/to/your/script/files"

# Identifier la lettre de disque la plus haute utilisée
high_letter=$(ls /dev/sd* | tail -1)
high_letter=${high_letter:7:1}

# Lister chaque clé USB
for letter in {c..z}; do
  if [ "$letter" \> "$high_letter" ]; then
    continue
  fi
  disk="/dev/sd${letter}1"

  # Créer un répertoire pour chaque clé
  mnt_dir="/mnt/sd${letter}1"
  mkdir -p "$mnt_dir"
  
  # Monter chaque clé dans le bon répertoire
  mount "$disk" "$mnt_dir"
  
  # Pour chaque clé, créer un sous-répertoire
  sub_dir="${mnt_dir}/${NUMERO_ETUDIANT}"
  mkdir -p "$sub_dir"
  
  # Pour chaque clé, copier vos fichiers .sh dans le sous-répertoire
  cp -v "${SCRIPT_DIRECTORY}/*.sh" "$sub_dir"
  
  # Démonter chaque clé
  umount -v "$disk"
done
