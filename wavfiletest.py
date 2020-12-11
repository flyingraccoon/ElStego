import wave
dicts = {}
frames = []
word = 'Hello World!'
w = wave.open(r'\\ops.internal\Users\Students-KS4\2014 Year Group\14JDenham\Project\wav.wav', 'r')
for letter in word:
    for i in range(w.getnframes()):
        ### read 1 frame and the position will updated ###
        frame = w.readframes(1)
            
        for j in range(len(frame)):
            if frame[j] == ord(letter):
                dicts[chr(frame[j])] = (i,j)
print(dicts)
#dicts = dict(sorted(dicts.items(), key=lambda item: item[1]))
import matplotlib.pyplot as plt
#print(dicts)
'''
plt.bar(range(len(dicts)), list(dicts.values()), align='center')
plt.xticks(range(len(dicts)), list(dicts.keys()))

plt.show()
'''