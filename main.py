from pdf_report import PdfReport, FileSharer
from roommate import Bill, Flatmate

amount_bill = float(input('Please enter the bill amount: '))
period_bill = input('Please enter the month and year of billing period (ex. May 2021): ')
roomy1_name = input('Please enter your name: ')
roomy1_days_stayed = int(input(f'Please enter number of days you stayed {roomy1_name}: '))
roomy2_name = input('Please enter your name: ')
roomy2_days_stayed = int(input(f'Please enter number of days you stayed {roomy2_name}: '))

# Generate the Bill
bill = Bill(amount=amount_bill, period=period_bill)
# Create Roommates
roomy1 = Flatmate(name=roomy1_name, days_in_house=roomy1_days_stayed)
roomy2 = Flatmate(name=roomy2_name, days_in_house=roomy2_days_stayed)
# Print to screen amount that each roommate pays
print(f"{roomy1.name} pays: ${roomy1.pays(bill, roomy2)}")
print(f"{roomy2.name} pays: ${roomy2.pays(bill, roomy1)}")
# Create PDF for billing information
pdf_file = PdfReport(f"{bill.period}_billing.pdf")
pdf_file.generate(roomy1, roomy2, bill)
shared_pdf_url = FileSharer(filepath=pdf_file.filename)
print(shared_pdf_url.upload())
