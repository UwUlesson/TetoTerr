from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from window_general import *

class authenticate():
    def __init__(self):
        self.credentials = None



    def authenticate_user(self):
        #conexion por la documentacion auth install, se uso force ssl porque pues queremos escribir comentarios lol

        if self.credentials is not None:
            self.youtube_service = build("youtube", "v3", credentials=self.credentials)
            self.window.destroy()
            self.exeScreen()
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret.json',
            scopes=["https://www.googleapis.com/auth/youtube.force-ssl"])

        # Creacion del servidor local para la autenticación
        self.credentials = flow.run_local_server(host='localhost',
                        port=8080, 
                        success_message='Everything seems fine!, you can go ☆*:.｡.o(≧▽≦)o.｡.:*☆ (please close this site on your way out)',
                        open_browser=True)

        # Construcción del servicio de YouTube usando las credenciales obtenidas
        self.youtube_service = build("youtube", "v3", credentials=self.credentials)

        if self.youtube_service is None:
            raise RuntimeError("YouTube service could not be initialized.")

    
    # execucion de la otra ventana
    def exeScreen(self):
        from initial_screen import start
        open = start()
        open.screen()



