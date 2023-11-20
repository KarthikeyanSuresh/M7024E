from ui.menu import ModernUI
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    ui_app = ModernUI(root)
    ui_app.root.mainloop()

# from cloudwatch.ec2metrics import CloudwatchMetrics
# import tkinter as tk
# from tkinter import ttk
# from ttkthemes import ThemedTk
# from PIL import Image, ImageTk

# # def main():
# #     # Replace 'YOUR_INSTANCE_ID' with your actual EC2 instance ID
# #     instance_id = 'i-0d01fafb039e0ad94'

# #     # List of metrics to monitor
# #     metrics_to_monitor = ['CPUUtilization', 'DiskReadBytes', 'DiskWriteBytes', 'NetworkIn', 'NetworkOut']

# #     # Instantiate the class
# #     ec2_metrics = CloudwatchMetrics(region='eu-north-1')

# #     for metric in metrics_to_monitor:
# #         data_points = ec2_metrics.get_ec2_metrics(instance_id, metric, period=300)
# #         if data_points:
# #             print(f"{metric} Data Points: {data_points}")
# #         else:
# #             print(f"No data available for {metric}")


