# disk_section.py
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout
import pyqtgraph as pg

class DiskSection(QGroupBox):
    def __init__(self):
        super().__init__("Disk Usage")
        layout = QVBoxLayout()
        self.disk_plot = pg.PlotWidget(title="Disk Usage (%)")
        self.disk_plot.setYRange(0, 100)
        self.disk_curve = self.disk_plot.plot(pen=pg.mkPen('g', width=2))
        self.disk_data = [0] * 60  # Last 60 seconds for Disk usage
        layout.addWidget(self.disk_plot)
        self.setLayout(layout)

    def update_disk(self, data):
        """Update the Disk graph data."""
        self.disk_curve.setData(data)
