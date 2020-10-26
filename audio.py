import pyttsx3
import PyPDF2
book=open("xyz.pdf","rb")
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
speaker =pyttsx3.init()
n=input()
for i in range(7,n):
    page=pdfReader.getPage(7) #from which we can to start reading
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()