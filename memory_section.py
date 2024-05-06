# memory_section.py
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout
import pyqtgraph as pg

class MemorySection(QGroupBox):
    def __init__(self):
        super().__init__("Memory Usage")
        layout = QVBoxLayout()
        self.memory_plot = pg.PlotWidget(title="Memory Usage (%)")
        self.memory_plot.setYRange(0, 100)
        self.memory_curve = self.memory_plot.plot(pen=pg.mkPen('b', width=2))
        self.memory_data = [0] * 60  # Last 60 seconds for memory usage
        layout.addWidget(self.memory_plot)
        self.setLayout(layout)

    def update_memory(self, data):
        """Update the Memory graph data."""
        self.memory_curve.setData(data)
