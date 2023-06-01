#!/bin/bash

# Initialise les variables
nombres=()
produit=1

# Lit les nombres
while true; do
  echo "Entrez un nombre (0 pour arrêter):"
  read nombre
  # Vérifie si le nombre est 0
  if (( nombre == 0 )); then
    break
  fi
  # Ajoute le nombre à la liste
  nombres+=($nombre)
  # Multiplie le produit par le nombre
  produit=$((produit * nombre))
done

# Affiche les nombres
echo "Nombres saisis: ${nombres[@]}"

# Affiche le produit
echo "Produit: $produit"