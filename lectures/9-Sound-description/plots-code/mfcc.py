import numpy as np
import matplotlib.pyplot as plt
import essentia.standard as ess

M = 1024
N = 1024
H = 512
fs = 44100
spectrum = ess.Spectrum(size=N)
window = ess.Windowing(size=M, type='hann')
mfcc = ess.MFCC(numberCoefficients = 12)
x = ess.MonoLoader(filename = '../../../sounds/speech-male.wav', sampleRate = fs)()
mfccs = []

for frame in ess.FrameGenerator(x, frameSize=M, hopSize=H, startFromZero=True):          
  mX = spectrum(window(frame))
  mfcc_bands, mfcc_coeffs = mfcc(mX)
  mfccs.append(mfcc_coeffs)            
mfccs = np.array(mfccs)

plt.figure(1, figsize=(9, 7))

frmTime = H*np.arange(mfccs[:,0].size)/float(fs)                             
plt.pcolormesh(np.transpose(mfccs[:,1:]))
plt.xlabel('time (sec)')
plt.ylabel('mel coefficients')
plt.autoscale(tight=True)
plt.savefig('mfcc.png')
plt.show()

