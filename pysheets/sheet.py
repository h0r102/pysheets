import tkinter as tk
from tkinter import ttk

import numpy as np


class _Sheet(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super(_Sheet, self).__init__(*args, **kwargs)

    def init_sheet(self, n_rows, n_columns):
        self._cell_array = np.tile(_Cell(), (n_rows, n_columns))

    def get_num_rows(self):
        return self._cell_array.shape[0]

    def get_num_columns(self):
        return self._cell_array.shape[1]

    def input_to(self, row, column, value):
        self._cell_array[row, column].value = value


DEFAULT_CELL_WIDTH = 8.0
DEFAULT_CELL_HEIGHT = 4.0


class _Cell(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super(_Cell, self).__init__(*args, **kwargs)

        self.width = DEFAULT_CELL_WIDTH
        self.height = DEFAULT_CELL_HEIGHT
        self.value = ""
