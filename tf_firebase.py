from firebase_admin import db

# tf_yolo로 부터 데이터 전달을 위해 import
import tf_yolo

import firebase_admin
from firebase_admin import credentials

# Firebase Database 인증 및 앱 초기화
cred = credentials.Certificate("projecttaver-firebase-adminsdk-dagdm-4ae54d28ee.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://projecttaver-default-rtdb.firebaseio.com/'})

dir = db.reference('매장')


def register_firebase(allTable : int, cafeName : str, latitude :float, longitude :float , peopleNum:int):
    code = "1"
    while True:
        dir = db.reference('매장/' + code)

        if dir.get() != None:
            code = int(code) + 1
            code = str(code)
        else:
            dir.update({'allTable': allTable,
                        'cafeName': cafeName,
                        'latitude': latitude,
                        'longitude': longitude,
                        'peopleNum': peopleNum
                        })
            break
    return code

def update_firebase(code, saturation):
    dir = db.reference('매장/' + code)
    saturation_instance = dir.child('allTable').get() - saturation
    dir.update({'peopleNum': saturation_instance})

