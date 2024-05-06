# network_section.py
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout
import pyqtgraph as pg

class NetworkSection(QGroupBox):
    def __init__(self):
        super().__init__("Network Usage")
        layout = QVBoxLayout()
        self.network_plot = pg.PlotWidget(title="Network Traffic (KB/s)")
        self.network_plot.setYRange(0, 100)  # Adjust as necessary
        self.network_curve = self.network_plot.plot(pen=pg.mkPen('m', width=2))
        self.network_data = [0] * 60  # Last 60 seconds for Network traffic
        layout.addWidget(self.network_plot)
        self.setLayout(layout)

    def update_network(self, data):
        """Update the Network graph data."""
        self.network_curve.setData(data)
