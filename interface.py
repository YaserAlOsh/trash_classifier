from tkinter import Tk, Label, Canvas, Button, Frame
from threading import Thread
import time as t

SIZE = 16
COLOR = "white"


class Interface:

    def __init__(self, rpi):
        self.rpi = rpi
        self.stream = Tk()
        self.stream.attributes('-fullscreen', True)
        self.stream.title("Trash Classifier System")
        self.stream.minsize(width=300, height=400)
        self.display_first_layout()
        self.stream.mainloop()
        self.waiting = False

    # this function for displaying the loading page after the capture button has been clicked
    def display_loading_layout(self):
        self.clear_frame()
        self.stream.update()
        self.waiting = True
        loading = Label(text="Classifying...", font=(COLOR, SIZE))
        loading.place(x=self.stream.winfo_width() * 0.45, y=self.stream.winfo_height() * 0.4)

        for i in range(16):
            Label(self.stream, bg="#525252", width=2, height=1).place(x=(i + 23) * 23,
                                                                      y=self.stream.winfo_height() * 0.45)

#         self.stream.update()
        self.play_animation()

    # this function will play the animation of the bar in the loading layout
    def play_animation(self):
        i = 0
        while (i < 1) or self.waiting:
            for j in range(16):
                # make block red:
                Label(self.stream, bg="#FF2E2E", width=2, height=1).place(x=(j + 23) * 23,
                                                                          y=self.stream.winfo_height() * 0.45)
                t.sleep(0.06)
                self.stream.update_idletasks()
                # make block gray:
                Label(self.stream, bg="#525252", width=2, height=1).place(x=(j + 23) * 23,
                                                                          y=self.stream.winfo_height() * 0.45)
                i += 1

        self.show_final_layout()

    # this function is for deleting all the widgets inside the window(which is the stream object in our case)
    # before moving to the next layout
    def clear_frame(self):
        for widgets in self.stream.winfo_children():
            widgets.destroy()

    # this function will display the classification results after the item has been classified using the model
    # it will display the name of the category and the percentage
    def display_classification_results(self, dict):
        self.waiting = False
        self.dict = dict

    def display_results(self, category, percentage):
        category_displayed = Label(text=f"Item category is {category}", font=(COLOR, SIZE))
        category_displayed.place(x=self.stream.winfo_width() * 0.40, y=self.stream.winfo_height() * 0.35)
        percentage_displayed = Label(text=f"Percentage = {percentage}%", font=(COLOR, SIZE))
        percentage_displayed.place(x=self.stream.winfo_width() * 0.40, y=self.stream.winfo_height() * 0.42)

    def show_final_layout(self):
        self.clear_frame()

        if self.dict.get('General') == True:
            category_displayed = Label(text=f"Item category is General", font=(COLOR, SIZE))
            category_displayed.place(x=self.stream.winfo_width() * 0.40, y=self.stream.winfo_height() * 0.35)
            percentage_displayed = Label(text=f"This category can't be classified", font=(COLOR, SIZE))
            percentage_displayed.place(x=self.stream.winfo_width() * 0.40, y=self.stream.winfo_height() * 0.42)

        else:
            max_value = max(self.dict.values())

            if self.dict.get('Plastic') == max_value:
                self.display_results('Plastic', "%.5f" % max_value)
            elif self.dict.get('Metal') == max_value:
                self.display_results('Metal', "%.5f" % max_value)
            elif self.dict.get('Paper') == max_value:
                self.display_results('Paper', "%.5f" % max_value)

        # buttons
        retaking_button = Button(text="Retake Photo", command=self.display_first_layout)
        retaking_button.place(x=self.stream.winfo_width() * 0.35, y=self.stream.winfo_height() * 0.5)
        exit_button = Button(text="Exit", command=self.stream.destroy)
        exit_button.place(x=self.stream.winfo_width() * 0.50, y=self.stream.winfo_height() * 0.5)

    # this function will call the classify function in the rpi class, which will stop the camera from streaming
    # after the 'Capture' button has been clicked on. Also, it will call the display loading layout function
    # to display the loading layout
    def call_classify_and_loading(self):
        self.waiting = True
        loading_thread = Thread(target=self.display_loading_layout, name="Loading")
        loading_thread.start()
        #self.stream.after(4000, self.create_temp_func,{'Metal': 0.99232, 'Plastic': 100.00, 'Paper': 0.23132, 'General': False})
        self.rpi.trigger_camera()

    def exit(self):
        self.rpi.stop_stream()
        self.stream.destroy()

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

        self.stream.update()
        # the width of camera_steam should be
        camera_stream = Canvas(self.stream, width=self.stream.winfo_width(), height=self.stream.winfo_height() * 0.9)
        camera_stream.grid(row=2, column=2)
        camera_stream.create_rectangle(0, 20, self.stream.winfo_width(), self.stream.winfo_height() * 0.9, fill="black")

        # this function is for playing a real-live stream
        self.rpi.make_stream()
        # here where the two buttons "Capture" and "Exit" will be inside this frame to align with each other
        f = Frame(self.stream)
        f.grid(row=3, column=2)
        capture_button = Button(f, text="Capture", command=self.call_classify_and_loading)
        capture_button.pack(side="left")
        exit_button = Button(f, text="Exit", command=self.exit)
        exit_button.pack(side="right")


# def classify():
#     pass
#
#
# interface = Interface(None, quit, classify)
