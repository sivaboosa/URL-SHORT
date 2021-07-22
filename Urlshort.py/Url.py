from tkinter import *
import pyshorteners
import clipboard
window = Tk()

window.geometry("1200x1200") # window size

window.resizable(True,True) # making window resizable

window.title("URL Shortener") # Title

#url entry
url_input = Entry(window, font=("Hervetica","18"))
url_input.grid(row=3, column=4, pady=6)

#label shortened url
str_url = StringVar(window)

shortened_url =Label(window, textvariable=str_url, font =("Hervetica","16"),fg="light green",bg="black")
shortened_url.grid(row=4, column=5, pady=6)

# copy short url function
def copy_short_url():
  try:
    clipboard.copy(str_url.get())
    print("Url copied succesfully")
  except:
    str_url.set("something went wrong please try again")  

# copy short url button
copy_btn = Button(window, text="copy", bg="white", fg="black", font=("Helvetica","12"), command=copy_short_url)
copy_btn.grid(row=4, column=3, pady=6, padx=10)

# short url function
def short_url():
    try:
      s = pyshorteners.Shortener()
      url = url_input.get()
      final_result =s.tinyurl.short(url)
      str_url.set(final_result)
      url_input.delete(0,END)
    except:
        str_url.set("Enter url please")  

# Button to short url
btn = Button(window, text="Short Url", padx=8, pady=4, bg="white", fg="green", font= ("Helvetica","16"), activebackground="white", command=short_url)
btn.grid(row=2, column=3,pady=6)














window.mainloop()