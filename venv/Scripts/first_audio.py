import pyttsx3

engine = pyttsx3.init() # Iniciando o pyttsx3
engine.setProperty("voice", "brazil") # Configurando o pradrão de voz

engine.say('Meu nome é Bruno') # Adicionando comando para a fila
engine.runAndWait() # runAndWait executa tudo que sta na fila

engine.save_to_file('Meu nome é Bruno', 'nome_Bruno.mp3')
engine.runAndWait()