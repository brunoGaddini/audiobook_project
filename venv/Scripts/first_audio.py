import pyttsx3

engine = pyttsx3.init() # starting the pyttsx3
engine.setProperty("voice", "brazil") # Configuring the voice pattern

engine.say('Meu nome é Bruno')
engine.runAndWait()

engine.save_to_file('Meu nome é Bruno', 'nome_Bruno.mp3')
engine.runAndWait()
