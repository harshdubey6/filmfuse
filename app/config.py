import os
from urllib.parse import quote_plus

username = quote_plus('dubeyharsh320')
password = quote_plus('yY64v4djov5RSQx6')


class Config:
    JWT_ALGORITHM = 'HS256'
    MONGO_URI = f"mongodb+srv://{username}:{password}@cluster0.cgyk1.mongodb.net/MovieDB?retryWrites=true&w=majority"
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB
    API_KEY = 'dd39691a'
    YOUTUBE_API_KEY = 'AIzaSyAHX3vfeBZ51GkPTHV6TWWK4y4NIoPwOxY'
