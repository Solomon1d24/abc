import PyPDF2
import sys

inputs = sys.argv[1:]

watermarkfile = "wtr.pdf"

def watermark(pdfs):
    for items in pdfs:
        with open(items, 'rb') as filethatinput:
            pdf = PyPDF2.PdfFileReader(filethatinput)
            pdfWriter  = PyPDF2.PdfFileWriter()
            with open(watermarkfile, 'rb') as filethatwatermark:
                watermark = PyPDF2.PdfFileReader(filethatwatermark)
                for i in range(pdf.getNumPages()):
                    firstPage = pdf.getPage(i)
                    firstPageofwatermark = watermark.getPage(0)
                    firstPage.mergePage(firstPageofwatermark)
                    pdfWriter.addPage(firstPage)
                with open(f"new{items}.pdf", 'wb') as filethatoutput:
                    pdfWriter.write(filethatoutput)

watermark(inputs)






