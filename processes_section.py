# processes_section.py
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout
import pyqtgraph as pg

class ProcessesSection(QGroupBox):
    def __init__(self):
        super().__init__("Process Count")
        layout = QVBoxLayout()
        self.process_plot = pg.PlotWidget(title="Process Count")
        self.process_plot.setYRange(0, 200)  # Adjust as per your system's average process count
        self.process_curve = self.process_plot.plot(pen=pg.mkPen('r', width=2))
        self.process_data = [0] * 60  # Last 60 seconds for process count
        layout.addWidget(self.process_plot)
        self.setLayout(layout)

    def update_processes(self, data):
        """Update the Processes graph data."""
        self.process_curve.setData(data)
