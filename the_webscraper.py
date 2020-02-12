import tkinter as tk

class RunGUI():
    window = tk.Tk()
    
    l1 = tk.Label(window, text = "Enter website name here ")
    l2 = tk.Label(window, text = "Enter checkrate here ")
    l3 = tk.Label(window, text = "Enter SID here ")
    l4 = tk.Label(window, text = "Enter Twilio Authorization here ")
    l5 = tk.Label(window, text = "Enter Twilio phone number here ")
    l6 = tk.Label(window, text = "Enter user phone number here ")
    
    
    
    website = tk.Entry(window,  )
    checkrate = tk.Entry(window )
    sid = tk.Entry(window )
    auth = tk.Entry(window )
    twilphone = tk.Entry(window )
    userphone = tk.Entry(window )
    
    button = tk.Button(window, text ="Finish", width = 25, command = print(website.get) )
    
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
    
    
    
    window.mainloop()
def end(window, website):
    window.destroy
    a = "ur mum"
   
if __name__ == "__main__":
    RunGUI()
