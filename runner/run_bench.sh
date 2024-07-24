#!/bin/bash


# THREAD number_of_threads
bin/thread 100000

# FORK number_of_forks
bin/fork 16 | tail -n 1

# READ number_of_reads
bin/read 10000000

# WRITTE number_of_writtes
bin/write 10000000 a

# MMAP_MUNMAP number_of_maps/unmaps number_of_pages
bin/mmap_munmap 10000000 1

# RECV
bin/recv &
sleep 1

# SEND number_of_messages text
bin/send 10000000 a

# PAGE_FAULT number_of_faults
bin/page_fault 1000000
