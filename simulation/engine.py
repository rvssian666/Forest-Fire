import numpy as np
from scipy import ndimage
from collections import defaultdict

class ForestFireEngine:
    EMPTY, TREE, BURNING = 0, 1, 2

    def __init__(self, size, p, f, grid=None):
        self.size = size
        self.p = p
        self.f = f
        self.grid = np.array(grid, dtype=int) if grid is not None else np.zeros((size, size), dtype=int)
        # Aseguramos que sea un defaultdict de enteros
        self.fire_sizes = defaultdict(int)

    def _get_fire_clusters(self):
        """Identifica clusters de fuego conectados."""
        burning_mask = (self.grid == self.BURNING)
        if not np.any(burning_mask):
            return {}
        
        labeled, num_features = ndimage.label(burning_mask)
        sizes = defaultdict(int)
        
        for i in range(1, num_features + 1):
            # Convertimos explícitamente a int nativo de Python
            size = int(np.sum(labeled == i))
            sizes[size] += 1
        
        return sizes

    def step(self):
        fire_sizes = self._get_fire_clusters()
        # Usamos .get(size, 0) para que si la llave no existe, empiece en 0 y no explote
        for size, count in fire_sizes.items(): 
            self.fire_sizes[size] = self.fire_sizes.get(size, 0) + count
        
        new_grid = self.grid.copy()
        burning_mask = (self.grid == self.BURNING)
        tree_mask = (self.grid == self.TREE)
        empty_mask = (self.grid == self.EMPTY)

        # Regla 1: Crecimiento
        new_grid[empty_mask & (np.random.random(self.grid.shape) < self.p)] = self.TREE
        
        # Regla 2: Propagación
        has_burning_neighbor = np.zeros(self.grid.shape, dtype=bool)
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            shifted = np.roll(np.roll(burning_mask, dx, axis=0), dy, axis=1)
            has_burning_neighbor |= shifted
        
        new_grid[tree_mask & has_burning_neighbor] = self.BURNING

        # Regla 3: Rayos
        lightning = (tree_mask & ~has_burning_neighbor & (np.random.random(self.grid.shape) < self.f))
        new_grid[lightning] = self.BURNING

        # Regla 4: Extinción (El fuego se convierte en vacío)
        new_grid[burning_mask] = self.EMPTY

        self.grid = new_grid