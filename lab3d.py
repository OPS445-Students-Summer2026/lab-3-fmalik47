#!/usr/bin/env python3

import subprocess

def free_space():
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = p.communicate()
    return stdout.decode('utf-8').strip()
