import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# opciones de voz / idioma
id1 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-ES_HELENA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0'

# escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():

    # almacenar el recognizer en una variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:
        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print("ya puedes hablar")

        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-ar")

            # prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            # devolver pedido
            return pedido

        # en caso de que no compenda el audio
        except sr.UnknownValueError:
            # prueba de que no comprendio el audio
            print("ops, no entendi")

            # devolver error
            return "sigo esperando"

        # en caso de no resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print("ups, no hay servicio")

            # devolver error
            return "sigo esperando"

        # error inesperado
        except:

            # prueba de que no comprendio el audio
            print("ups, algo ha salido mal")

            # devolver error
            return "sigo esperando"


# ----------------------------------------------------
# función para que el asistente pueda ser escuchado
def hablar(mensaje):
    # encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# informar el día de la semana
def pedir_dia():
    # crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # crear una variable para el dia de semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario con nombre de dias
    calendario = {0:'Lunes',
                  1:'Martes',
                  2:'Miércoles',
                  3:'Jueves',
                  4:'Viernes',
                  5:'Sábado',
                  6:'Domingo'}

    # decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')


# informar que hora es
def pedir_hora():
    # crear una variable; con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'

    # decir la hora
    hablar(hora)

# funcion saludo inicial
def saludo_inicial():
    # crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'


    # decir el saludo
    hablar(f'{momento}, soy Artemisa, tu asistente personal. Por favor, dime en que te puedo ayudar')


# funcion central del asistente
def pedir_cosas():

    # activar saludo inicial
    saludo_inicial()

    #variable de corte
    comenzar = True

    # loop central
    while comenzar:
        # activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Congusto estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando en Wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente: ')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'adiós' in pedido:
            hablar('Me voy a descansar, cualquier cosa me avisas')
            break

pedir_cosas()







