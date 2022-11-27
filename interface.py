from guizero import App, Text,PushButton, Picture, Drawing

class Interface:
    app = None
    def __init__(self,rpi,exit_app,classify,title):
        self.rpi = rpi
        self.app = App(title=title)
        self.app.set_full_screen(keybind='<Escape>')
        message = Text(self.app, text="Welcome to our Points-Based Trash Classifier System Utilizing Deep Learning Techniques.")
        prompt = Text(self.app, text="Please place your trash in front of the camera and click the classify button, you will see the correct category on the screen and the LEDs.")
        prompt2 = Text(self.app,text="Then kindly take your trash and throw it in the correct bin.")
        classify = PushButton(self.app,command=classify,text="Classify")
        classify.bg = "green"

        close = PushButton(self.app,command=exit_app,text="Esc",align="bottom")
        close.bg = 'red'
        self.img_preview = Drawing(self.app)
        self.img_preview.rectangle(10,10,300,300)
        #self.img_preview.rectangle(
    def show_image(self,img_path):
        self.img_preview.image(0,0,img_path,width=480,height=320)
        self.app.display()
    def show(self):
        self.app.display()