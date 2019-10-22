from PyPDF2 import PdfFileMerger

# pdfs = ["Classwork/Session 12/Session1CourseIntroduction.pdf", "Classwork/Session 12/Session2.pdf","Classwork/Session 12/Session 3 - Industry Analysis (Breakfast Cereal and Five Forces).pdf"]

merger = PdfFileMerger()

merger.append("Classwork/Session 12/Session1CourseIntroduction.pdf", pages=(9,10))
merger.append("Classwork/Session 12/Session 3 - Industry Analysis (Breakfast Cereal and Five Forces).pdf", pages=(10,17))
merger.append("Classwork/Session 12/Session 3 - Industry Analysis (Breakfast Cereal and Five Forces).pdf", pages=(17,18))

merger.write("combinedResultSix.pdf")
merger.close()