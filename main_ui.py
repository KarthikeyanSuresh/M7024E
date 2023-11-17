import os
from s3.operations import S3Operations
from s3.list_buckets import ListBuckets
from s3.create_buckets import CreateBuckets
from s3.delete_object import DeleteS3Object
import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog as sd 
import tkinter.filedialog as filedialog


class S3App:
    def __init__(self, master):
        self.master = master
        master.title("S3 Operations")

        self.label = tk.Label(master, text="The following actions are available: 1. Create S3 buckets, 2. List S3 buckets, 3. Operations in S3. Choose an action:")
        self.label.pack()

        self.create_button = tk.Button(master, text="Create S3 Buckets", command=self.create_buckets)
        self.create_button.pack()

        self.list_button = tk.Button(master, text="List S3 Buckets", command=self.list_buckets)
        self.list_button.pack()

        self.operations_button = tk.Button(master, text="Operations in S3", command=self.operations_in_s3)
        self.operations_button.pack()

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
        s3_operations = S3Operations(region_operation)

        if operation == "1":
            file_path = filedialog.askopenfilename(title="Select file to upload")
            object_key = sd.askstring("Input", "Enter the object key:")
            s3_operations.upload_s3_object(file_path, bucket_name, object_key)

        elif operation == "2":
            object_name = sd.askstring("Input", "Enter the name of the file to be downloaded:")
            object_key = sd.askstring("Input", "Enter the object key:")
            s3_operations.download_s3_object(bucket_name, object_key, object_name)

        elif operation == "3":
            object_key = sd.askstring("Input", "Enter the object key:")
            DeleteS3Object(bucket_name, object_key)

if __name__ == "__main__":
    root = tk.Tk()
    app = S3App(root)
    root.mainloop()
