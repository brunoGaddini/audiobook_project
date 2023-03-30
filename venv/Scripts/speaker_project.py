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