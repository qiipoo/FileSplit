
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter
from PyPDF2 import PdfMerger
import sys
import copy
import os

file_path = r'C:\Users\JT-0919\Desktop\Hi\YQP'

input_files = [
    '01-40英尺半高硬开顶重载集装箱运输模式与经济性分析.pdf',
    '02-40英尺半高硬开顶重载集装箱运输模式与经济性分析2.pdf']
output_file = '40英尺半高硬开顶重载集装箱运输模式与经济性分析_NEW.pdf'

if len(sys.argv) == 1:
    merger = PdfMerger()

    for pdf in input_files:
        
        reader = PdfReader(os.path.join(file_path, pdf))
        if reader.isEncrypted:
            reader.decrypt("")

        merger.append(reader)

    merger.write(os.path.join(file_path, output_file))

    merger.close()

else:
    pass
