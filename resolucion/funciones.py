import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import soundfile as sf 
import sounddevice as sd
from time import localtime, strftime

def ruidoRosa_voss(t, ncols=16, fs=44100): ## Explorar otros valores de ncols, ej:4 o 32.
    """
    Genera ruido rosa utilizando el algoritmo de Voss-McCartney (https://www.dsprelated.com/showabstract/3933.php).
    
    .. Nota:: si 'ruido_rosa.wav' existe, este será sobreescrito.
    
    Parametros
    ----------
    t : float
        Valor temporal en segundos, este determina la duración del ruido generado.
    ncols: int
        Determina el número de fuentes a aleatorias a agregar.
    fs: int
        Frecuencia de muestreo en Hz de la señal. Por defecto el valor es 44100 Hz.
    
    Returns: NumPy array
        Datos de la señal generada.
    
    Ejemplo
    -------
    Generar un `.wav` desde un numpy array de 10 segundos con ruido rosa a una 
    frecuencia de muestreo de 44100 Hz.
    
        import numpy as np
        import pandas as pd
        import soundfile as sf
        
        ruidoRosa_voss(10)
    """
    # Cálculo de cantidad de muestras
    cant_muestras = fs*t
    nrows = cant_muestras

    # Cálculo de arrays
    array = np.full((nrows, ncols), np.nan)
    array[0, :] = np.random.random(ncols)
    array[:, 0] = np.random.random(nrows)

    # El número total de cambios es nrows
    n = nrows
    cols = np.random.geometric(0.5, n)
    cols[cols >= ncols] = 0
    rows = np.random.randint(nrows, size=n)
    array[rows, cols] = np.random.random(n)

    df = pd.DataFrame(array)
    filled = df.fillna(method='ffill', axis=0)
    total = filled.sum(axis=1)

    # Centrado del array en 0
    total = total - total.mean()

    # Normalizado
    valor_max = max(abs(max(total)), abs(min(total)))
    total = total / valor_max

    # Generación de archivo de audio .wav
    sf.write('ruido_rosa.wav', total, fs)

    return total

def grafico_señal(data,fs=44100,title=None):
    """
    Grafica el dominio temporal de una señal.
    
    Parametros
    ----------
    data : array
        Array de amplitud de la señal a graficar.
    fs: int
        Frecuencia de muestreo en Hz de la señal. Por defecto el valor es 44100 Hz.
    title:
        Título del gráfico. Por defecto no tiene.

    Returns: Gráfico de la señal.

    Ejemplo
    -------
    Generar un gráfico desde una señal de ruido rosa a una 
    frecuencia de muestreo de 44100 Hz.
    
        import numpy as np
        import matplotlib.pyplot as plt
        
        grafico_señal(ruido_rosa)
    """

    # Eje x: tiempo
    x = np.arange(0,len(data)/fs,1/fs)
    plt.xlabel('Tiempo [s]')
    
    # Eje y: amplitud normalizada
    y = data
    plt.ylabel('Amplitud')
    
    plt.title(title)
    plt.plot(x,y)
    
    return plt.show()

def ss_fi(T,f1,f2,fs=44100):
    """
    Genera un Sine Sweep y su filtro inverso utilizando las ecuaciones de Meng, Q.

    .. Nota:: si 'sine_sweep.wav' y/o 'filtro_inverso.wav' existen, serán sobreescritos.
    
    Parametros
    ----------
    T : int
        Valor temporal en segundos, este determina la duración del audio generado.
    f1: int
        Frencuancia inferior en Hz.
    f2: int
        Frencuancia superior en Hz.
    fs: int
        Frecuencia de muestreo en Hz de la señal. Por defecto el valor es 44100 Hz.
    
    Returns: NumPy array
        Datos de las señales generadas.
    
    Ejemplo
    -------
    Generar dos `.wav` desde un numpy array de 10 segundos con sine sweep y su filtro inverso a una 
    frecuencia de muestreo de 44100 Hz.
    
        import numpy as np
        import math
        import soundfile as sf
        
        ss_fi(10,20,20000)
    """

    # Definición del sine sweep
    w1 = 2*math.pi*f1
    w2 = 2*math.pi*f2
    R = np.log(w2/w1)
    K = (T*w1)/R
    L = T/R
    t = np.arange(0,T,1/fs)

    sine_sweep = np.sin(K*((np.exp(t/L))-1))

    # Definición del filtro inverso
    w = (K/L)*(math.e**(t/L))
    m = w1/(2*math.pi*w)
    t2 = np.flip(t)
    ss2 = np.sin(K*((np.exp(t2/L))-1))

    filtro_inverso = m*ss2

    # Generación de archivos de audio .wav
    sf.write('sine_sweep.wav', sine_sweep, fs)
    sf.write('filtro_inverso.wav',filtro_inverso, fs)

    return sine_sweep, filtro_inverso

