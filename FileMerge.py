
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter
from PyPDF2 import PdfMerger
import os

file_path = r'C:\Users\JT-0919\Desktop\Hi\YQP'


def merge_file():
    in_files = [
        'scan_20221222120359.pdf',
        'NEW_DEL.pdf']
    out_file = 'NEW_OUT.pdf'
    merger = PdfMerger()
    for pdf in in_files:
        reader = PdfReader(os.path.join(file_path, pdf))
        if reader.isEncrypted:
            reader.decrypt("")
        merger.append(reader)
    merger.write(os.path.join(file_path, out_file))
    merger.close()


def del_file(del_num):
    in_file = r'C359 省委军民融合办关于征求《湖北省支持绿色智能船舶产业发展试点示范若干措施（征求意见稿）》意见的函.pdf'
    out_file = r'NEW_DEL.pdf'

    if type(del_num) == int:
        del_multi = False
    elif type(del_num) == list or type(del_num) == set or type(del_num) == tuple:
        del_multi = True
    else:
        print("Unsupported type!")
        return

    reader = PdfReader(os.path.join(file_path, in_file))
    writer = PdfWriter()
    for num in range(0, reader.getNumPages()):
        if del_multi:
            if num + 1 in del_num:
                continue
        else:
            if num + 1 == del_num:
                continue
        writer.addPage(reader.getPage(num))
    writer.write(os.path.join(file_path, out_file))


if __name__ == '__main__':
    try:
        del_file([1, 2])
        # merge_file()
    except Exception as e:
        print(e)

