# Import essential library
import pyttsx3
import PyPDF2

# Open the PDF file and initialize the PDF reader
book = open('oop.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)
print(pages)

# Initialize the text-to-speech engine
# On linux, use 'espeak' or 'espeak-ng';
# On macOS, use 'nsss';
# On Windows, use 'sapi5'.
speaker = pyttsx3.init(driverName='espeak')

# Configure speech settings for smoother reading
rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate - 80)  # Adjust the value as needed speed
speaker.setProperty('volume', 0.1)  # Adjust volume (0.0 to 1.0)

# Iterate through all the pages and read their content
for num in range(pages):
    bookPage = pdfReader.pages[num]
    text = bookPage.extract_text()
    speaker.say(text)
    speaker.runAndWait()

# Close the PDF file and cleanup the text-to-speech engine
book.close()
speaker.stop()
