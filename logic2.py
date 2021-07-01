from tkinter import Tk
import math

root = Tk()
blank_space = ""
root.title(50 * blank_space + "Celestial")
root.resizable(width=False , height=False)
root.geometry("440x576+465+43")


class Calculator:
	def __init__(self):
		self.ans = 0
		self.num = " "
		self.inputValue = True
		self.check_ans = False
		self.operate = " "
		self.result = False
		
	def EnterVal(self, val):
		self.result = False
		firstVal = EntrDisplay.get()
		secondVal = str(val)
		
		if self.inputValue:
			self.num = secondVal
			self.inputValue = False
			
		else:
			if secondVal == ' . ':
				if secondVal in firstVal:
					self.num = firstVal + secondVal
					return self.num
		self.display(self.num)
		
	def totalVal(self):
		self.result = True
		self.num = float(self.num)
		
		if self.check_ans == True:
			self.validFunc()
			
		else:
			self.ans = float(EntDisplay.get())
			
	def display(self, value):
		EntrDisplay.delete(0, END)
		EntrDisplay.insert(0, value)
			
	def validFunc(self):
		if self.operate == "add":
			self.ans += self.num
		if self.operate == "subtract":
			self.ans -= self.num
		if self.operate == "multiply":
			self.ans *= self.num
		if self.operate == "divide":
			self.ans /= self.num
		if self.operate == "mod" :
			self.ans %= self.num
		
		self.inputValue = True
		self.check_ans = False
		self.display(self.ans)
		
	def operation(self,operate):
		self.num = float(self.num)
		
		if self.check_ans:
			self.validFunc()
			
		if not self.result:
			self.ans = self.num
			self.inputValue = True
		self.check_ans = True
		self.operate = operate
		self.result = False
		
	def backspace(self):
		num_len = len(EntrDisplay.get())
		EntrDisplay.delete(num_len - 1, ' ')
		if num_len == 1:
			EntrDisplay.insert(0, "0")
			
	def C_entry(self):
		self.result = False
		self.num = "0"
		self.display(0)
		self.inputValue ="True"
		
	def entry_allC(self):
		self.C_entry()
		self.ans = 0
		
	def sqrd(self):
		self.result = False
		self.num = math.sqrt(float(EntrDisplay.get()))
		self.display(self.num)
		
root.mainloop()
