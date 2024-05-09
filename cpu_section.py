# cpu_section.py
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QLabel
import pyqtgraph as pg

class CPUSection(QGroupBox):
    def __init__(self, show_detailed=True):
        super().__init__("CPU Usage")
        layout = QVBoxLayout()

        # CPU Usage graph
        self.cpu_plot = pg.PlotWidget(title="CPU Usage (%)")
        self.cpu_plot.setYRange(0, 100)
        self.cpu_curve = self.cpu_plot.plot(pen=pg.mkPen('y', width=2))
        self.cpu_data = [0] * 60  # Last 60 seconds for CPU usage

        layout.addWidget(self.cpu_plot)

        if show_detailed:
            # Detailed information
            self.logical_cores_label = QLabel("Logical Cores: 8")
            self.physical_cores_label = QLabel("Physical Cores: 8")
            self.cpu_freq_label = QLabel("Current Frequency: ")
            self.cpu_stats_label = QLabel("CPU Stats: ")

            # Add detailed information to the layout
            details_layout = QVBoxLayout()
            details_layout.addWidget(self.logical_cores_label)
            details_layout.addWidget(self.physical_cores_label)
            details_layout.addWidget(self.cpu_freq_label)
            details_layout.addWidget(self.cpu_stats_label)

            combined_layout = QHBoxLayout()
            combined_layout.addLayout(layout)
            combined_layout.addLayout(details_layout)

            self.setLayout(combined_layout)
        else:
            # Only graph layout
            self.setLayout(layout)

    def update_cpu(self, data):
        """Update the CPU graph data and optionally update the details."""
        self.cpu_curve.setData(data)

        # Update detailed labels only if they're visible
        try:
            import psutil
            cpu_info = psutil.cpu_freq()
            self.cpu_freq_label.setText(f"Current Frequency: {cpu_info.current:.2f} MHz")
            cpu_stats = psutil.cpu_stats()
            self.cpu_stats_label.setText(
                f"CPU Stats: ctx_switches={cpu_stats.ctx_switches}, "
                f"interrupts={cpu_stats.interrupts}, soft_interrupts={cpu_stats.soft_interrupts}"
            )
        except AttributeError:
            pass
