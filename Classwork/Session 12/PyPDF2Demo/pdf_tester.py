from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

def PDFmerge(pdfs, output):  
    # creating pdf file merger object 
    pdfMerger = PdfFileMerger() 
      
    # appending pdfs one by one 
    for pdf in pdfs: 
            pdfMerger.append(pdf) 
          
    # writing combined pdf to output pdf file 
    with open(output, 'wb') as f: 
        pdfMerger.write(f) 
  
def main(): 
    # pdf files to merge 
    pdfs = ["Classwork/Session 12/Session1.pdf", "Classwork/Session 12/Session2.pdf","Classwork/Session 12/Session3.pdf","Classwork/Session 12/Session4.pdf","Classwork/Session 12/Session5.pdf","Classwork/Session 12/Session6.pdf","Classwork/Session 12/Session7.pdf","Classwork/Session 12/Session8.pdf","Classwork/Session 12/Session9.pdf","Classwork/Session 12/Session10.pdf","Classwork/Session 12/Session11.pdf","Classwork/Session 12/Session12.pdf"]
     
    # output pdf file name 
    output  = 'combinedasmmaterials.pdf'
      
    # calling pdf merge function 
    PDFmerge(pdfs = pdfs, output = output) 
  
if __name__ == "__main__": 
    # calling the main function 
    main() 
