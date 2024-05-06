# cpu_section.py
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout
import pyqtgraph as pg

class CPUSection(QGroupBox):
    def __init__(self):
        super().__init__("CPU Usage")
        layout = QVBoxLayout()
        self.cpu_plot = pg.PlotWidget(title="CPU Usage (%)")
        self.cpu_plot.setYRange(0, 100)
        self.cpu_curve = self.cpu_plot.plot(pen=pg.mkPen('y', width=2))
        self.cpu_data = [0] * 60  # Last 60 seconds for CPU usage
        layout.addWidget(self.cpu_plot)
        self.setLayout(layout)

    def update_cpu(self, data):
        """Update the CPU graph data."""
        self.cpu_curve.setData(data)
