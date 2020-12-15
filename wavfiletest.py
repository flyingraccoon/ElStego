import wave,time
dicts = {}
frames = []
chrs = []
word = 'Hello World!'
w = wave.open(r'\\ops.internal\Users\Students-KS4\2014 Year Group\14JDenham\Project\wav.wav', 'r')
n_channels = w.getnchannels()      # Number of channels. (1=Mono, 2=Stereo).
sample_width = w.getsampwidth()    # Sample width in bytes.
framerate = w.getframerate()       # Frame rate.
n_frames = w.getnframes()          # Number of frames.
comp_type = w.getcomptype()        # Compression type (only supports "NONE").
comp_name = w.getcompname() 
for i in range(w.getnframes()):
        ### read 1 frame and the position will updated ###
        frame = w.readframes(1)
        frames.append(frame)
print('here')
framenum = 0
smallframenum = 0
for frame in frames:
    smallframenum = 0
    for smallframe in frame:
        chrs.append((chr(smallframe),framenum,smallframenum))
        smallframenum +=1
    framenum+=1    
print('here2')
for letter in word:
    for pos in chrs:
        if pos[0] == letter:
            print(pos)
            break
print(frames)
with wave.open(r'\\ops.internal\Users\Students-KS4\2014 Year Group\14JDenham\Project\outwav.wav', 'wb') as wav_file:
    params = (n_channels, sample_width, framerate, n_frames, comp_type, comp_name)
    wav_file.setparams(params)
    wav_file.writeframes(b''.join(frames))
