# memory_section.py
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QLabel
import psutil
import pyqtgraph as pg

class MemorySection(QGroupBox):
    def __init__(self):
        super().__init__("Memory Usage")

        # Create the main layout for the Memory section
        main_layout = QHBoxLayout()

        # Create the graph layout and add the PlotWidget
        graph_layout = QVBoxLayout()
        self.memory_plot = pg.PlotWidget(title="Memory Usage (%)")
        self.memory_plot.setYRange(0, 100)
        self.memory_curve = self.memory_plot.plot(pen=pg.mkPen('b', width=2))
        self.memory_data = [0] * 60  # Last 60 seconds for Memory usage
        graph_layout.addWidget(self.memory_plot)

        # Create the layout for Memory information labels
        info_layout = QVBoxLayout()

        # Example labels for various memory stats
        self.total_memory_label = QLabel(f"Total Memory: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
        self.available_memory_label = QLabel("Available Memory: ")
        self.used_memory_label = QLabel("Used Memory: ")
        self.percent_memory_label = QLabel("Memory Percentage Used: ")

        # Add all labels to the layout
        info_layout.addWidget(self.total_memory_label)
        info_layout.addWidget(self.available_memory_label)
        info_layout.addWidget(self.used_memory_label)
        info_layout.addWidget(self.percent_memory_label)

        # Add graph and info layouts to the main layout
        main_layout.addLayout(graph_layout)
        main_layout.addLayout(info_layout)
        self.setLayout(main_layout)

    def update_memory(self, data):
        """Update the Memory graph and information labels."""
        # Update the graph data
        self.memory_curve.setData(data)

        # Get the latest memory stats
        memory_info = psutil.virtual_memory()

        # Update the memory labels dynamically
        self.available_memory_label.setText(
            f"Available Memory: {memory_info.available / (1024 ** 3):.2f} GB"
        )
        self.used_memory_label.setText(
            f"Used Memory: {memory_info.used / (1024 ** 3):.2f} GB"
        )
        self.percent_memory_label.setText(
            f"Memory Percentage Used: {memory_info.percent:.2f}%"
        )
