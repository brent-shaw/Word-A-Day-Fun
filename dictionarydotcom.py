import urllib2
import datetime
from bs4 import BeautifulSoup
from time import sleep

wotd = 'https://www.dictionary.com/wordoftheday/'

date = datetime.datetime.today()

lastword = ""
limit = 10000
count = 0

with open('output.csv', 'w') as outfile:
    while (count < limit):

        date -= datetime.timedelta(days=1)

        addr = wotd+date.strftime('%Y/%m/%d')
        page = urllib2.urlopen(addr)
        bs = BeautifulSoup(page, 'html.parser')
        sect = bs.find('div', attrs={'class': 'definition-header'})
        word = str(sect.find('strong'))
        defs = bs.find('ol', attrs={'class': 'definition-list'}).findAll('li')
        defn = ''
        for li in defs:
            defn += str(li.find('span'))[6:-7].replace('<em>', '').replace('</em>', '')+','

        count += 1
        sleep(1) #keep website happy :)

        outfile.write(date.strftime('%Y-%m-%d')+ ","+word[8:-9] + "," + defn+'\n')

        print(date.strftime('%Y-%m-%d')+" - "+word[8:-9])

        print(lastword)

        if word == lastword:
            break
        else:
            lastword = word[8:-9]