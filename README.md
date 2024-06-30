Updates:

Decreased the size upto 65 to 70% before we had 1.16MB file for CSV file now we have added .bin file to store the index in 8bit binary format which has shown us decrease in size of CSV file to 295KB and calculating all the .bin file size is 304KB which comes around 600KB from 1.16MB to 600KB compression is seen.

Further Needs:
I need to make a new custom file extension which stores all .bin file in a single format and divides it into appropriate tables to recognize in better way.
Further Look into maximum words a page can contain needs to be viewed as we have taken 100 as the threshold point here and then taking modulo but as we are using 8bit format we can store upto 255 words so we need to look further to see if it can cross 255 words or not if yes we need to make a extra .bin file for each page with the last mark and connect both the files together

We are going towards a hard coded form for right now but soon we can make a intelligent dfs way to make the optimization better.

----------------

first install the reportlab library
using the command below.

pip install reportlab

----------------

main file:-pdfshort.py
output.csv contains the dictionary for the book content.

----------------

AIM:

I am trying to compress a pdf file by making a dictionary and mapping its index

further compression is needed....

I have compressed a book of ice and fire which was 1.53MB size into 1.16MB for now

but further dividing the csv files into second layer will compress it further more

It is time consuming to decompress and process but this compression is needed for least used pdf files for a unnecessary space consumption.

In further steps i will compress csv file data and make a new layer of compression on it which might decrease its size by 30 to 40 percent

as it is compression it also displays a property of cryptography as it is not easily readable as it is spreaded in compression layer.

rest of the display properties except for the text part needs to processed seperately somewhere to have a exact copy of pdf but for now i am working on the text part only.

Further Progress Update:

I am working on own custom file extension which will store data in structured way specifically for dictionary based compression applications
suppose a word occurs in more than 100th index then the size of the integer can also cause in memory consumption so a differentiatior needs to be present if we want to use modulo for it
i will work on dictionary mapping which will take page wise storage structure like a sliding window then we will not have to take the dictionary key multiple time while we can access the index in any order which will only take limited space just as much the next button causes.

one more structure can be sorted technique in which occurence comes first all the sorted this will decrease the space by O(n)
