#-----------------------------------------------------------------------------
                                                            
from tkinter import *                                       #importing files
from tkinter import filedialog
from PIL import Image, ImageTk 
from os import system, name
from simpleimage import SimpleImage
import Brain

#-------------------------------------------------------------------------------

BRIGHT_THRESHOLD = 200                                      #bright threshold to find sufficiently brighter pixels
DEFAULT_FILE = 'mri1.jpg'                                   #default file to open

#-------------------------------------------------------------------------------

root = Tk()                                                 #giving title and heading
root.title("Brain Tuomor Detector")
label = Label(root, text = "Brain Tuomor Detector", fg = "purple").grid(row = 0,column = 2)

#---------------------------------------------------------------------------------

name_entry = Label(root, text = "Enter Your Name").grid(row = 3, column = 1)                           #entry fields
name_entry_field = Entry(root, width = 50, fg = "red").grid(row = 3, column = 2)
age_entry = Label(root, text = "Enter Your Age").grid(row = 5, column = 1)
age_entry_field = Entry(root, width = 50, fg = "red").grid(row = 5, column = 2)

#---------------------------------------------------------------------------------

def submit_button():                                        #defining submit button
   
    def open_file():                                        #opening a file
        new.filename = filedialog.askopenfilename(initialdir = r"C:\Users\Lenovo\Desktop\Hermehar\python", title = "Select File to open", filetypes = (("jpeg images","*.jpg"),("png images","*.png")))

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

        def find_tumour(filename):                              #sufficiently brighter pixels are colored red and rest are colored green
            for pixel in filename:
                pixel_avg = get_avg(pixel)
                if pixel.red >= BRIGHT_THRESHOLD:
                    pixel.red = pixel_avg * 3                    #color sufficiently bright pixels with red color 
                    pixel.green = 0
                    pixel.blue = 0
                else:
                    pixel.green = pixel_avg                      #displaying green color 
                    pixel.red = 0
                    pixel.blue = 0
            return filename

        def main():                                             #displaying the images
        
            filename = new.filename
            filename = SimpleImage(filename)
            filename.show()                                    #display original image
            find_tumour_filename = find_tumour(filename)          
            find_tumour_filename.show()                        #display image of brain with tumor 
            trimmed_filename = trim_filename(filename, 40)
            find_tumour_filename = find_tumour(trimmed_filename)
            find_tumour_filename.show()                                #display part of brain with tumor

        if __name__ == '__main__':
            main()
    
    new = Toplevel()                                        #opening a new window
    new.title("New window")
    l1 = Label(new, text = "Hi! Please select a jpeg on png file of your Brain MRI.").grid(row = 2)
    open_filename_button = Button(new, text = "Select File", command = open_file, fg = "#33FFCA", bg = "black").grid(row = 4, column = 1)
    quit_button = Button(new, text = "Cancel", command = new.quit(), fg = "#33FFCA", bg = "black").grid(row = 4, column = 2)
    
    new.geometry("450x450")
    new.mainloop()

#----------------------------------------------------------------------------------
#adding two buttons

submit_button = Button(root, text = "Submit", command = submit_button, fg = "#33FFCA", bg = "black").grid(row = 7, column = 1)
cancel_button = Button(root, text =  "Cancel", command = root.quit(), fg = "#33FFCA", bg = "black").grid(row = 7, column = 2)

#------------------------------------------------------------------------------------

root.geometry ("500x500")
root.mainloop()                                              #ending the document