def play_rec(filename, duration=None, end_delay=None, play_device_id=None, rec_device_id=None):
    """
    Reproduce un audio seleccionado y graba simultáneamente, según los dispositivos de audio elegidos. La grabación será guaradada en un archivo con el nombre 'recording' seguido de la fecha y hora local.

    Parametros
    ----------
    filename : str
        Nombre del archivo de audio a reproducir.
    duration(opcional): int
        Duración de la reproducción y adquisición, en segundos. Si no se elige una duración, la duración por defecto de la grabación y reproducción será igual a la duración del audio a reproducir.
    end_delay(opcional): int
        Delay en segundos, entre que se detiene la reproducción del audio y se termina la grabación. Si no se elige un tiempo de delay, la grabación terminará al mismo tiempo que se termine de reproducir el audio.
    play_device_id(opcional): int
        Número de ID del dispositivo de audio elegido para reproducir. Si no se indica en el argumento de la función, será solicitado al momento de correr la misma.
    rec_device_id(opcional): int
        Número de ID del dispositivo de audio elegido para grabar. Si no se indica en el argumento de la función, será solicitado al momento de correr la misma.

    .. Nota:: Si la duración elegida es mayor que el tiempo del audio a reproducir, el audio terminará de reproducirse y la función seguirá grabando hasta el tiempo indicado. Si la duración elegida es menor a la duración del audio a reproducir, la reproducción y la grabación se detendrán en el tiempo indicado.

    Returns: NumPy array
        Datos del audio grabado.
    """

    # Ingresar nombre del archivo de audio a reproducir
    if filename == False:
        filename = input('Ingrese el nombre del archivo de audio .wav a reproducir: ') + '.wav'

    # Extraer datos del archivo de audio
    playdata, fs = sf.read(filename, dtype='float32')
    print('Playdata type = ' + str(type(playdata)))
    play_samples = int(len(playdata))  # Cantidad de muestras del archivo de audio cargado
    print('Play samples = ' + str(play_samples))
    play_time = play_samples/fs  # Duración original del archivo de audio cargado

    # Definir duración de la función
    duration_samples = int(duration * fs)  # Cantidad de muestras necesarias para la duración requerida
    print('Duration samples = ' + str(duration_samples))
    print('Duration samples type = ' + str(type(duration_samples)))
    end_delay_samples = int(end_delay * fs)  # Cantidad de muestras necesarias para el delay requerido
    print('End_delay samples = ' + str(end_delay_samples))
    end_delay_array = np.zeros(end_delay_samples)
    print('End delay array = ' + str(type(end_delay_array)))
    if duration < play_time and end_delay == None:
        playdata = playdata[:duration_samples]
    elif duration < play_time and end_delay != None:
        playdata = np.concatenate([playdata[:duration_samples], end_delay_array])
    elif duration > play_time and end_delay == None:
        playdata = np.concatenate([playdata, np.zeros(duration_samples - play_samples)])
    elif duration > play_time and end_delay != None:
        playdata = np.concatenate([playdata, np.zeros(duration_samples - play_samples), end_delay_array])

    # Elegir dispositivo de reproducción y grabación
    if play_device_id or rec_device_id == None:
        print('Listado de dispositivos de audio disponibles:\n')
        print(sd.query_devices())

    if play_device_id == None:
        play_device_id = int(
            input('Ingrese el número de la lista del dispositivo que desea utilizar para reproducir: '))

    if rec_device_id == None:
        rec_device_id = int(input('Ingrese el número de la lista del dispositivo que desea utilizar para grabar: '))

    # Establcer valores por defecto de la función
    sd.default.samplerate = fs
    sd.default.device = rec_device_id, play_device_id
    sd.default.channels = 2
    if duration == None:
        duration = playdata/fs

    # Reproducción y adquisición
    recording = sd.playrec(playdata)
    sd.wait()
    fecha_hora = strftime('%Y-%m-%d   %Hh-%Mm-%Ss', localtime())
    sf.write('recording ' + fecha_hora + '.wav', recording, fs)

    return recording, duration, end_delay