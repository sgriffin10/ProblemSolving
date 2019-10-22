from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()

merger.append("Classwork/Session 12/Session1.pdf", pages=(9,10))
merger.append("Classwork/Session 12/Session4.pdf", pages=(2,10))
merger.append("Classwork/Session 12/Session4.pdf", pages=(11,17))
merger.append("Classwork/Session 12/Session5.pdf", pages=(3,5))
merger.append("Classwork/Session 12/Session5.pdf", pages=(6,7))
merger.append("Classwork/Session 12/Session5.pdf", pages=(9,11))
merger.append("Classwork/Session 12/Session7.pdf", pages=(2,3))
merger.append("Classwork/Session 12/Session7.pdf", pages=(4,6))
merger.append("Classwork/Session 12/Session7.pdf", pages=(7,8))
merger.append("Classwork/Session 12/Session8.pdf", pages=(6,7))
merger.append("Classwork/Session 12/Session9.pdf", pages=(9,10))
merger.append("Classwork/Session 12/Session10.pdf", pages=(7,9))
merger.append("Classwork/Session 12/Session11.pdf", pages=(3,5))
merger.append("Classwork/Session 12/Session11.pdf", pages=(12,13))

merger.write("TheMetaCombinedResults.pdf")
merger.close()