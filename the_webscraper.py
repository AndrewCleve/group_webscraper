import tkinter as tk
##class myClass():
	# # def method1(self):
		# # print("myClass method1")
	# # def method2(self,someString):
		# # print("myClass method2:" + someString )
# # class anotherClass(myClass):
	# # def method2(self):
		# # print("anotherClass")
	# # class myClass():
		# # def method1(self):
			# # print("anotherClass method1")
# # def main():
	# # c = myClass()
	
	# # c.method1()
	# # c.method2("this is my string")
	
	# # c2 = anotherClass()
	
	# # c2.method1()
	# # c2.method2()
  
# # if __name__ == "__main__":
  # # main()
class GUI():
    def RunGUI(self):
        self.window = tk.Tk()
        
        l1 = tk.Label(self.window, text = "Enter website name here ")
        l2 = tk.Label(self.window, text = "Enter checkrate here ")
        l3 = tk.Label(self.window, text = "Enter SID here ")
        l4 = tk.Label(self.window, text = "Enter Twilio Authorization here ")
        l5 = tk.Label(self.window, text = "Enter Twilio phone number here ")
        l6 = tk.Label(self.window, text = "Enter user phone number here ")
        
        
        
        website = tk.Entry(self.window,  )
        checkrate = tk.Entry(self.window )
        sid = tk.Entry(self.window )
        auth = tk.Entry(self.window )
        twilphone = tk.Entry(self.window )
        userphone = tk.Entry(self.window )
        
        button = tk.Button(self.window, text ="Finish", width = 25, command = self.end() )
        
        l1.grid(row = 0, column = 0, pady =2)
        l2.grid(row = 1, column = 0, pady =2)
        l3.grid(row = 2, column = 0, pady =2)
        l4.grid(row = 3, column = 0, pady =2)
        l5.grid(row = 4, column = 0, pady =2)
        l6.grid(row = 5, column = 0, pady =2)
        
        website.grid(row = 0, column = 2, pady = 2)
        checkrate.grid(row = 1, column = 2, pady = 2)
        sid.grid(row = 2, column = 2, pady = 2)
        auth.grid(row = 3, column = 2, pady = 2)
        twilphone.grid(row = 4, column = 2, pady = 2)
        userphone.grid(row = 5, column = 2, pady = 2)
        
        button.grid(row=6, column =1 )
        
        
        
        self.window.mainloop()
    def end(self):
        self.window.destroy
    
   
if __name__ == "__main__":
    NewGUI = GUI()
    NewGUI.RunGUI()
    