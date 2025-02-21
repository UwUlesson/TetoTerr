import tkinter
from window_general import windows
import vlc



class screen(windows):

    def __init__(self):
        super().__init__()
        self.player = vlc.MediaPlayer()
        # canvas
        self.canvas = tkinter.Canvas(self.window, width=300, height=225)
        self.canvas.grid(row=0, column=3)
        self.play_video()
        # input
        self.inputBox = tkinter.Text(self.window,width=120,height=28)
        self.inputBox.grid(row=1, column=1)
        # button
        button = tkinter.Button(self.window,text="_post_",command=self.post)
        button.grid(row=2,column=3)


    def play_video(self):
        video_path = "video.mp4"
        media = vlc.Media(video_path)
        self.player.set_media(media)
        self.player.set_xwindow(self.canvas.winfo_id())
        self.player.audio_set_volume(50)
        self.player.play()

    def post(self):
        from SendYou import Send
        send_ins = Send(self)
        request = send_ins.request
        request.execute()
        self.window.destroy()

window = screen()
window.show()
