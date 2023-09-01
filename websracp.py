import html5lib
import xlsxwriter
import requests
from bs4 import BeautifulSoup
url="https://www.practo.com/search/doctors?results_type=doctor&q=%5B%7B%22word%22%3A%22dermatologist%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22subspeciality%22%7D%5D&city=Kolkata"
r = requests.get(url)
html_text = r.text
soup = BeautifulSoup(html_text, 'html.parser')

workbook  = xlsxwriter.Workbook("Webscraping.xlsx")
worksheet = workbook.add_worksheet("Firstsheet")

worksheet.write(0,0,"Serial No.")
worksheet.write(0,1,"Doctor's Name")
worksheet.write(0,2,"Doctor's Post")
worksheet.write(0,3,"Doctor's Experience")
worksheet.write(0,4,"Doctor's Address")
worksheet.write(0,5,"Doctor's Clinque")
worksheet.write(0,6,"Doctor's Fees")
index=1
all_doctor = soup.find_all('div', class_="info-section")
for all_doctor in all_doctor:
     doctor_name = all_doctor.find('div', class_="u-color--primary uv2-spacer--xs-bottom").text
     doctor_post = " Dermatologist "
     doctor_exp=all_doctor.find('div',class_='uv2-spacer--xs-top').div.text.split()[0]
     doctor_add=all_doctor.find('div',class_='u-bold u-d-inlineblock u-valign--middle').text
     doctor_clinque=all_doctor.find('div',class_="u-d-inlineblock u-valign--middle").a.text
     doctor_fees=all_doctor.find_all('div' , class_="uv2-spacer--xs-top")[-1].span.span.text
     worksheet.write(index,0,index)
     worksheet.write(index, 1, doctor_name)
     worksheet.write(index, 2, doctor_post)
     worksheet.write(index, 3, doctor_exp)
     worksheet.write(index, 4, doctor_add)
     worksheet.write(index, 5, doctor_clinque)
     worksheet.write(index, 6, doctor_fees)
     index=index+1
workbook.close()
