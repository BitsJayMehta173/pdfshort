import pdfplumber
import csv

words=[]
idx=[]
dictionary=dict()
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
        t=''
        i=0
        row=[]
        for word in text:
            if word==" " or word=='\n':
                # print(t+str(i))
                if t in dictionary:
                    dictionary[t].append(i)
                else:
                    dictionary[t]=[]
                    dictionary[t].append(i)
                row=[]
                i+=1
                if i==100:
                    i=0
                t=""
            else:
                t+=word

        # with open('output.txt', 'w') as file:
        #     for value in words:
        #         file.write(value+" ")

        filename = 'output.csv'

        # Writing to csv file
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for key, value in dictionary.items():
                arr=[]
                temp=key
                # print(temp)
                arr.append(temp)
                for v in value:
                    arr.append(v)
                    # print(key)
                    # print(v)
                # for v in value:    
                #     print(v)
                words.append(arr)
            writer.writerows(words)

        # print(dictionary)
    return words


pdf_path = 'iaf.pdf'
text = extract_text_from_pdf(pdf_path)
