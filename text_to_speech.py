import playsound
url2 = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/9f36a3b4-0dab-4244-8c45-a8efcac3c5a2'
apikey2 = 'EJ3oIt0uZf-Ex_zx5LIADf8tVfRlIOUhEbbyhLuIyjw0'

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(apikey2)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url2)



with open('outputss.txt', 'r') as f:
     text = f.readlines()

     text = [line.replace('\n','') for line in text]

     text = ''.join(str(line) for line in text)

with open('tts.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-GB_JamesV3Voice').get_result()
    audio_file.write(res.content)


playsound.playsound('tts.mp3')


