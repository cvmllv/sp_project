# memory_section.py
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QLabel
import psutil
import pyqtgraph as pg

class MemorySection(QGroupBox):
    def __init__(self, show_detailed=True):
        super().__init__("Memory Usage")
        layout = QVBoxLayout()

        # Memory Usage graph
        self.memory_plot = pg.PlotWidget(title="Memory Usage (%)")
        self.memory_plot.setYRange(0, 100)
        self.memory_curve = self.memory_plot.plot(pen=pg.mkPen('b', width=2))
        self.memory_data = [0] * 60  # Last 60 seconds of Memory usage

        layout.addWidget(self.memory_plot)

        if show_detailed:
            # Detailed information
            memory_info = psutil.virtual_memory()
            self.total_memory_label = QLabel(f"Total Memory: {memory_info.total / (1024 ** 3):.2f} GB")
            self.available_memory_label = QLabel("Available Memory: ")
            self.used_memory_label = QLabel("Used Memory: ")
            self.percent_memory_label = QLabel("Memory Percentage Used: ")

            # Add detailed information to the layout
            details_layout = QVBoxLayout()
            details_layout.addWidget(self.total_memory_label)
            details_layout.addWidget(self.available_memory_label)
            details_layout.addWidget(self.used_memory_label)
            details_layout.addWidget(self.percent_memory_label)

            combined_layout = QHBoxLayout()
            combined_layout.addLayout(layout)
            combined_layout.addLayout(details_layout)

            self.setLayout(combined_layout)
        else:
            # Only graph layout
            self.setLayout(layout)

    def update_memory(self, data):
        """Update the Memory graph data and optionally update the details."""
        self.memory_curve.setData(data)

        # Update detailed labels only if they're visible
        try:
            memory_info = psutil.virtual_memory()
            self.available_memory_label.setText(f"Available Memory: {memory_info.available / (1024 ** 3):.2f} GB")
            self.used_memory_label.setText(f"Used Memory: {memory_info.used / (1024 ** 3):.2f} GB")
            self.percent_memory_label.setText(f"Memory Percentage Used: {memory_info.percent:.2f}%")
        except AttributeError:
            pass
