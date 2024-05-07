# disk_section.py
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QLabel
import psutil
import pyqtgraph as pg

class DiskSection(QGroupBox):
    def __init__(self):
        super().__init__("Disk Usage")

        # Create the main layout for the Disk section
        main_layout = QHBoxLayout()

        # Create the graph layout and add the PlotWidget
        graph_layout = QVBoxLayout()
        self.disk_plot = pg.PlotWidget(title="Disk Usage (%)")
        self.disk_plot.setYRange(0, 100)
        self.disk_curve = self.disk_plot.plot(pen=pg.mkPen('r', width=2))
        self.disk_data = [0] * 60  # Last 60 seconds of Disk usage
        graph_layout.addWidget(self.disk_plot)

        # Create the layout for Disk information labels
        info_layout = QVBoxLayout()

        # Example labels for various disk stats
        disk_info = psutil.disk_usage('/')
        self.total_disk_label = QLabel(f"Total Disk Space: {disk_info.total / (1024 ** 3):.2f} GB")
        self.used_disk_label = QLabel("Used Disk Space: ")
        self.free_disk_label = QLabel("Free Disk Space: ")
        self.percent_disk_label = QLabel("Disk Usage Percentage: ")

        # Add all labels to the layout
        info_layout.addWidget(self.total_disk_label)
        info_layout.addWidget(self.used_disk_label)
        info_layout.addWidget(self.free_disk_label)
        info_layout.addWidget(self.percent_disk_label)

        # Add graph and info layouts to the main layout
        main_layout.addLayout(graph_layout)
        main_layout.addLayout(info_layout)
        self.setLayout(main_layout)

    def update_disk(self, data):
        """Update the Disk graph and information labels."""
        # Update the graph data
        self.disk_curve.setData(data)

        # Get the latest disk stats
        disk_info = psutil.disk_usage('/')

        # Update the disk labels dynamically
        self.used_disk_label.setText(
            f"Used Disk Space: {disk_info.used / (1024 ** 3):.2f} GB"
        )
        self.free_disk_label.setText(
            f"Free Disk Space: {disk_info.free / (1024 ** 3):.2f} GB"
        )
        self.percent_disk_label.setText(
            f"Disk Usage Percentage: {disk_info.percent:.2f}%"
        )
