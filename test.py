from auth import authenticate

auth_instance = authenticate() # Asegúrate de llamar a authenticate_user()
print(auth_instance.youtube_service)