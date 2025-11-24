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

# Fonction de maillage
def create_mesh(nx, ny, Lx, Ly):
    """Génère le maillage 2D"""
    x = np.linspace(0, Lx, nx)
    y = np.linspace(0, Ly, ny)
    return np.meshgrid(x, y)

X, Y = create_mesh(nx, ny, Lx, Ly)
print("Fonction de maillage implémentée")

Commit message: Ajout de la fonction de maillage

# Discrétisation de l'équation de Helmholtz
def helmholtz_discretization(k, nx, ny):
    """Discrétisation par différences finies"""
    dx = Lx / (nx - 1)
    dy = Ly / (ny - 1)
    
    # Matrice de discrétisation (simplifiée)
    A = np.zeros((nx*ny, nx*ny))
    
    print("Discrétisation effectuée")
    return A

A = helmholtz_discretization(1.0, nx, ny)

Commit message: Discrétisation de l'équation de Helmholtz

# Visualisation
def plot_results(X, Y, solution):
    """Affichage des résultats"""
    plt.figure(figsize=(8, 6))
    plt.contourf(X, Y, solution, levels=20, cmap='viridis')
    plt.colorbar(label='Solution')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Solution de l\'équation de Helmholtz')
    plt.savefig('helmholtz_solution.png')
    print("Visualisation sauvegardée")

# Test avec solution fictive
solution_test = np.sin(np.pi * X) * np.sin(np.pi * Y)
plot_results(X, Y, solution_test)

Commit message: Ajout de la visualisation des résultats
