"""
I have MS Visual Studio in this PC
then "pip3 install pdfminer.six
"""

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import pdfminer
import io
from io import StringIO
import csv
# The StringIO and cStringIO modules are gone. Instead, import the io module and use io.StringIO or io.BytesIO for text and data respectively.
def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    GIA = text[0:15].strip()
    ldPos = text.find("details/")
    bnid2=text[ldPos+8:ldPos+18]
    return GIA,bnid2


dl=[]
with open('di_list_2018.csv','r') as fr:
    csvReader = csv.reader(fr)

    i=1
    for row in csvReader:
        print(i)
        i+=1
        fname=row[1]+'.pdf'
        gia,bnid=convert_pdf_to_txt(fname)
        r1=[row[0],row[1],row[2],gia,bnid]
        dl.append(r1)
        print(r1)

with open('bn_gia_list_2018.csv','w', newline='') as f:
    writer=csv.writer(f)
    for row in dl:
        writer.writerow(row)