# ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═
# Configuracion de librerias
# ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═

import importlib as ilib
import subprocess as sub
import wave as wv

def libSetup(lib):
    # Funcion para instalar automaticamente librerias no existentes
    try:ilib.import_module(lib)
    except ImportError:sub.check_call(['pip', 'install', lib])

libSetup('pyaudio')
import pyaudio as pya

libSetup('numpy')
import numpy as np

libSetup('scipy.signal')
from scipy.signal import find_peaks

libSetup('librosa')
import librosa as libo
import pickle as pk

def is_number_in_array(array, number, offset=5):
    for i in range(number - offset, number + offset + 1):
        if i in array:
            return True
    return False

def detectarSinIA (AUDIO):
    rate, data = wv.read(AUDIO)
    # data is voice signal. its type is list(or numpy array)

    # Calculate Fast Fourier Transform (FFT)
    fft_data = np.fft.fft(data)
    # Find peaks in the magnitude spectrum
    frequencies, _ = find_peaks(np.abs(fft_data), prominence=1000)

    # Combine peak detection with frequency range filtering for robustness
    filtered_frequencies = []
    for freq in frequencies:
        for char, frequency_pair in DTMF_TABLE.items():
            if (freq >= frequency_pair[0] - 50 and  # Lower bound with tolerance
                freq <= frequency_pair[0] + 50 and  # Upper bound with tolerance
                freq >= frequency_pair[1] - 50 and
                freq <= frequency_pair[1] + 50):
                filtered_frequencies.append(freq)
                break  # Exit inner loop if a match is found

    # Detect pressed button (using filtered frequencies)
    for char, frequency_pair in DTMF_TABLE.items():
        if all(is_number_in_array(filtered_frequencies, f) for f in frequency_pair):
            print("Pressed button:", char)
            break  # Exit the loop after finding a match

def detectarConIA(AUDIO):
    """
    # MODELO DE RECONOCIMIENTO CON IA
    IA = 'modelo_knn.pkl'
    # Cargar el audio y extraer características (MFCCs)
    y, sr = libo.load(AUDIO)
    mfccs = libo.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    mfcc_features = np.mean(mfccs, axis=1)

    # Cargar el modelo
    with open(IA, 'rb') as f:
        knn = pk.load(f)

    # Cargar un nuevo archivo de audio
    y, sr = libo.load(AUDIO)
    mfccs = libo.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    mfcc_features = np.mean(mfccs, axis=1)

    # Hacer una predicción
    prediction = knn.predict([mfcc_features])
    print("Predicción:", prediction)
    """

# Configuración del audio
CHUNK = 1024
FORMAT = pya.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 1
AUDIO = 'output.wav'

DTMF_TABLE = {
    '1': [1209, 697],   '2': [1336, 697],   '3': [1477, 697],   'A': [1633, 697],
    '4': [1209, 770],   '5': [1336, 770],   '6': [1477, 770],   'B': [1633, 770],
    '7': [1209, 852],   '8': [1336, 852],   '9': [1477, 852],   'C': [1633, 852],
    '*': [1209, 941],   '0': [1336, 941],   '#': [1477, 941],   'D': [1633, 941],
} 

# Inicializar PyAudio
p = pya.PyAudio()

# Escuchando...
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Inicio de Grabacion
print("Grabando...")
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print("Grabación finalizada.")

# Stop and close the stream
stream.stop_stream()
stream.close()

# Cargando datos de la grabacion
wf = wv.open(AUDIO, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

# Call the function to start the DTMF detection
detectarSinIA()

p.terminate()