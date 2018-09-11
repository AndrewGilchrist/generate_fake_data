import os
import shutil

datapath = "/opt/data-demo/active"

def generate_test_data():
  create_file("250M", datapath + "/" + "test_data_250MB.bin")
  create_file("100M", datapath + "/" + "test_data_100MB.bin")
  create_file("50M", datapath + "/" + "test_data_50MB.bin")
  create_file("25M", datapath + "/" + "test_data_25MB.bin")
  create_file("5M", datapath + "/" + "test_data_5MB.bin")
  create_file("2M", datapath + "/" + "test_data_2MB.bin")

def create_file(size, path):
  print("create_file: " + path)
  command = "fallocate -l " + size + " " + path
  os.system(command)


generate_test_data()
