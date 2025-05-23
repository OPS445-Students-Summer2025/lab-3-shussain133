#!/usr/bin/env python3
# Author ID: Shazma Hussain - (167689223)


import subprocess

def free_space():
    # Run the command and capture output
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, errors = p.communicate()

    # Return the result as a string in utf-8 and strip the newline characters
    return output.decode('utf-8').strip()

# Uncomment the next line to run the function
# print(free_space())
