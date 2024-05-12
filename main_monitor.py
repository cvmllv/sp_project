from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QGridLayout, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPalette, QColor, QPainter, QBrush, QPen, QFont
import getpass
from cpu_section import TopCPUProcessesWidget
from memory_section import TopMemoryProcessesWidget
from network_section import TopNetworkProcessesWidget, NetworkMonitorWidget
from battery_section import BatteryGraphWidget
from kill_process_section import KillerApp
from toggle_switch import ThemeSwitch

class RectanglePlaceholder(QWidget):
    """A QWidget subclass to mimic a rectangle placeholder."""
    def __init__(self, width, height, color='#d3d3d3'):
        super().__init__()
        self.setFixedSize(QSize(width, height))
        self.setAutoFillBackground(True)

        # Setting the background color
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

        # Initialize a layout to organize children inside the rectangle
        self.inner_layout = QVBoxLayout(self)
        self.inner_layout.setContentsMargins(10, 10, 10, 10)

        # Set size policy to allow resizing within the layout
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Define the pen and brush for the rectangle
        main_color = QColor('#000000')  # Purple color

        # Create pens with slightly offset colors to mimic shadow effect
        shadow_pen1 = QPen(QColor(main_color.red(), main_color.green(), main_color.blue(), 100))
        shadow_pen1.setWidth(5)

        shadow_pen2 = QPen(QColor(main_color.red(), main_color.green(), main_color.blue(), 75))
        shadow_pen2.setWidth(5)
        shadow_pen3 = QPen(QColor(main_color.red(), main_color.green(), main_color.blue(), 50))
        shadow_pen3.setWidth(5)
        shadow_pen4 = QPen(QColor(main_color.red(), main_color.green(), main_color.blue(), 25))
        shadow_pen4.setWidth(5)
        #brush = QBrush(QColor('#a9cce3'))  # Light purple color

        # Set the pen and brush
        painter.setPen(shadow_pen1)
        painter.setPen(shadow_pen2)
        painter.setPen(shadow_pen3)
        painter.setPen(shadow_pen4)
        #painter.setBrush(brush)

        # Draw the rectangle
        painter.drawRoundedRect(self.rect(), 5, 5)

        # Draw the background color for the label
       # painter.fillRect(self.rect(), QColor('#FFB6C1'))  # Light blue color


