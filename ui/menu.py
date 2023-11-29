import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.simpledialog as sd 
import tkinter.filedialog as filedialog
from PIL import Image, ImageTk
from ui.ec2 import EC2Operations
from cloudwatch.ec2metrics import CloudwatchMetrics
from s3.operations import S3Operations
from s3.list_buckets import ListBuckets
from s3.create_buckets import CreateBuckets
from ec2.instance_status import InstanceStatus
from ec2.stop_instances import StopInstances
from ec2.create_instance import CreateEC2Instance
from tkinter import Listbox
from pprint import pformat

class ModernUI:
    """
    The ModernUI class provides a graphical user interface for interacting with AWS services.

    This class uses the tkinter library to create a GUI. It provides methods to interact with AWS EC2 and S3 services.

    Attributes:
        root (tkinter.Tk): The root window for the GUI.

    Methods:
        create_main_menu(): Creates the main menu of the GUI.
        show_ec2_menu(): Shows the EC2 service menu.
        show_s3_menu(): Shows the S3 service menu.
        show_ec2_metrics_ui(): Shows the EC2 metrics UI.
        fetch_metrics(metrics_fetcher, instance_id, metric_name, period, region, result_label): Fetches EC2 metrics.
        create_ec2_instance(): Creates an EC2 instance.
        check_instance_status(): Checks the status of an EC2 instance.
        show_ec2_status(): Shows the status of an EC2 instance.
        stop_ec2_instance(): Stops an EC2 instance.
        create_buckets(): Creates S3 buckets.
        list_buckets(): Lists S3 buckets.
        operations_in_s3(): Performs operations in S3.
        clear_frame(): Clears the frame of the GUI.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("AWS Service Menu")
        self.root.geometry("700x800")
        self.create_main_menu()


    def create_main_menu(self):
        self.clear_frame()

        ttk.Label(self.root, text="Select Service", font=('Helvetica', 16)).pack(pady=20)

        # EC2 button
        ec2_button = ttk.Button(self.root, text="EC2", command=self.show_ec2_menu)
        ec2_button.pack(side="left", padx=20)

        # EC2 image
        ec2_image = ImageTk.PhotoImage(Image.open("ui/ec2_icon.png").resize((100, 100)))
        ec2_label = ttk.Label(self.root, image=ec2_image, compound="top")
        ec2_label.image = ec2_image
        ec2_label.pack(side="left", padx=20)

        # S3 button
        s3_button = ttk.Button(self.root, text="S3", command=self.show_s3_menu)
        s3_button.pack(side="right", padx=20)

        # S3 image
        s3_image = ImageTk.PhotoImage(Image.open("ui/s3_icon.png").resize((100, 100)))
        s3_label = ttk.Label(self.root, image=s3_image, compound="top")
        s3_label.image = s3_image
        s3_label.pack(side="right", padx=20)

    def show_ec2_menu(self):
        self.clear_frame()

        ttk.Label(self.root, text="EC2 Functions", font=('Helvetica', 16)).pack(pady=20)

        # Button to show metrics
        metrics_button = ttk.Button(self.root, text="Show Metrics", command=self.show_ec2_metrics_ui)
        metrics_button.pack(pady=10)

        # Button to create instance
        create_instance_button = ttk.Button(self.root, text="Create Instance", command=self.create_ec2_instance)
        create_instance_button.pack(pady=10)

        # Button to show status of EC2 instance
        show_status_button = ttk.Button(self.root, text="Show Instance Status", command=self.show_ec2_status)
        show_status_button.pack(pady=10)

        # Button to stop EC2 instance
        stop_instance_button = ttk.Button(self.root, text="Stop Instance", command=self.stop_ec2_instance)
        stop_instance_button.pack(pady=10)

        return_button = ttk.Button(self.root, text="Return to Main Menu", command=self.create_main_menu)
        return_button.pack(pady=20)
    
    def show_s3_menu(self):
        self.clear_frame()
        ttk.Label(self.root, text="S3 Functions", font=('Helvetica', 16)).pack(pady=20)
        self.label = tk.Label(self.root, text="The following actions are available: 1. Create S3 buckets, 2. List S3 buckets, 3. Operations in S3. Choose an action:", font=("Consolas", 12))
        self.label.pack(pady=10, padx=50)

        self.create_button = tk.Button(self.root, text="Create S3 Buckets", command=self.create_buckets, font=("Consolas", 12))
        self.create_button.pack(padx=10, pady=10)

        self.list_button = tk.Button(self.root, text="List S3 Buckets", command=self.list_buckets, font=("Consolas", 12))
        self.list_button.pack(padx=10, pady=10)

        self.operations_button = tk.Button(self.root, text="Operations in S3", command=self.operations_in_s3, font=("Consolas", 12))
        self.operations_button.pack(padx=10, pady=10)
        return_button = ttk.Button(self.root, text="Return to Main Menu", command=self.create_main_menu)
        return_button.pack(pady=20)

    def show_ec2_metrics_ui(self):
        self.clear_frame()
        ttk.Label(self.root, text="Available metrics are: CPUUtilization, DiskReadBytes, DiskWriteBytes, NetworkIn, NetworkOut").pack(pady=20)

        ttk.Label(self.root, text="Enter Instance ID:").pack(pady=5)
        instance_id_entry = ttk.Entry(self.root)
        instance_id_entry.pack(pady=5)

        ttk.Label(self.root, text="Enter Metric Name:").pack(pady=5)
        metric_name_entry = ttk.Entry(self.root)
        metric_name_entry.pack(pady=5)

        ttk.Label(self.root, text="Enter AWS Region:").pack(pady=5)
        region_entry = ttk.Entry(self.root)
        region_entry.pack(pady=5)

        ttk.Label(self.root, text="Enter Period to query:").pack(pady=5)
        period_entry = ttk.Entry(self.root)
        period_entry.pack(pady=5)

        result_label = ttk.Label(self.root, text="")
        result_label.pack(pady=20)

        fetch_metrics_button = ttk.Button(self.root, text="Fetch Metrics",
                                          command=lambda: self.fetch_metrics(
                                              EC2Operations(), instance_id_entry.get(), metric_name_entry.get(),
                                              int(period_entry.get()), region_entry.get(), result_label))
        fetch_metrics_button.pack(pady=20)
        return_button = ttk.Button(self.root, text="Return to Main Menu", command=self.create_main_menu)
        return_button.pack(pady=20)

    def fetch_metrics(self, metrics_fetcher, instance_id, metric_name, period,region, result_label):
        if region:
            self.region = region

        if not self.region:
            result_label.config(text="Please select or enter a region.")
            return

        ec2_metrics = CloudwatchMetrics(region=self.region)
        data_points = metrics_fetcher.fetch_metrics(ec2_metrics, instance_id, metric_name, period)

        if data_points:
            result_label.config(text=f"{metric_name} Data Points: {data_points}")
        else:
            result_label.config(text=f"No data available for {metric_name}")

    def create_ec2_instance(self):
        self.clear_frame()
        ttk.Label(self.root, text="Creating EC2 instance...").pack(pady=20)

        ttk.Label(self.root, text="Enter Instance Name:").pack(pady=5)
        instance_name_entry = ttk.Entry(self.root)
        instance_name_entry.pack(pady=5)

        ttk.Label(self.root, text="Enter Instance Type:").pack(pady=5)
        instance_type_entry = ttk.Entry(self.root)
        instance_type_entry.pack(pady=5)

        ttk.Label(self.root, text="Enter Image ID:").pack(pady=5)
        image_id_entry = ttk.Entry(self.root)
        image_id_entry.pack(pady=5)

        ttk.Label(self.root, text="Enter Key Pair Name:").pack(pady=5)
        key_pair_entry = ttk.Entry(self.root)
        key_pair_entry.pack(pady=5)

        ttk.Label(self.root, text="Enter Security Group ID:").pack(pady=5)
        security_group_entry = ttk.Entry(self.root)
        security_group_entry.pack(pady=5)

        ttk.Label(self.root, text="Enter AWS Region:").pack(pady=5)
        region_entry = ttk.Entry(self.root)
        region_entry.pack(pady=5)

        ttk.Label(self.root, text="Enter Instance Storage:").pack(pady=5)
        instance_storage_entry = ttk.Entry(self.root)
        instance_storage_entry.pack(pady=5)

        result_label = ttk.Label(self.root, text="")
        result_label.pack(pady=20)

        def create_inst():
            instance_name = instance_name_entry.get()
            instance_type = instance_type_entry.get()
            image_id = image_id_entry.get()
            key_pair = key_pair_entry.get()
            security_group = security_group_entry.get()
            region = region_entry.get()
            instance_storage = instance_storage_entry.get()
            instance = CreateEC2Instance(ami_id=image_id, instance_type=instance_type, storage_size=instance_storage, region=region, instance_name=instance_name, security_group=security_group, keypair=key_pair)
            result_message = instance.create_ec2_instance()
            messagebox.showinfo("Create Instance", result_message)  

        create_instance_button = ttk.Button(self.root, text="Create Instance", command=create_inst)
        create_instance_button.pack(pady=20)  

        return_button = ttk.Button(self.root, text="Return to Main Menu", command=self.create_main_menu)
        return_button.pack(pady=20)

    def check_instance_status(self):
        region = "us-east-1"  # You can modify this to get user input or set a default region
        instance_status = InstanceStatus(region)
        status_message = instance_status.get_instance_status()
        self.label_result.config(text=status_message)
        messagebox.showinfo("Instance Status", status_message)

    def show_ec2_status(self):
        self.clear_frame()
        # Implement code to show EC2 instance status here
        ttk.Label(self.root, text="Showing EC2 instance status...").pack(pady=20)
        ttk.Label(self.root, text="Enter AWS Region:").pack(pady=5)
        region_entry = ttk.Entry(self.root)
        region_entry.pack(pady=5)

        def show_status():
            region = region_entry.get()
            inst = InstanceStatus(region)
            status_message = inst.get_instance_status()
            messagebox.showinfo("Instance Status", status_message)

        show_status_button = ttk.Button(self.root, text="Show Instance Status", command=show_status)
        show_status_button.pack(pady=20)

        return_button = ttk.Button(self.root, text="Return to Main Menu", command=self.create_main_menu)
        return_button.pack(pady=20)

    def stop_ec2_instance(self):
        self.clear_frame()
        ttk.Label(self.root, text="Stopping EC2 instance...").pack(pady=20)
        ttk.Label(self.root, text="Enter AWS Region:").pack(pady=5)
        region_entry = ttk.Entry(self.root)
        region_entry.pack(pady=5)
        ttk.Label(self.root, text="Enter Instance ID:").pack(pady=5)
        instance_id_entry = ttk.Entry(self.root)
        instance_id_entry.pack(pady=5)

        def stop_instance():
            region = region_entry.get()
            instance_id = instance_id_entry.get()
            instance = StopInstances(region)
            result_message = instance.stop_instance(instance_id)
            messagebox.showinfo("Stop Instance", result_message)

        stop_instance_button = ttk.Button(self.root, text="Stop Instance", command=stop_instance)
        stop_instance_button.pack(pady=20)

        return_button = ttk.Button(self.root, text="Return to Main Menu", command=self.create_main_menu)
        return_button.pack(pady=20)

    def create_buckets(self):
        num_buckets = int(sd.askstring("Input", "How many buckets do you want to create?"))
        for i in range(num_buckets):
            bucket_name = sd.askstring("Input", "Enter a bucket name:")
            bucket_region = sd.askstring("Input", "Enter a region:")
            s3_bucket_creation = CreateBuckets(bucket_name, bucket_region)
            s3_bucket_creation.create_bucket()

    def list_buckets(self):
        region = sd.askstring("Input", "Enter region to list the existing buckets in that region:")
        s3_bucket_list = ListBuckets(region)
        buckets = s3_bucket_list.get_buckets_in_region()
        message = f"The list of existing buckets in the {region} region are:\n{', '.join(buckets)}"
        messagebox.showinfo("List of Buckets", message)

    def operations_in_s3(self):
        operation = sd.askstring("Input", "Enter the number of the operation you want to perform:\n1. Upload\n2. Download\n3. Delete")
        bucket_name = sd.askstring("Input", "Enter the bucket name:")
        region_operation = sd.askstring("Input", "Enter the region:")

        if operation == "1":
            file_path = filedialog.askopenfilename(title="Select file to upload")
            s3_operations = S3Operations(region_operation)
            object_key = sd.askstring("Input", "Enter the object key:")
            s3_operations.upload_s3_object(file_path, bucket_name, object_key)

        elif operation == "2":
            object_name = sd.askstring("Input", "Enter the name of the file to be downloaded:")
            s3_operations = S3Operations(region_operation)
            object_key = sd.askstring("Input", "Enter the object key:")
            s3_operations.download_s3_object(bucket_name, object_key, object_name)

        elif operation == "3":
            object_key = sd.askstring("Input", "Enter the object key:")
            s3_operations = S3Operations(region_operation)
            s3_operations.delete_s3_object(bucket_name, object_key)

        return_button = ttk.Button(self.root, text="Return to Main Menu", command=self.create_main_menu)
        return_button.pack(pady=20)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernUI(root)
    root.mainloop()
