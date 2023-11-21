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

class ModernUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AWS Service Menu")
        self.root.geometry("600x400")
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
        s3_button.pack(side="left", padx=20)

        # S3 image
        s3_image = ImageTk.PhotoImage(Image.open("ui/s3_icon.png").resize((100, 100)))
        s3_label = ttk.Label(self.root, image=s3_image, compound="top")
        s3_label.image = s3_image
        s3_label.pack(side="left", padx=20)

    def show_ec2_menu(self):
        self.clear_frame()

        ttk.Label(self.root, text="EC2 Functions", font=('Helvetica', 16)).pack(pady=20)

        # Button to show metrics
        metrics_button = ttk.Button(self.root, text="Show Metrics", command=self.show_ec2_metrics_ui)
        metrics_button.pack(pady=10)

        # Button to create instance
        create_instance_button = ttk.Button(self.root, text="Create Instance", command=self.create_ec2_instance)
        create_instance_button.pack(pady=10)

        # Button to list instances
        list_instances_button = ttk.Button(self.root, text="List Instances", command=self.list_ec2_instances)
        list_instances_button.pack(pady=10)

        # Button to show status of EC2 instance
        show_status_button = ttk.Button(self.root, text="Show Instance Status", command=self.show_ec2_status)
        show_status_button.pack(pady=10)

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
        ttk.Label(self.root, text="Enter Instance ID:").pack(pady=5)
        instance_id_entry = ttk.Entry(self.root)
        instance_id_entry.pack(pady=5)

        ttk.Label(self.root, text="Enter Metric Name:").pack(pady=5)
        metric_name_entry = ttk.Entry(self.root)
        metric_name_entry.pack(pady=5)

        ttk.Label(self.root, text="Enter AWS Region:").pack(pady=5)
        region_entry = ttk.Entry(self.root)
        region_entry.pack(pady=5)

        result_label = ttk.Label(self.root, text="")
        result_label.pack(pady=20)

        fetch_metrics_button = ttk.Button(self.root, text="Fetch Metrics",
                                          command=lambda: self.fetch_metrics(
                                              EC2Operations(), instance_id_entry.get(), metric_name_entry.get(),
                                              region_entry.get(), result_label))
        fetch_metrics_button.pack(pady=20)
        return_button = ttk.Button(self.root, text="Return to Main Menu", command=self.create_main_menu)
        return_button.pack(pady=20)

    def fetch_metrics(self, metrics_fetcher, instance_id, metric_name, region, result_label):
        if region:
            self.region = region

        if not self.region:
            result_label.config(text="Please select or enter a region.")
            return

        ec2_metrics = CloudwatchMetrics(region=self.region)

        data_points = metrics_fetcher.fetch_metrics(ec2_metrics, instance_id, metric_name)

        if data_points:
            result_label.config(text=f"{metric_name} Data Points: {data_points}")
        else:
            result_label.config(text=f"No data available for {metric_name}")

    def create_ec2_instance(self):
        # Implement code to create EC2 instance here
        ttk.Label(self.root, text="Creating EC2 instance...").pack(pady=20)

    def list_ec2_instances(self):
        # Implement code to list EC2 instances here
        ttk.Label(self.root, text="Listing EC2 instances...").pack(pady=20)

    def show_ec2_status(self):
        # Implement code to show EC2 instance status here
        ttk.Label(self.root, text="Showing EC2 instance status...").pack(pady=20)

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
