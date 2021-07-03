from tkinter import *                                       #importing files
from tkinter import filedialog
from PIL import Image, ImageTk 
import PIL
from simpleimage import SimpleImage
import pywhatkit

BRIGHT_THRESHOLD = 200                                      #bright threshold to find sufficiently brighter pixels

root = Tk()                                                 #giving title and heading
root.title("Brain Infection Detector")
label = Label(root, text = "Brain Infection Detector", fg = "purple").grid(row = 0,column = 2)

def open_file():                                        #opening a file
    root.filename = filedialog.askopenfilename(initialdir = r"C:\Users\Lenovo\Desktop\Hermehar\python", title = "Select File to open", filetypes = (("jpeg images","*.jpg"),("png images","*.png")))

def send_report():                                      #storing values of entryfields in a variable and sending message on user's whatsapp            
    name = name_entry_field.get()                      #storing values of entryfields in a variable
    age = age_entry_field.get()                        
    mobile = mobile_entry_field.get()
    pywhatkit.sendwhatmsg_instantly(f'{mobile}', f'This is the report of {name}, age: {age}.The red portion in the image indicates the infection in the brain.')    # sending the message on the whatsapp 
    Report = Label(root, text = f'Report of {name} has been sent to {mobile}', fg = "purple").grid(row = 9, column = 2)
    Thanks = Label(root, text = "Thanks for using the software", fg = "purple").grid(row = 11, column = 2)    

name_entry = Label(root, text = "Enter Your Name").grid(row = 3, column = 1)                           #entry fields
name_entry_field = Entry(root, width = 50, fg = "red")
name_entry_field.grid(row = 3, column = 2)

age_entry = Label(root, text = "Enter Your Age").grid(row = 4, column = 1)
age_entry_field = Entry(root, width = 50, fg = "red")
age_entry_field.grid(row = 4, column = 2)

mobile_entry = Label(root, text = "Enter Your Mobile Number").grid(row = 5, column = 1)
mobile_entry_field = Entry(root, width = 50, fg = "red")
mobile_entry_field.grid(row = 5, column = 2)

l1 = Label(root, text = "Please select a jpeg on png file of your Brain MRI.").grid(row = 7, column = 1)
open_filename_button = Button(root, text = "Select File", command = open_file, fg = "#33FFCA", bg = "black").grid(row = 7, column = 2)

def cancel_button():                                        #cancel nutton to quit the program
    quit()

def submit_button():                                        #defining submit button

    def get_avg(pixel):                                     #getting the average of pixels
        return (pixel.red + pixel.green + pixel.blue) // 3

    def trim_filename(original_filename, trim_size):        #cropping the image
        new_width = original_filename.width - 2 * trim_size
        new_height = original_filename.height - 2 * trim_size
        trimmed_filename = SimpleImage.blank(new_width,new_height)     #added a blank canvas 
        for x in range(new_width):
            for y in range(new_height):
                old_x = x + trim_size
                old_y = y + trim_size
                orig_pixel =original_filename.get_pixel(old_x, old_y)
                trimmed_filename.set_pixel(x,y,orig_pixel)
        return trimmed_filename

    def find_tumour(filename):                             #sufficiently brighter pixels are colored red and rest are colored green
        for pixel in filename:
            pixel_avg = get_avg(pixel)
            if pixel.red >= BRIGHT_THRESHOLD:
                pixel.red = pixel_avg * 3                  #color sufficiently bright pixels with red color 
                pixel.green = 0
                pixel.blue = 0
            else:
                pixel.green = pixel_avg                    #displaying green color 
                pixel.red = 0
                pixel.blue = 0       
        return filename

    def main():                                             #displaying the images
        filename = root.filename
        filename = SimpleImage(filename)
        filename.show()                                    #display original image
        find_tumour_filename = find_tumour(filename)          
        find_tumour_filename.show()                        #display image of brain with tumor 
        trimmed_filename = trim_filename(filename, 40)
        find_tumour_filename = find_tumour(trimmed_filename)
        find_tumour_filename.show()                        #display part of brain with tumor   

    if __name__ == '__main__':
        main()
                                                               #adding three buttons
submit_button = Button(root, text = "Submit", command = submit_button, fg = "#33FFCA", bg = "black").grid(row = 12, column = 1)
cancel_button = Button(root, text =  "Cancel", command = cancel_button, fg = "#33FFCA", bg = "black").grid(row = 12, column = 2)
send_button = Button(root, text = "Send Report on Whatsapp", command = send_report, fg = "#33FFCA", bg = "black").grid(row = 12, column = 3)

root.mainloop()                                              
