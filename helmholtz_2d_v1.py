"""
Discrétisation de l'équation de Helmholtz 2D
Auteur: Kamel STIFAN
Date: 2024-11-24
"""

import numpy as np
import matplotlib.pyplot as plt

# Paramètres du domaine
nx, ny = 50, 50  # Nombre de points
Lx, Ly = 1.0, 1.0  # Dimensions

# Création du maillage
x = np.linspace(0, Lx, nx)
y = np.linspace(0, Ly, ny)
X, Y = np.meshgrid(x, y)

print("Maillage créé avec succès")
print(f"Dimensions: {nx}x{ny}")
Commit message: Initial commit - Structure du code
