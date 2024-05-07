import sys
import psutil
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton
from PyQt5.QtCore import QTimer
from cpu_section import CPUSection
from memory_section import MemorySection
from disk_section import DiskSection
from processes_section import ProcessesSection
from network_section import NetworkSection

class SystemMonitorDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("System Monitor Dashboard")
        self.setMinimumSize(1400, 800)

        # Create the main layout
        main_layout = QVBoxLayout()

        # Drop-down menu to select sections
        section_label = QLabel("Select a section:")
        self.section_combobox = QComboBox()
        self.section_combobox.addItem("CPU")
        self.section_combobox.addItem("Memory")
        self.section_combobox.addItem("Disk")
        self.section_combobox.addItem("Processes")
        self.section_combobox.addItem("Network")
        main_layout.addWidget(section_label)
        main_layout.addWidget(self.section_combobox)

        # Button to display summary of all sections
        self.summary_button = QPushButton("Show Summary of All Sections")
        self.summary_button.clicked.connect(self.show_summary)
        main_layout.addWidget(self.summary_button)

        # Content Layout (Dynamic sections)
        self.content_layout = QVBoxLayout()

        # CPU, Memory, Disk, Processes, Network Sections
        self.cpu_section = CPUSection()
        self.memory_section = MemorySection()
        self.disk_section = DiskSection()
        self.processes_section = ProcessesSection()
        self.network_section = NetworkSection()

        # Connect combo box selection to its handler
        self.section_combobox.currentIndexChanged.connect(self.show_selected_section)

        # Add the content layout to the main layout
        main_layout.addLayout(self.content_layout)

        self.setLayout(main_layout)

        # Initialize data for graphs
        self.cpu_data = [0] * 60
        self.memory_data = [0] * 60
        self.disk_data = [0] * 60
        self.process_data = [0] * 60
        self.network_data = [0] * 60

        # Set up a timer to update CPU, memory, disk, and process graphs
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_metrics)
        self.timer.start(1000)

        # Show the initial section (CPU by default)
        self.show_selected_section()

    def update_metrics(self):
        """Update CPU, memory, disk, and process information."""
        # CPU
        cpu_percent = psutil.cpu_percent(interval=0.1)
        self.cpu_data = self.cpu_data[1:] + [cpu_percent]
        self.cpu_section.update_cpu(self.cpu_data)

        # Memory
        memory_info = psutil.virtual_memory()
        memory_percent = memory_info.percent
        self.memory_data = self.memory_data[1:] + [memory_percent]
        self.memory_section.update_memory(self.memory_data)

        # Disk
        disk_usage = psutil.disk_usage('/').percent
        self.disk_data = self.disk_data[1:] + [disk_usage]
        self.disk_section.update_disk(self.disk_data)

        # Processes
        process_count = len(psutil.pids())
        self.process_data = self.process_data[1:] + [process_count]
        self.processes_section.update_processes(self.process_data)

        # Network (Placeholder data, replace with real)
        self.network_data = self.network_data[1:] + [50]  # Replace with actual network data
        self.network_section.update_network()

    def show_selected_section(self):
        """Show the selected section."""
        selected_section = self.section_combobox.currentText()
        self.clear_content_layout()
        if selected_section == "CPU":
            self.content_layout.addWidget(self.cpu_section)
        elif selected_section == "Memory":
            self.content_layout.addWidget(self.memory_section)
        elif selected_section == "Disk":
            self.content_layout.addWidget(self.disk_section)
        elif selected_section == "Processes":
            self.content_layout.addWidget(self.processes_section)
        elif selected_section == "Network":
            self.content_layout.addWidget(self.network_section)

    def show_summary(self):
        """Show a summary of graphs only in two columns."""
        self.clear_content_layout()

        # Create two columns to hold the graphs
        column1_layout = QVBoxLayout()
        column2_layout = QVBoxLayout()

        # Divide graphs across the two columns
        column1_layout.addWidget(self.cpu_section)
        column1_layout.addWidget(self.disk_section)
        column1_layout.addWidget(self.network_section)

        column2_layout.addWidget(self.memory_section)
        column2_layout.addWidget(self.processes_section)

        # Combine the two columns into a horizontal layout
        summary_layout = QHBoxLayout()
        summary_layout.addLayout(column1_layout)
        summary_layout.addLayout(column2_layout)

        self.content_layout.addLayout(summary_layout)

    def clear_content_layout(self):
        """Clear the current content layout."""
        for i in reversed(range(self.content_layout.count())):
            widget = self.content_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)
            else:
                self.content_layout.itemAt(i).layout().deleteLater()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SystemMonitorDashboard()
    window.show()
    sys.exit(app.exec_())
