from tkinter import Tk, Label, Canvas, Button, Frame
import time as t

SIZE = 16
COLOR = "white"


class Interface:

    def __init__(self, rpi, exit_screen, classifying):
        self.rpi = rpi
        self.classify_obj = classifying
        self.stream = Tk()
        self.stream.attributes('-fullscreen', True)
        self.stream.title("Trash Classifier System")
        self.stream.minsize(width=300, height=400)
        self.display_first_layout()
        self.stream.mainloop()

    # this function for displaying the loading page after the capture button has been clicked
    def display_loading_layout(self):
        self.clear_frame()
        loading = Label(text="Capturing...", font=(COLOR, SIZE))
        loading.place(x=200, y=160)

        for i in range(16):
            Label(self.stream, bg="#525252", width=2, height=1).place(x=(i + 12) * 12, y=200)

        self.stream.update()
        self.play_animation()

    # this function will play the animation of the bar in the loading layout
    def play_animation(self):
        for i in range(3):
            for j in range(16):
                # make block red:
                Label(self.stream, bg="#FF2E2E", width=2, height=1).place(x=(j + 12) * 12, y=200)
                t.sleep(0.06)
                self.stream.update_idletasks()
                # make block gray:
                Label(self.stream, bg="#525252", width=2, height=1).place(x=(j + 12) * 12, y=200)
        else:
            self.display_classification_results("Osama", "0.0001")

    # this function is for deleting all the widgets inside the window(which is the stream object in our case)
    # before moving to the next layout
    def clear_frame(self):
        for widgets in self.stream.winfo_children():
            widgets.destroy()

    # this function will display the classification results after the item has been classified using the model
    # it will display the name of the category and the percentage
    def display_classification_results(self, category_name, percentage_of_category):
        self.clear_frame()
        category = Label(text=f"Item category is {category_name}", font=(COLOR, SIZE))
        category.place(x=150, y=150)
        percentage = Label(text=f"Percentage = {percentage_of_category}%", font=(COLOR, SIZE))
        percentage.place(x=150, y=180)
        retaking_button = Button(text="Retake Photo", command=self.display_first_layout)
        retaking_button.place(x=150, y=210)
        exit_button = Button(text="Exit", command=self.stream.destroy)
        exit_button.place(x=270, y=210)

    # this function will call the classify function in the rpi class, which will stop the camera from streaming
    # after the 'Capture' button has been clicked on. Also, it will call the display loading layout function
    # to display the loading layout
    def call_classify_and_loading(self):
        self.rpi.classify()
        self.display_loading_layout()

    # this function is for displaying the first layout when you run the code.
    # It will display some text at the top, display the camera streaming in its required position,
    # and two buttons at the bottom one for capturing the photo and the other for stopping the program
    def display_first_layout(self):
        self.clear_frame()
        welcome = Label(text="Welcome to our Trash Classifier System",
                        font=(COLOR, SIZE))
        welcome.grid(row=0, column=2)
        prompt = Label(text="Click on the Capture button to classify the trash", font=(COLOR, SIZE))
        prompt.grid(row=1, column=2)
        camera_stream = Canvas(self.stream, width=500, height=350)
        camera_stream.grid(row=2, column=2)
        camera_stream.create_rectangle(0, 20, 600, 600, fill="black")
        # this function is for playing a real-live stream
        self.rpi.make_stream()
        # here where the two buttons "Capture" and "Exit" will be inside this frame to align with each other
        f = Frame(self.stream)
        f.grid(row=3, column=2)
        capture_button = Button(f, text="Capture", command=self.call_classify_and_loading)
        capture_button.pack(side="left")
        exit_button = Button(f, text="Exit", command=self.stream.destroy)
        exit_button.pack(side="right")


# def classify():
#     pass
#
#
# interface = Interface(None, quit, classify)
