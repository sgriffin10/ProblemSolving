from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

def PDFmerge(pdfs, output):  
    # creating pdf file merger object 
    pdfMerger = PdfFileMerger() 
      
    # appending pdfs one by one 
    for pdf in pdfs: 
        with open(pdf, 'rb') as f: 
            pdfMerger.append(f) 
          
    # writing combined pdf to output pdf file 
    with open(output, 'wb') as f: 
        pdfMerger.write(f) 
  
def main(): 
    # pdf files to merge 
    pdfs = ["Classwork/Session 12/Session1CourseIntroduction.pdf", "Classwork/Session 12/Session2.pdf","Desktop/Session 4 - Competition & Markets.pdf"]

#'Session 4 - Competition & Markets.pdf','Session 5 - Resources and Capabilities.pdf','Session 6 - Corporate Strategy and Internal Ecosystems.pdf','Session 7 - Business Models.pdf','Session 8 - External Ecosystems and Multi-sided Markets.pdf','Session 9 - Corporate Social Responsibility.pdf','Session 10 - Globalization.pdf','Session 11 - Implementation and Talent Management.pdf','Session 12 - Business Writing.pdf' 
     
    # output pdf file name 
    output  = 'combinedasmmaterials.pdf'
      
    # calling pdf merge function 
    PDFmerge(pdfs = pdfs, output = output) 
  
if __name__ == "__main__": 
    # calling the main function 
    main() 