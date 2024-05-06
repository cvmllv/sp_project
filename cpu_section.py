# cpu_section.py
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QLabel
import psutil
import pyqtgraph as pg

class CPUSection(QGroupBox):
    def __init__(self):
        super().__init__("CPU Usage")
        
        # Create the main layout for the CPU section
        main_layout = QHBoxLayout()

        # Create the graph layout and add the PlotWidget
        graph_layout = QVBoxLayout()
        self.cpu_plot = pg.PlotWidget(title="CPU Usage (%)")
        self.cpu_plot.setYRange(0, 100)
        self.cpu_curve = self.cpu_plot.plot(pen=pg.mkPen('y', width=2))
        self.cpu_data = [0] * 60  # Last 60 seconds for CPU usage
        graph_layout.addWidget(self.cpu_plot)

        # Create the layout for CPU information labels
        info_layout = QVBoxLayout()

        # Example labels for various CPU stats
        self.logical_cores_label = QLabel(f"Logical Cores: {psutil.cpu_count(logical=True)}")
        self.physical_cores_label = QLabel(f"Physical Cores: {psutil.cpu_count(logical=False)}")
        self.cpu_freq_label = QLabel("Current Frequency: ")
        self.cpu_times_label = QLabel("CPU Times: ")
        self.cpu_stats_label = QLabel("CPU Stats: ")

        # Add all labels to the layout
        info_layout.addWidget(self.logical_cores_label)
        info_layout.addWidget(self.physical_cores_label)
        info_layout.addWidget(self.cpu_freq_label)
        info_layout.addWidget(self.cpu_times_label)
        info_layout.addWidget(self.cpu_stats_label)

        # Add graph and info layouts to the main layout
        main_layout.addLayout(graph_layout)
        main_layout.addLayout(info_layout)
        self.setLayout(main_layout)

    def update_cpu(self, data):
        """Update the CPU graph and information labels."""
        # Update the graph data
        self.cpu_curve.setData(data)

        # Update the CPU information labels dynamically
        cpu_freq = psutil.cpu_freq()
        cpu_times = psutil.cpu_times()
        cpu_stats = psutil.cpu_stats()

        # Update the labels with the latest CPU stats
        self.cpu_freq_label.setText(
            f"Current Frequency: {cpu_freq.current:.2f} MHz (Max: {cpu_freq.max:.2f} MHz, Min: {cpu_freq.min:.2f} MHz)"
        )
        self.cpu_times_label.setText(
            f"CPU Times: user={cpu_times.user:.2f}s, system={cpu_times.system:.2f}s, idle={cpu_times.idle:.2f}s"
        )
        self.cpu_stats_label.setText(
            f"CPU Stats: ctx_switches={cpu_stats.ctx_switches}, interrupts={cpu_stats.interrupts}, "
            f"soft_interrupts={cpu_stats.soft_interrupts}, syscalls={cpu_stats.syscalls}"
        )
