import io
import subprocess

# THREAD number_of_threads
subprocess.call(["./thread", "100000"])

# FORK number_of_forks
proc = subprocess.Popen(["./fork", "8"], stdout=subprocess.PIPE)
for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):
  pass
print(line, end='')

# READ number_of_reads
subprocess.call(["./read", "10000000"])

# WRITE number_of_writtes text
subprocess.call(["./write", "10000000", "a"])

# MMAP_MUNMAP number_of_maps/unmaps number_of_pages
subprocess.call(["./mmap_munmap", "1000000", "1000"])
subprocess.call(["./mmap_munmap", "1000000", "1"])

# PAGE_FAULT number_of_faults
subprocess.call(["./page_fault", "100000"])

# RECV
subprocess.Popen(["./recv"])    # background process

# SEND number_of_messages text
subprocess.call(["./send", "100000", "a"])

# SELECT number of messages text
subprocess.call(["./select", "100000"])
