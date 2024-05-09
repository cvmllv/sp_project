# network_section.py
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QLabel
import psutil
import pyqtgraph as pg

class NetworkSection(QGroupBox):
    def __init__(self, show_detailed=True):
        super().__init__("Network Traffic")
        layout = QVBoxLayout()

        # Network Traffic graph
        self.network_plot = pg.PlotWidget(title="Network Traffic (KB/s)")
        self.network_plot.setYRange(0, 1000)  # Adjust based on traffic levels
        self.incoming_curve = self.network_plot.plot(pen=pg.mkPen('g', width=2))  # Incoming traffic
        self.outgoing_curve = self.network_plot.plot(pen=pg.mkPen('m', width=2))  # Outgoing traffic
        self.incoming_data = [0] * 60  # Last 60 seconds of incoming traffic
        self.outgoing_data = [0] * 60  # Last 60 seconds of outgoing traffic

        layout.addWidget(self.network_plot)

        if show_detailed:
            # Detailed information
            self.bytes_sent_label = QLabel("Bytes Sent: ")
            self.bytes_received_label = QLabel("Bytes Received: ")
            self.packets_sent_label = QLabel("Packets Sent: ")
            self.packets_received_label = QLabel("Packets Received: ")

            # Add detailed information to the layout
            details_layout = QVBoxLayout()
            details_layout.addWidget(self.bytes_sent_label)
            details_layout.addWidget(self.bytes_received_label)
            details_layout.addWidget(self.packets_sent_label)
            details_layout.addWidget(self.packets_received_label)

            combined_layout = QHBoxLayout()
            combined_layout.addLayout(layout)
            combined_layout.addLayout(details_layout)

            self.setLayout(combined_layout)
        else:
            # Only graph layout
            self.setLayout(layout)

    def update_network(self):
        """Update the Network graph data and optionally update the details."""
        self.incoming_curve.setData(self.incoming_data)
        self.outgoing_curve.setData(self.outgoing_data)

        # Update detailed labels only if they're visible
        try:
            net_io = psutil.net_io_counters()
            self.bytes_sent_label.setText(f"Bytes Sent: {net_io.bytes_sent / (1024 ** 2):.2f} MB")
            self.bytes_received_label.setText(f"Bytes Received: {net_io.bytes_recv / (1024 ** 2):.2f} MB")
            self.packets_sent_label.setText(f"Packets Sent: {net_io.packets_sent}")
            self.packets_received_label.setText(f"Packets Received: {net_io.packets_recv}")
        except AttributeError:
            pass
