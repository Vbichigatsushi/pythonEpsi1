from tkinter import *
from tkinter import ttk

def calculatePercentage():
	totalValue = int(total_field.get())
	usedValue = int(used_field.get())

	if usedValue<totalValue:
		usedPercentage.set(f'{((usedValue/totalValue)*100):.2f} % utilisés !')
	else:
		usedPercentage.set('Error : used is bigger than total !')

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

total_field = StringVar()
used_field = StringVar()

ttk.Label(frm, text='Total capacity (Gb)').grid(row=0, column=0)
ttk.Entry(frm, textvariable=total_field).grid(row=0, column=1)
ttk.Label(frm, text='Used capacity (Gb)').grid(row=1, column=0)
ttk.Entry(frm, textvariable=used_field).grid(row=1, column=1)

ttk.Button(frm, text='Percent usage', command=calculatePercentage).grid(row=2, column=1)

usedPercentage = StringVar()
ttk.Label(frm, textvariable=usedPercentage).grid(row=3, columnspan=2)
root.mainloop()