class ComplexUILayout(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Complex UI Layout with Rectangles")
        #self.setStyleSheet("color: purple;")
        self.setMinimumSize(1400, 800)

        self.width = 450
        self.height = 100

        self.light_theme()

        # Main layout to hold all sub-layouts
        main_layout = QGridLayout()
        main_layout.setSpacing(10)

        # Get the current PC user's username
        username = getpass.getuser()


        # First column of rectangles
        first_column = QVBoxLayout()
        first_column.setSpacing(10)

        # Create the rectangle placeholder
        welcome_rectangle = RectanglePlaceholder(self.width, 60 + self.height, '#800080')  # Light blue color

        # Create a label with the welcome message
        welcome_label = QLabel(f"Welcome back, {username}!", welcome_rectangle)
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setFont(QFont('Monaco', 16, QFont.Bold)) 
        welcome_label.setStyleSheet("color: white;")  

        # Add the welcome label to the layout within the rectangle
        welcome_rectangle.inner_layout.addWidget(welcome_label)

        # Add other rectangles to the first column
        first_column.addWidget(welcome_rectangle)

        #Rectangle with CPU Usage
        cpu_rectangle = RectanglePlaceholder(self.width, 145 + self.height,'#FFFFFF')
        cpu_label = QLabel("CPU Usage", cpu_rectangle)
        cpu_label.setStyleSheet("color: purple;")
        cpu_label.setAlignment(Qt.AlignLeft)
        cpu_label.setMargin(5)
        cpu_table = TopCPUProcessesWidget()
        cpu_rectangle.inner_layout.addWidget(cpu_label)
        cpu_rectangle.inner_layout.addWidget(cpu_table)
        first_column.addWidget(cpu_rectangle)
        first_column.addWidget(RectanglePlaceholder(self.width, 235 + self.height,'#FFFFFF'))

        # Second column of rectangles
        second_column = QVBoxLayout()
        second_column.setSpacing(10)
        right_stack_hbox = QHBoxLayout()

        self.theme_switch = ThemeSwitch()
  

        right_stack_hbox.addWidget(self.theme_switch)
        self.theme_switch.toggle_button.clicked.connect(self.switch_theme)   
        right_stack_hbox.addWidget(RectanglePlaceholder(220, 60 + self.height,'#FFFFFF'))
        second_column.addLayout(right_stack_hbox)

        memory_rectangle = RectanglePlaceholder(self.width, 145 + self.height,'#FFFFFF')
        memory_label = QLabel("Memory Usage", memory_rectangle)
        memory_label.setStyleSheet("color: purple;")
        memory_table = TopMemoryProcessesWidget()
        memory_rectangle.inner_layout.addWidget(memory_label)
        memory_rectangle.inner_layout.addWidget(memory_table)
        second_column.addWidget(memory_rectangle)

        network_rectangle = RectanglePlaceholder(self.width, 235 + self.height,'#FFFFFF')
        network_usage_label = QLabel("Network Usage", network_rectangle)
        network_usage_label.setStyleSheet("color: purple;")
        network_process_table = TopNetworkProcessesWidget()
        network_usage_table = NetworkMonitorWidget()
        network_rectangle.inner_layout.addWidget(network_usage_label)
        network_rectangle.inner_layout.addWidget(network_process_table)
        network_rectangle.inner_layout.addWidget(network_usage_table)
        second_column.addWidget(network_rectangle)

        # Third column of rectangles
        third_column = QVBoxLayout()
        third_column.setSpacing(10)
        battery_rectangle = RectanglePlaceholder(self.width, 145 + self.height,'#FFFFFF')
        battery_label = QLabel("Battery Usage", battery_rectangle)
        battery_label.setStyleSheet("color: purple;")
        battery_graph = BatteryGraphWidget()
        battery_rectangle.inner_layout.addWidget(battery_label)
        battery_rectangle.inner_layout.addWidget(battery_graph)
        third_column.addWidget(battery_rectangle)
        third_column.addWidget(RectanglePlaceholder(self.width, 145 + self.height,'#FFFFFF'))
        kill_process_rectangle = RectanglePlaceholder(self.width, 145 + self.height,'#FFFFFF')
        kill_process_label = QLabel("Enter the process you want to kill", kill_process_rectangle)
        kill_process_label.setStyleSheet("color: purple;")
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


    def switch_theme(self):
        self.theme_switch.toggle_theme()
        # Toggle the theme based on the internal state of the theme switcher
        if self.theme_switch.checked:  # Assuming 'checked' is a boolean attribute of ThemeSwitch
            self.dark_theme()
        else:
            self.light_theme()


    def dark_theme(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: white;
                color: #E7D5F6;
            }
            QWidget {
                background-color: #3E3E3E;
                color: #E7D5F6;
            }    
            QPushButton {
                background-color: #555555;
                color: white;
            }
            RectanglePlaceholder{
                background-color: #2E2E2E;
                color: white;
            }
            RectanglePlaceholder QLabel {
                color: white;
            }
            QTableWidget {
                background-color: transparent;
                border: none;
                color: #FFFFFF;
                font-size: 13px;
            }
            QHeaderView::section {
                background-color: rgba(255, 255, 255, 0.3);
                text-align: left;
                font-size: 13px;
                color: #E7D5F6;  
                font-weight: 500;
            }
            QTableWidget QHeaderView {
                background-color: rgba(255, 255, 255, 0.3);
                font-size: 13px;
                color: #E7D5F6;  
                border: none;
                font-weight: 500;
                text-transform: uppercase;
            }
            QTableWidget QTableWidgetItem {
                padding: 3px;
                color: #fff;
            }
            QTableWidget::item:selected {
                background: rgba(255, 255, 255, 0.5);
            }
        """)


    def light_theme(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #ffffff;
                color: black;
            }
            QVBoxLayout {
                background-color: white;
            } 
            QPushButton {
                background-color: #eeeeee;
                color: black;
            }
            QLabel {
                color: black;
            }
            QTableWidget {
                background-color: transparent;
                border: none;
                color: #000000;
                font-size: 13px;
            }
            QHeaderView::section {
                background-color: rgba(255, 255, 255, 0.3);
                text-align: left;
                font-size: 13px;
                color: #562680;  
                font-weight: 500;
            }
            QTableWidget QHeaderView {
                background-color: rgba(255, 255, 255, 0.3);
                font-size: 13px;
                color: #562680;  
                border: none;
                font-weight: 500;
                text-transform: uppercase;
            }
            QTableWidget QTableWidgetItem {
                padding: 3px;
                color: #fff;
            }
            QTableWidget::item:selected {
                background: rgba(255, 255, 255, 0.5);
            }
            """)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = ComplexUILayout()
    window.show()
    sys.exit(app.exec_())