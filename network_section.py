# network_section.py
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QLabel
import psutil
import pyqtgraph as pg

class NetworkSection(QGroupBox):
    def __init__(self):
        super().__init__("Network Usage")

        # Create the main layout for the Network section
        main_layout = QHBoxLayout()

        # Create the graph layout and add the PlotWidget
        graph_layout = QVBoxLayout()
        self.network_plot = pg.PlotWidget(title="Network Traffic (KB/s)")
        self.network_plot.setYRange(0, 1000)  # Adjust the Y-range based on typical traffic levels
        self.incoming_curve = self.network_plot.plot(pen=pg.mkPen('g', width=2))  # Incoming traffic
        self.outgoing_curve = self.network_plot.plot(pen=pg.mkPen('m', width=2))  # Outgoing traffic
        self.incoming_data = [0] * 60  # Last 60 seconds for incoming traffic
        self.outgoing_data = [0] * 60  # Last 60 seconds for outgoing traffic
        graph_layout.addWidget(self.network_plot)

        # Create the layout for Network information labels
        info_layout = QVBoxLayout()

        # Add labels to display network statistics
        self.bytes_sent_label = QLabel("Bytes Sent: ")
        self.bytes_received_label = QLabel("Bytes Received: ")
        self.packets_sent_label = QLabel("Packets Sent: ")
        self.packets_received_label = QLabel("Packets Received: ")

        # Add all labels to the info layout
        info_layout.addWidget(self.bytes_sent_label)
        info_layout.addWidget(self.bytes_received_label)
        info_layout.addWidget(self.packets_sent_label)
        info_layout.addWidget(self.packets_received_label)

        # Add graph and info layouts to the main layout
        main_layout.addLayout(graph_layout)
        main_layout.addLayout(info_layout)
        self.setLayout(main_layout)

        # Initialize previous stats for delta calculation
        self.prev_net_io = psutil.net_io_counters()

    def update_network(self):
        """Update the Network graph and information labels."""
        # Get the latest network stats and calculate the delta
        net_io = psutil.net_io_counters()
        incoming_delta = (net_io.bytes_recv - self.prev_net_io.bytes_recv) / 1024
        outgoing_delta = (net_io.bytes_sent - self.prev_net_io.bytes_sent) / 1024

        # Update previous counters
        self.prev_net_io = net_io

        # Update incoming and outgoing traffic graphs
        self.incoming_data = self.incoming_data[1:] + [incoming_delta]
        self.outgoing_data = self.outgoing_data[1:] + [outgoing_delta]
        self.incoming_curve.setData(self.incoming_data)
        self.outgoing_curve.setData(self.outgoing_data)

        # Update network statistics labels dynamically
        self.bytes_sent_label.setText(f"Bytes Sent: {net_io.bytes_sent / (1024 ** 2):.2f} MB")
        self.bytes_received_label.setText(f"Bytes Received: {net_io.bytes_recv / (1024 ** 2):.2f} MB")
        self.packets_sent_label.setText(f"Packets Sent: {net_io.packets_sent}")
        self.packets_received_label.setText(f"Packets Received: {net_io.packets_recv}")
