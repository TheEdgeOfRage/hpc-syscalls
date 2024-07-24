import os
import sys

import numpy as np
import plotly.graph_objects as go
from scipy.interpolate import interp1d

thread = []
fork = []
read = []
write = []
mmap_munmap = []
send = []
recv = []
page_fault = []
configs = []

headerColor = 'grey'
rowEvenColor = 'lightgrey'
rowOddColor = 'white'

colors = [
	'rgb(63, 255, 63)',
	'rgb(191, 255, 63)',
	'rgb(223, 255, 63)',
	'rgb(255, 255, 63)',
	'rgb(255, 191, 63)',
	'rgb(255, 127, 63)',
	'rgb(255, 63, 63)',
]

for filename in sorted(os.listdir(sys.argv[1])):
	configs.append(filename[:-4])
	with open(os.path.join(sys.argv[1], filename)) as f:
		content = f.readlines()

	new_dict = dict()
	for line in content[1:]:
		new_dict[line.split(',')[0]] = int(line.split(',')[2])

	thread.append(int(new_dict['thread'] / 1000))
	fork.append(int(new_dict['fork'] / 1000))
	read.append(int(new_dict['read'] / 1000))
	write.append(int(new_dict['write'] / 1000))
	mmap_munmap.append(int(new_dict['mmap_munmap'] / 1000))
	send.append(int(new_dict['send'] / 1000))
	recv.append(int(new_dict['recv'] / 1000))
	page_fault.append(int(new_dict['page_fault'] / 1000))


threadcolorfilter = interp1d([min(thread), max(thread)], [0, 6])
threadcolor = [int(threadcolorfilter(x)) for x in thread]

forkcolorfilter = interp1d([min(fork), max(fork)], [0, 6])
forkcolor = [int(forkcolorfilter(x)) for x in fork]

readcolorfilter = interp1d([min(read), max(read)], [0, 6])
readcolor = [int(readcolorfilter(x)) for x in read]

writecolorfilter = interp1d([min(write), max(write)], [0, 6])
writecolor = [int(writecolorfilter(x)) for x in write]

mmap_munmapcolorfilter = interp1d([min(mmap_munmap), max(mmap_munmap)], [0, 6])
mmap_munmapcolor = [int(mmap_munmapcolorfilter(x)) for x in mmap_munmap]

sendcolorfilter = interp1d([min(send), max(send)], [0, 6])
sendcolor = [int(sendcolorfilter(x)) for x in send]

recvcolorfilter = interp1d([min(recv), max(recv)], [0, 6])
recvcolor = [int(recvcolorfilter(x)) for x in recv]

page_faultcolorfilter = interp1d([min(page_fault), max(page_fault)], [0, 6])
page_faultcolor = [int(page_faultcolorfilter(x)) for x in page_fault]

fig = go.Figure(
	data=[go.Table(
		columnorder=[1, 2, 3, 4, 5, 6, 7, 8, 9],
		columnwidth=[7, 2, 2, 2, 2, 3, 2, 2, 2],
		header=dict(
			values=[
				"config",
				"thread",
				"fork",
				"read",
				"write",
				"mmap_munmap",
				"send",
				"recv",
				"page_fault"
			],
			line_color='darkslategray',
			fill_color=headerColor,
			align=['left', 'center'],
			font=dict(color='white', size=13)
		),
		cells=dict(
			values=[
				configs,
				thread,
				fork,
				read,
				write,
				mmap_munmap,
				send,
				recv,
				page_fault,
			],
			line_color='darkslategray',
			fill_color=[
				rowOddColor,
				np.array(colors)[threadcolor],
				np.array(colors)[forkcolor],
				np.array(colors)[readcolor],
				np.array(colors)[writecolor],
				np.array(colors)[mmap_munmapcolor],
				np.array(colors)[sendcolor],
				np.array(colors)[recvcolor],
				np.array(colors)[page_faultcolor],
			],
			align=['left', 'center'],
			font=dict(color='darkslategray', size=13)
		)
	)]
)

fig.show()
