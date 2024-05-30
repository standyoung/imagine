import requests
import json

# secrets.json 파일에서 데이터 불러오기
with open('../secrets.json', 'r') as file:
    secrets = json.load(file)

# API_KEY 가져오기
API_KEY = secrets['API_KEY']

# AI 모델을 사용할 수 있는 사이트 접근
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"

# 인증 코드 넣기
headers = {"Authorization": f"Bearer {API_KEY}"}

# 인터넷 연결 필요
def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("../media/images/christmas.png")
print(output[0]['generated_text'])

