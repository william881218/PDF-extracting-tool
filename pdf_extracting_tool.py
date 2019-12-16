import pdfplumber
import csv, codecs

def main():
    path = 'test.pdf'
    pdf = pdfplumber.open(path)
    with codecs.open("output.csv", "w",  'utf_8_sig') as csvfile:
        writer = csv.writer(csvfile)
        for page in pdf.pages:
            table = page.extract_tables()
            writer.writerow(table[0][5][1].split('\n'))
            if (table[1][5][1] == None): break
            writer.writerow(table[1][5][1].split('\n'))
    pdf.close()

if __name__ == '__main__':
    main()
