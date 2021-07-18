"""This program helps the user to find out the brain tumor from the brain MRI.
--- This program takes the image from the user and identifies the tumor in it.
--- Tumor is represented in red color.
--- Firstly, the original image is shown,
--- Secondly, the image will be shown, which will mark the sufficiently bright parts of the image 
    with red color indiacting the tumor and rest of the part will be colored with green color indicating 
    that this region does not have any tumor.
--- Further, the image of tumor in the brain will be shown.
--- Lastly, the report of the patient will be sent on his whatsapp. If no traces of infection found, then it will say No traces found, else it will say traces of infections found. 
"""

from tkinter import *                                       #importing files
from tkinter import filedialog
from PIL import Image, ImageTk, ImageSequence  
import PIL
from simpleimage import SimpleImage
import pywhatkit


BRIGHT_THRESHOLD = 200                                      #bright threshold to find sufficiently brighter pixels


root = Tk()                                                 #giving title and heading
root.title("Brain Infection Detector")
label = Label(root, text = "Brain Infection Detector", fg = "purple").grid(row = 0,column = 2)
NAME_ENTRY_FIELD = Entry(root, width = 50, fg = "red")      #storing values of textfields in constants
AGE_ENTRY_FIELD = Entry(root, width = 50, fg = "red")
MOBILE_ENTRY_FIELD = Entry(root, width = 50, fg = "red")


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


def find_tumor(filename):                              #sufficiently brighter pixels are colored red and rest are colored green
        for pixel in filename:
            pixel_avg = get_avg(pixel)
            if pixel.red >= BRIGHT_THRESHOLD:
                pixel.red = pixel_avg * 4                  #color sufficiently bright pixels with red color 
                pixel.green = 0
                pixel.blue = 0
            else:
                pixel.green = 0                   #displaying green color 
                pixel.red = 0
                pixel.blue = 0       
        return filename


def open_file():                                        #opening a file
    root.filename = filedialog.askopenfilename(initialdir = r"C:\Users\Lenovo\Desktop\Hermehar\python", title = "Select File to open", filetypes = (("Jpeg images","*.jpg"),("Png images","*.png"),("All files","*.*")))


def layout():                                           #entry fields
    name_entry = Label(root, text = "Enter Your Name").grid(row = 3, column = 1)                           
    NAME_ENTRY_FIELD.grid(row = 3, column = 2)

    age_entry = Label(root, text = "Enter Your Age").grid(row = 4, column = 1)
    AGE_ENTRY_FIELD.grid(row = 4, column = 2)

    mobile_entry = Label(root, text = "Enter Your Mobile Number").grid(row = 5, column = 1)
    MOBILE_ENTRY_FIELD.grid(row = 5, column = 2)
    
    l1 = Label(root, text = "Please select a jpeg on png file of your Brain MRI.").grid(row = 7, column = 1)

    open_filename_button = Button(root, text = "Select File", command = open_file, fg = "#33FFCA", bg = "black").grid(row = 7, column = 2)


def cancel_button():                                    #cancel nutton to quit the program
    quit()


def submit_button():                                    #defining submit button
    
    def main():                                         #displaying the images and sending the report
        open_layout = layout()        
        filename = root.filename
        filename = SimpleImage(filename)
        filename.show()                                    #display original image
        find_tumor_filename = find_tumor(filename)          
        find_tumor_filename.show()                        #display image of brain with tumor 
        trimmed_filename = trim_filename(filename, 40)
        find_tumor_filename = find_tumor(trimmed_filename)
        find_tumor_filename.show()                        #display part of brain with tumor  
        find_tumor_filename.pil_image.save('tumor_output.jpg')
        
        def send_report():                                      #storing values of entryfields in a variable and sending message on user's whatsapp            
            name = NAME_ENTRY_FIELD.get()                       #storing values of entryfields in a variable
            age = AGE_ENTRY_FIELD.get()                        
            mobile = MOBILE_ENTRY_FIELD.get()
            root.choose_filename = filedialog.askopenfilename(initialdir = r"C:\Users\Lenovo\Desktop\Hermehar\python", title = "Select File to open", filetypes = (("Jpeg images","*.jpg"),("Png images","*.png"),("All files","*.*"))) 
            output_filename = root.choose_filename
            output_filename = SimpleImage(output_filename)
            for pixel in filename:
                if pixel.green == 0:
                    pywhatkit.sendwhatmsg_instantly(f'+919058422269', f'This is the report of {name}, age: {age} . Traces of infection have been found in the sample.The red portion in the image indicates the infection in the brain.')
                else:
                    pywhatkit.sendwhatmsg_instantly(f'+919058422269', f'This is the report of {name}, age: {age} . No Traces of infection have been found in the sample.')

            Report = Label(root, text = f'Report of {name} has been sent to {mobile}', fg = "purple").grid(row = 9, column = 2)
            Thanks = Label(root, text = "Thanks for using the software", fg = "purple").grid(row = 11, column = 2) 
            return send_report
                    
        message = send_report()           #calling a function to send report on whatsapp

    if __name__ == '__main__':
        main()


#adding two buttons                                                       
submit_button = Button(root, text = "Open", command = submit_button, fg = "#33FFCA", bg = "black").grid(row = 12, column = 1)
cancel_button = Button(root, text =  "Close", command = cancel_button, fg = "#33FFCA", bg = "black").grid(row = 12, column = 2)


root.mainloop()                                         #ending the document
