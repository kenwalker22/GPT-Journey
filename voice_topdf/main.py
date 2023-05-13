import PyPDF2
import pyttsx3
speaker = pyttsx3.init()

# Create a PdfReader object
pdfReader = PyPDF2.PdfReader("book1.pdf")

# Get the number of pages in the PDF file
numPages = len(pdfReader.pages)

# Iterate over the pages in the PDF file
for page_num in range(numPages):
    # Get the text from the current page
    text = pdfReader.pages[page_num].extract_text()
    
 # Strip whitespace from the text
    clean_text = text.strip()
    
  # Replace newline characters with spaces
    clean_text = clean_text.replace('\n', ' ')


    # Print the clean text
    print(clean_text)

#name mp3 file whatever you would like
speaker.save_to_file(clean_text, 'story.mp3')
speaker.runAndWait()

speaker.stop()
