import pdfplumber
import csv
import os

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

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            cnt=0
            for key, value in dictionary.items():
                arr=[]
                temp=key
                # print(temp)
                arr.append(temp)
                byte_arr=[]
                byte=0
                for v in value:
                    binary_string = format(v, '08b')
                    bdigit=[]
                    for w in binary_string:
                        if w=='1':
                            bdigit.append(True)
                        else:
                            bdigit.append(False)
                    for q in range(8):
                        if bdigit[q]:
                            byte |= (1 << q)
                    byte_arr.append(byte)
                    byte=0
                    # arr.append(binary_string)
                    # print(key)
                    # print(v)
                # for v in value:    
                #     print(v)
                folder_name = 'binaryfolder'
                file_name = str(cnt)+'.bin'
                file_path = os.path.join(folder_name, file_name)
                cnt+=1
                with open(file_path, 'wb') as out_file:
                    out_file.write(bytes(byte_arr))
                words.append(arr)
            writer.writerows(words)

        # print(dictionary)
    return words


pdf_path = 'iaf.pdf'
text = extract_text_from_pdf(pdf_path)
