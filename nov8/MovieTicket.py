from tkinter import *

class OnlineTicket(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		Label(self, text="Select language: ").grid(row=0, column=0, sticky=W)
		
		# radio buttons
		self.lang = IntVar() 
		self.english = Radiobutton(self, text="English", justify=LEFT,  variable=self.lang, value=1)
		self.english.grid(row=1, column=0, sticky=W)
		self.kannada = Radiobutton(self, text="Kannada", justify=LEFT, variable=self.lang, value=2)
		self.kannada.grid(row=2, column=0, sticky=W)
		self.hindi = Radiobutton(self, text="Hindi", justify=LEFT, variable=self.lang, value=3)
		self.hindi.grid(row=3, column=0, sticky=W)		
	
		Label(self, text="").grid(sticky=W)
		Label(self, text="Pick a movie name: ").grid(sticky=W) 

		# checkboxes
		self.movie1 = BooleanVar()
		self.movie2 = BooleanVar()
		self.movie3 = BooleanVar()
		self.andh = Checkbutton(self, text="Chichhore", variable=self.movie1)
		self.andh.grid(sticky=W)
		self.pail = Checkbutton(self, text="Pailwan", variable=self.movie2)
		self.pail.grid(sticky=W)		
		self.elc = Checkbutton(self, text="El Camino", variable=self.movie3)
		self.elc.grid(sticky=W)

		#option Menu
		Label(self, text="").grid(sticky=W)
		Label(self, text="No. of seats: ").grid(row=15, sticky=W) 
		seatlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		self.seat = IntVar()
		self.seat.set(seatlist[0])
		
		self.seats = OptionMenu(self, self.seat, *seatlist)
		self.seats.grid(row=15, column=1, sticky=W)		
	
		#submit
		Label(self, text="").grid(sticky=W)
		self.sub = Button(self, text="Submit", command=self.submit)
		self.sub.grid(sticky=W)

		#textbox
		Label(self, text="Message: ").grid(row=20, column=0, sticky=W)
		self.errorMsg = Entry(self, width=20)
		self.errorMsg.grid(row=20, column=1, sticky=W)

	def submit(self):
		lang = self.lang.get()
		if lang not in [1, 2, 3]:
			self.errorMsg.delete(0, END)
			self.errorMsg.insert(0, "No language selected")
		elif not self.movie1.get() and not self.movie2.get() and not self.movie3.get():
			self.errorMsg.delete(0, END)
			self.errorMsg.insert(0, "No movie selected")
		elif self.seat.get() == 0:
			self.errorMsg.delete(0, END)
			self.errorMsg.insert(0, "Select atleast 1 seat")
		else:
			self.errorMsg.delete(0, END)
			self.errorMsg.insert(0, "SUCCESS!")


if __name__ == "__main__":
	root = Tk()
	root.title = "Online Movie Ticket Booking"
	root.grid()
	app = OnlineTicket(root)

	root.mainloop()
