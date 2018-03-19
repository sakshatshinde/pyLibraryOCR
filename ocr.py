from PIL import Image
import pytesseract
import csv

#we have to specify where the 'tesseract' library is located on our machine
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'


#for making the CSV
with open('data.csv', 'w') as csvfile:
    fieldNames = ['Library Code']
    writer = csv.DictWriter(csvfile, fieldnames = fieldNames)

    writer.writeheader()
        
    

        
    #for reading different files 
    for i in range(6):
        i = str(i)
        inputImage = 'test' + i + '.png'
        dataEntry = pytesseract.image_to_string(Image.open(inputImage))
        print(dataEntry)
        writer.writerow({'Library Code' : dataEntry})
       


