# processes_section.py
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QLabel, QListWidget
import psutil
import pyqtgraph as pg

class ProcessesSection(QGroupBox):
    def __init__(self):
        super().__init__("Processes Count and Details")

        # Create the main layout for the Processes section
        main_layout = QHBoxLayout()

        # Create the graph layout and add the PlotWidget
        graph_layout = QVBoxLayout()
        self.process_plot = pg.PlotWidget(title="Running Processes")
        self.process_plot.setYRange(0, 200)  # Adjust this based on the average process count of your system
        self.process_curve = self.process_plot.plot(pen=pg.mkPen('b', width=2))
        self.process_data = [0] * 60  # Last 60 seconds of process count
        graph_layout.addWidget(self.process_plot)

        # Create the layout for process details labels
        info_layout = QVBoxLayout()
        self.process_count_label = QLabel("Current Process Count: 0")

        # Add a list widget to display the names of processes
        self.process_list = QListWidget()
        self.process_list.setFixedHeight(200)

        # Add all labels and the list to the layout
        info_layout.addWidget(self.process_count_label)
        info_layout.addWidget(self.process_list)

        # Add graph and info layouts to the main layout
        main_layout.addLayout(graph_layout)
        main_layout.addLayout(info_layout)
        self.setLayout(main_layout)

    def update_processes(self, data):
        """Update the Processes graph and information labels."""
        # Update the graph data
        self.process_curve.setData(data)

        # Get the current number of running processes
        current_processes = psutil.pids()
        process_count = len(current_processes)

        # Update the process count label
        self.process_count_label.setText(f"Current Process Count: {process_count}")

        # Update the list of processes with names and PIDs
        self.process_list.clear()
        for pid in current_processes[:10]:  # Display only the top 10 processes
            try:
                proc = psutil.Process(pid)
                proc_info = f"{proc.pid}: {proc.name()}"
                self.process_list.addItem(proc_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
