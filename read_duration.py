import os
from PyPDF2 import PdfFileReader
from tqdm import tqdm
import sec_to_time as sf

location = '/media'

print(f'pdf files in : {location}')
H_PER_DAY = 4
READ_SPEED = 30

files_in_dir = []

for r, d, f in tqdm(os.walk(location), desc = 'walking files ... '):
   for item in f:
      if (item.endswith('.pdf')):
          files_in_dir.append(os.path.join(r, item))

print(f'number of pdf files : {len(files_in_dir)}')
number_pages = []
for item in tqdm(files_in_dir):
    try:
        pdf = PdfFileReader(open(item,'rb'))
        num_pages = pdf.getNumPages()
        num_pages = num_pages - 4
    except:
        print(f'problem with file {item}')
    number_pages.append(num_pages)

#for p, f in zip(number_pages, files_in_dir):
#    print(f)
#    print(p)

total_pages = sum(number_pages)
dur = total_pages * READ_SPEED * 60
dur = sf.sec_to_time_format(dur, hours_per_day = H_PER_DAY)
print(dur)

