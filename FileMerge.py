
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter
from PyPDF2 import PdfMerger
import sys
import copy
import os

file_path = r'C:\Users\JT-0919\Desktop\Hi\YQP'


def merge_file():
    in_files = [
        'scan_20221222120359.pdf',
        'NEW2.pdf']
    out_file = 'NEW.pdf'
    merger = PdfMerger()
    for pdf in in_files:
        reader = PdfReader(os.path.join(file_path, pdf))
        if reader.isEncrypted:
            reader.decrypt("")
        merger.append(reader)
    merger.write(os.path.join(file_path, out_file))
    merger.close()


def del_file(del_num):
    in_file = r'技术服务方案.pdf'
    out_file = r'NEW2.pdf'
    reader = PdfReader(os.path.join(file_path, in_file))
    writer = PdfWriter()
    for num in range(0, reader.getNumPages()):
        if num == del_num - 1:
            continue
        writer.addPage(reader.getPage(num))
    writer.write(os.path.join(file_path, out_file))


if __name__ == '__main__':
    try:
        del_file(2)
        # merge_file()
    except Exception as e:
        print(e)

