# disk_section.py
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QLabel
import psutil
import pyqtgraph as pg

class DiskSection(QGroupBox):
    def __init__(self, show_detailed=True):
        super().__init__("Disk Usage")
        layout = QVBoxLayout()

        # Disk Usage graph
        self.disk_plot = pg.PlotWidget(title="Disk Usage (%)")
        self.disk_plot.setYRange(0, 100)
        self.disk_curve = self.disk_plot.plot(pen=pg.mkPen('r', width=2))
        self.disk_data = [0] * 60  # Last 60 seconds of Disk usage

        layout.addWidget(self.disk_plot)

        if show_detailed:
            # Detailed information
            disk_info = psutil.disk_usage('/')
            self.total_disk_label = QLabel(f"Total Disk Space: {disk_info.total / (1024 ** 3):.2f} GB")
            self.used_disk_label = QLabel("Used Disk Space: ")
            self.free_disk_label = QLabel("Free Disk Space: ")
            self.percent_disk_label = QLabel("Disk Usage Percentage: ")

            # Add detailed information to the layout
            details_layout = QVBoxLayout()
            details_layout.addWidget(self.total_disk_label)
            details_layout.addWidget(self.used_disk_label)
            details_layout.addWidget(self.free_disk_label)
            details_layout.addWidget(self.percent_disk_label)

            combined_layout = QHBoxLayout()
            combined_layout.addLayout(layout)
            combined_layout.addLayout(details_layout)

            self.setLayout(combined_layout)
        else:
            # Only graph layout
            self.setLayout(layout)

    def update_disk(self, data):
        """Update the Disk graph data and optionally update the details."""
        self.disk_curve.setData(data)

        # Update detailed labels only if they're visible
        try:
            disk_info = psutil.disk_usage('/')
            self.used_disk_label.setText(f"Used Disk Space: {disk_info.used / (1024 ** 3):.2f} GB")
            self.free_disk_label.setText(f"Free Disk Space: {disk_info.free / (1024 ** 3):.2f} GB")
            self.percent_disk_label.setText(f"Disk Usage Percentage: {disk_info.percent:.2f}%")
        except AttributeError:
            pass
