import tkinter
from auth import authenticate


class Send():
    def __init__(self,screen_instance) -> None:
        super().__init__()
        self.screen = screen_instance
        comment = self.screen.inputBox.get("1.0", "end-1c")
        self.youtube = authenticate()
        self.request = self.youtube.commentThreads().insert(
            part="snippet",
            body={
                "snippet": {
                "channelId": "UC18Jkl7X_iAscUgVMKMwK2g",  # Replace with channel ID
                "videoId": "JALbemLw3G4&ab",  # Replace with video ID
                "topLevelComment": {
                    "snippet": {
                        "textOriginal": comment 
                    }
                }
            }
        }
    )
