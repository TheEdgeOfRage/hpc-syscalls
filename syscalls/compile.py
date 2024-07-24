import subprocess

subprocess.call(["gcc", "-o", "thread", "thread.c", "-lpthread"])
subprocess.call(["gcc", "-o", "fork", "fork.c"])
subprocess.call(["gcc", "-o", "read", "read.c"])
subprocess.call(["gcc", "-o", "write", "write.c"])
subprocess.call(["gcc", "-o", "mmap_munmap", "mmap_munmap.c"])
subprocess.call(["gcc", "-o", "page_fault", "page_fault.c"])
subprocess.call(["gcc", "-o", "send", "send.c"])
subprocess.call(["gcc", "-o", "recv", "recv.c"])
subprocess.call(["gcc", "-o", "select", "select.c"])
