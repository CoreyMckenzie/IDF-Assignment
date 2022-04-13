import random
#import xlsxwriter

#workbook = xlsxwriter.Workbook('IDF_Assignment.xlsx') #Creating the workbook
#worksheet = workbook.add_worksheet() #Adding the spreadsheet

idfs = ['40-B01-A','40-B01-B', '30-B01-A', '30-B01-B', '30-B01-C', '30-L05-B', '30-L08-B', '50-B01-B1', '20-B01-A', '40-B01-BC', '40-B01-CC', '40-B01-FU', '30-B01-B', '30-L15-B', '50-B01-SPA', '140-MDF', '140-IDF', '41-B01-A', '40-B01-C', '40-B01-AC', '40-B01-DC', '50-B01-A1', '50-B01-A2', '50-B01-B2', '30-L18-B', '40-L03-A', '40-L05-A', '40-L05-B', '40-L08-A', '40-L08-B', '40-L11-A', '40-L11-B', '30-L21-B', '30-L24-B', '40-L15-B', '40-L18-A', '40-L18-B', '40-L21-A', '40-L21-B']
print(len(idfs))
j1 = []
j2 = []
j3 = []
j4 = []


while len(idfs) >= 0:
    try:
        capture = random.choice(idfs)
        if len(j1) != len(j2):
            j1.append(capture)
        elif len(j2) != len(j3):
            j2.append(capture)
        elif len(j3) != len(j4):
            j3.append(capture)
        else:
            j4.append(capture)
        idfs.remove(capture)
        print(len(idfs))
    except:
        break


#worksheet.write('A1', 'j1')
