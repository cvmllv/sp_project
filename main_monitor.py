from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QGridLayout, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPalette, QColor
import getpass
from cpu_section import TopCPUProcessesWidget
from memory_section import TopMemoryProcessesWidget
from network_section import TopNetworkProcessesWidget, NetworkMonitorWidget
from battery_section import BatteryGraphWidget
from kill_process_section import KillerApp

class RectanglePlaceholder(QLabel):
    """A QLabel subclass to mimic a rectangle placeholder."""
    def __init__(self, width, height, color='#d3d3d3'):
        super().__init__()
        self.setFixedSize(QSize(width, height))
        self.setAutoFillBackground(True)

        # Setting the background color
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

        # Initialize a layout to organize children inside the rectangle
        self.inner_layout = QVBoxLayout()
        self.setLayout(self.inner_layout)

        # Set size policy to allow resizing within the layout
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


class ComplexUILayout(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Complex UI Layout with Rectangles")
        self.setMinimumSize(1400, 800)

        self.width = 450
        self.height = 100

        # Main layout to hold all sub-layouts
        main_layout = QGridLayout()
        main_layout.setSpacing(10)

        # Get the current PC user's username
        username = getpass.getuser()

        # First column of rectangles
        first_column = QVBoxLayout()
        first_column.setSpacing(10)

        # Create the rectangle placeholder
        welcome_rectangle = RectanglePlaceholder(self.width, 60 + self.height)

        # Create a label with the welcome message
        welcome_label = QLabel(f"Welcome back, {username}!", welcome_rectangle)
        welcome_label.setAlignment(Qt.AlignCenter)

        # Add the welcome label to the layout within the rectangle
        welcome_rectangle.inner_layout.addWidget(welcome_label)

        # Add other rectangles to the first column
        first_column.addWidget(welcome_rectangle)


        #Rectangle with CPU Usage
        cpu_rectangle = RectanglePlaceholder(self.width, 145 + self.height)
        
        cpu_label = QLabel("CPU Usage", cpu_rectangle)
        cpu_label.setAlignment(Qt.AlignLeft)
        cpu_label.setMargin(5)

        cpu_table = TopCPUProcessesWidget()

        #cpu_rectangle.inner_layout.addWidget(cpu_label)
        cpu_rectangle.inner_layout.addWidget(cpu_table)


        first_column.addWidget(cpu_rectangle)
        first_column.addWidget(RectanglePlaceholder(self.width, 235 + self.height))

        # Second column of rectangles
        second_column = QVBoxLayout()
        second_column.setSpacing(10)

        # Horizontal stack (right_stack_hbox) added to the second column
        right_stack_hbox = QHBoxLayout()
        right_stack_hbox.addWidget(RectanglePlaceholder(220, 60 + self.height))
        right_stack_hbox.addWidget(RectanglePlaceholder(220, 60 + self.height))

        second_column.addLayout(right_stack_hbox)  # Add the horizontal layout to the second column

        memory_rectangle = RectanglePlaceholder(self.width, 145 + self.height)

        memory_label = QLabel("Memory Usage", memory_rectangle)
        memory_table = TopMemoryProcessesWidget()
        memory_rectangle.inner_layout.addWidget(memory_label)
        memory_rectangle.inner_layout.addWidget(memory_table)


        second_column.addWidget(memory_rectangle)

        network_rectangle = RectanglePlaceholder(self.width, 235 + self.height)
        network_usage_label = QLabel("Network Usage", network_rectangle)
        network_process_table = TopNetworkProcessesWidget()
        network_usage_table = NetworkMonitorWidget()

        network_rectangle.inner_layout.addWidget(network_usage_label)
        network_rectangle.inner_layout.addWidget(network_process_table)
        network_rectangle.inner_layout.addWidget(network_usage_table)

        second_column.addWidget(network_rectangle)

        # Third column of rectangles
        third_column = QVBoxLayout()
        third_column.setSpacing(10)

        battery_rectangle = RectanglePlaceholder(self.width, 145 + self.height)
        battery_label = QLabel("Battery Usage", battery_rectangle)
        battery_graph = BatteryGraphWidget()

        battery_rectangle.inner_layout.addWidget(battery_label)
        battery_rectangle.inner_layout.addWidget(battery_graph)

        third_column.addWidget(battery_rectangle)

        
        third_column.addWidget(RectanglePlaceholder(self.width, 145 + self.height))


        kill_process_rectangle = RectanglePlaceholder(self.width, 145 + self.height)
        kill_process_label = QLabel("Enter the process you want to kill", kill_process_rectangle)
        kill_process = KillerApp()

        kill_process_rectangle.inner_layout.addWidget(kill_process_label)
        kill_process_rectangle.inner_layout.addWidget(kill_process)

        third_column.addWidget(kill_process_rectangle)
        
        # Add all columns to the grid layout
        main_layout.addLayout(first_column, 0, 0)
        main_layout.addLayout(second_column, 0, 1)
        main_layout.addLayout(third_column, 0, 2)

        # Set the main layout for the window
        self.setLayout(main_layout)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = ComplexUILayout()
    window.show()
    sys.exit(app.exec_())
