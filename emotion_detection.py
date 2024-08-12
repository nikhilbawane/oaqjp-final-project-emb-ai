import requests

WATSON_BASE_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1'

def emotion_detector(text_to_analyze: str):
    url = WATSON_BASE_URL + '/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = myobj, headers = header)

    return response.text