import queue
import sounddevice as sd
import vosk
import json
import library_words
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from skills import *

q = queue.Queue()

model = vosk.Model('model_voice')

device = sd.default.device = 0, 2
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])

def callback(indata, frames, time, status):
    
    q.put(bytes(indata))

def recognie(data, vectorizer, clf):
    trigg = library_words.TRIGGERS.intersection(data.split())
    if not trigg:
        return

    data.replace(list(trigg)[0], '')
    text_vector = vectorizer.transform([data]).toarray()[0] 
    answer = clf.predict([text_vector])[0] 
    
    func_name = answer.split()[0]
    speaker(answer.replace(func_name, ''))
    exec(func_name + '()')




def main():
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(library_words.data_set.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(library_words.data_set.values()))

    del library_words.data_set

    with sd.RawInputStream(samplerate=samplerate, blocksize = 14000, device=device[0], dtype="int16", channels=1, callback=callback):
            
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                recognie(data, vectorizer, clf)

if __name__ == '__main__':
    main()           
