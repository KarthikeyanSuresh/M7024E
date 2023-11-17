from s3.operations import S3Operations
from s3.list_buckets import ListBuckets
from s3.create_buckets import CreateBuckets
import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog as sd 
import tkinter.filedialog as filedialog


class S3App:
    """
    This class represents a simple GUI application for performing operations on Amazon S3.
    The operations include creating S3 buckets, listing S3 buckets, and performing operations within S3.

    Attributes:
        - master: The root or parent window where the buttons will be displayed.
        - label: A label widget to display text on the window.
        - create_button: A button that triggers the 'create_buckets' method when clicked.
        - list_button: A button that triggers the 'list_buckets' method when clicked.
        - operations_button: A button that triggers the 'operations_in_s3' method when clicked.

    Methods:
        - create_buckets(): Creates S3 buckets in the specified region.
        - list_buckets(): Lists the existing S3 buckets in the specified region.
        - operations_in_s3(): Performs operations in S3.
    """
    def __init__(self, master):
        self.master = master
        master.title("S3 Operations")

        self.label = tk.Label(master, text="The following actions are available: 1. Create S3 buckets, 2. List S3 buckets, 3. Operations in S3. Choose an action:", font=("Consolas", 12))
        self.label.pack(pady=10, padx=50)

        self.create_button = tk.Button(master, text="Create S3 Buckets", command=self.create_buckets, font=("Consolas", 12))
        self.create_button.pack(padx=10, pady=10)

        self.list_button = tk.Button(master, text="List S3 Buckets", command=self.list_buckets, font=("Consolas", 12))
        self.list_button.pack(padx=10, pady=10)

        self.operations_button = tk.Button(master, text="Operations in S3", command=self.operations_in_s3, font=("Consolas", 12))
        self.operations_button.pack(padx=10, pady=10)

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

if __name__ == "__main__":
    root = tk.Tk() 
    app = S3App(root)
    root.mainloop()
