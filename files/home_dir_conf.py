import os

# Get home dir
home_dir = os.path.expanduser("~")
conf_dir = ".python-course-home-dir-conf"
conf_dir_path = os.path.join(home_dir, conf_dir)

# Make dir
os.makedirs(conf_dir_path, exist_ok=True)

# Conf file
conf_file_name = "message.conf"

# Full path
conf_file_path = os.path.join(conf_dir_path, conf_file_name)

DEFAULT_MESSAGE = "Change me!"
if not os.path.exists(conf_file_path):
    with open(conf_file_path, "w") as out_file:
        out_file.write(DEFAULT_MESSAGE)
        print("Message set!")
else:
    with open(conf_file_path) as in_file:
        message = in_file.read()
        print(f"Config message: {message}.")
