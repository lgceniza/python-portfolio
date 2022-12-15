from tkinter import *
from tkinter.filedialog import askopenfile
from PIL import ImageTk, Image

FILENAME_FONT = ('Calibri', 10, 'italic')
# CANVAS = {'.!label2': 'bg_file', '.!label4': 'watermark_file'}

# TODO: display uploaded image into canvas
# TODO: perform watermarking overlay
# TODO: download finished image

def open_file(label : Label):
  file_path = askopenfile(mode='r', filetypes=[('Image Files', ['*jpg', ['*jpeg', '*png']])])
  if file_path is not None:
    label.config(text=file_path.name.split('/')[-1])

    # paste img into canvas
    # image_img = ImageTk.PhotoImage(Image.open(file_path.name))
    # canvas_image = canvas.create_image(20,20,image=image_img)

def mode_changed(mode):
  if mode.get():
    logo_upload_btn.grid(row=1, column=3)
    logo_upload_filename_label.grid(row=1, column=4, columnspan=2)
    text_watermark_entry.grid_remove()
    image_upload_label.config(width=27)
    watermark_upload_label.config(width=18)
  else:
    image_upload_label.config(width=30)
    watermark_upload_label.config(width=30)
    logo_upload_btn.grid_remove()
    logo_upload_filename_label.grid_remove()
    text_watermark_entry.grid()


window = Tk()
window.title('hello')
window.config(width=600, height=500, padx=20, pady=20)

image_upload_label = Label(text="Upload an image to watermark:", anchor=W, width=30)
image_upload_btn = Button(text="Choose File", command=lambda: open_file(image_upload_filename_label))
image_upload_filename_label = Label(text="No file selected.", font=FILENAME_FONT, fg='grey', anchor=W, width=20)
watermark_upload_label = Label(text="Select your watermark:", anchor=W, width=30)
logo_upload_btn = Button(text="Choose File", command=lambda: open_file(logo_upload_filename_label))
logo_upload_filename_label = Label(text="No file selected.", font=FILENAME_FONT, fg='grey', anchor=W, width=20)
text_watermark_entry = Entry(width=20)
text_watermark_entry.insert(0, 'Text watermark here')
watermark_mode = BooleanVar()
option = Checkbutton(text="Image", variable=watermark_mode, onvalue=True, offvalue=False, command=lambda: mode_changed(watermark_mode))

image_upload_label.grid(row=0, column=0, columnspan=3)
image_upload_btn.grid(row=1, column=0)
image_upload_filename_label.grid(row=1, column=1, columnspan=2)
watermark_upload_label.grid(row=0, column=3, padx=10, columnspan=2)
option.grid(row=0, column=5, padx=10)
text_watermark_entry.grid(row=1, column=3, padx=10)

canvas = Canvas()
canvas.grid(row=2, column=0, columnspan=6)

window.mainloop()
