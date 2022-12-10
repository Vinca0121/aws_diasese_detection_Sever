from flask import Flask, request
from werkzeug.utils import secure_filename
# import os
# import ctypes
import subprocess




#Flask 인스턴스 생성
app = Flask(__name__)

# GET
@app.route('/data',methods = ['GET'])
def get():
    print("get 수행됨")
    # MongoDB 연결하는 부분

    # 마지막 image 데이터 가져오는 부분
    
    # 가져온 이미지 데이터를 서버에 저장하는 부분
    
    # 서버에 저장된 이미지 데이터를 darknet - YoloV4를 사용해서 검출
    
    # 결과 json을 파싱해서 저장하는 부분    
    subprocess.call(["./darknet detector test yolofiles/obj.data yolofiles/yolov4.cfg yolofiles/yolov4_4000.weights yolofiles/plants1.jpg -out prediction.json -dont_show"], cwd="/home/ubuntu/darknet")
    

    subprocess.call(["ls"], cwd="/home/ubuntu/darknet")
    return "this is get test"


# # POST 
# @app.route('/image', methods=['POST'])
# def upload_file():
#     print("post 수행됨")
#     f = request.files['file']	#이미지 파일 받기
#     # 저장할 경로 + 파일명
#     f.save("./save/"+secure_filename(f.filename))
        
#     # 이미지를 받아 YOLO 모델을 수행하는 코드(json 저장)
#     # https://asecurity.dev/entry/Python-subprocess-Popen-call%EC%B0%A8%EC%9D%B4-%EA%B7%B8%EB%A6%AC%EA%B3%A0-WorkDirectory-%EB%B3%80%EA%B2%BD
#     subprocess.call(["ls"], cwd="/home/ubuntu/darknet")
#     # DB에 Json파일을 파싱하여 저장하는 코드
    
        
#     # 클라이언트로 다시 이미지를 return하는 코드
#     #files = open('./save/bird.jpg', 'rb')
#     #upload = {'file': files}
#     #return upload

#     return "detected Image return"

#서버 실행
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    #app.run(debug=True)
