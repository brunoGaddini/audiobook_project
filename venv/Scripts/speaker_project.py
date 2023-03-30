# Importing libraries
import pyttsx3
import pdfplumber as pb

# Initializing the engine
engine = pyttsx3.init()

### Extracting texts ###
# Reading the PDF file
pdf = pb.open('O elefante em apuros.pdf')

# Generating the book page list (deleting unnecessary pages)
pages = pdf.pages[2:26]

text_book = ''
for page in pages:
    text_book += page.extract_text()

# Working the text
final_text = text_book.replace('.', '. ').replace(',', ', ')


engine.save_to_file(final_text, 'audiobook.mp3')
engine.runAndWait()