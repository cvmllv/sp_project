# main_monitor.py
import sys
import psutil
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QTimer
from menu_section import MenuSection
from home_section import HomeSection
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

        # Create the main layout divided into two parts: menu and content
        main_layout = QHBoxLayout()

        # Menu Section
        self.menu_section = MenuSection()

        # Content Layout (Dynamic sections)
        self.content_layout = QVBoxLayout()

        # Home, CPU, Memory, Disk, Processes, Network Sections
        self.home_section = HomeSection()
        self.cpu_section = CPUSection()
        self.memory_section = MemorySection()
        self.disk_section = DiskSection()
        self.processes_section = ProcessesSection()
        self.network_section = NetworkSection()

        # Connect menu signals to their handlers
        self.menu_section.signals.cpu_item_clicked.connect(self.show_cpu_section)
        self.menu_section.signals.memory_item_clicked.connect(self.show_memory_section)
        self.menu_section.signals.disk_item_clicked.connect(self.show_disk_section)
        self.menu_section.signals.processes_item_clicked.connect(self.show_processes_section)
        self.menu_section.signals.network_item_clicked.connect(self.show_network_section)

        # Add the menu section to the main layout
        main_layout.addWidget(self.menu_section, 1)
        main_layout.addLayout(self.content_layout, 4)

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
        self.network_section.update_network(self.network_data)

    def clear_content_layout(self):
        """Clear the current content layout."""
        for i in reversed(range(self.content_layout.count())):
            self.content_layout.itemAt(i).widget().setParent(None)

    def show_cpu_section(self):
        """Show the CPU section."""
        self.clear_content_layout()
        self.content_layout.addWidget(self.cpu_section)

    def show_memory_section(self):
        """Show the Memory section."""
        self.clear_content_layout()
        self.content_layout.addWidget(self.memory_section)

    def show_disk_section(self):
        """Show the Disk section."""
        self.clear_content_layout()
        self.content_layout.addWidget(self.disk_section)

    def show_processes_section(self):
        """Show the Processes section."""
        self.clear_content_layout()
        self.content_layout.addWidget(self.processes_section)

    def show_network_section(self):
        """Show the Network section."""
        self.clear_content_layout()
        self.content_layout.addWidget(self.network_section)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SystemMonitorDashboard()
    window.show()
    sys.exit(app.exec_())
