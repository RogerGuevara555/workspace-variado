import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # registra la proyección '3d'

# --- Parámetros del modelo ---
filos = {
    "Rojo":     0.50,
    "Naranja":  0.75,
    "Amarillo": 1.00,
    "Verde":    1.125,
    "Azul":     1.25,
    "Blanco":   1.30,
    "Púrpura":  1.50,
}
F_list = np.array(list(filos.values()))

# --- Malla 3D de (R, A, F) ---
R_vals = np.linspace(100, 500, 25)
A_vals = np.linspace(-0.30, 1.00, 25)

R_grid, A_grid, F_grid = np.meshgrid(R_vals, A_vals, F_list)
R_flat = R_grid.ravel()
A_flat = A_grid.ravel()
F_flat = F_grid.ravel()

# --- Daño esperado (4ª dimensión, codificada por color) ---
D_flat = R_flat * F_flat * (1 + 0.25 * A_flat)

# --- Scatter 4D ---
fig = plt.figure(figsize=(13, 9))
ax = fig.add_subplot(111, projection="3d")

sc = ax.scatter(
    R_flat,
    A_flat * 100,     # afinidad en %
    F_flat,           # filo como multiplicador
    c=D_flat,         # 4ª dimensión = color
    cmap="plasma",
    s=12,
    alpha=0.85,
    depthshade=True,
)

ax.set_xlabel("Raw (R)")
ax.set_ylabel("Afinidad (%)")
ax.set_zlabel("Filo (F)")
ax.set_title("Daño esperado 4D: R, A, F en ejes  ·  color = D")
fig.colorbar(sc, ax=ax, label="Daño esperado (D)", shrink=0.7)

ax.view_init(elev=22, azim=-55)
plt.tight_layout()
plt.show()