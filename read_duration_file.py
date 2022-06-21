import os
from PyPDF2 import PdfFileReader
from tqdm import tqdm
import sec_to_time as sf

location = '/media'

read_speed = 10 
day_hours = 4
pdf = PdfFileReader(open(location,'rb'))
num_pages = pdf.getNumPages()
num_pages = num_pages - 4

dur = num_pages * read_speed * 60
dur = sf.sec_to_time_format(dur, hours_per_day=day_hours)
print(f'pdf file : {location}')
print(f'number of pages : {num_pages + 4} pages')
print(f'read speed : {read_speed} minutes per page')
print(f'reading hours per day : {day_hours} hours')
print(f'read duration : {dur}')

