#!/usr/bin/python

import sys
import csv
import requests
import StringIO

asxlistedcompaniesfile = 'http://www.asx.com.au/asx/research/ASXListedCompanies.csv'

if len(sys.argv) != 1:
    print "Usage: scrapeYahooHistoricalData.py "
    print "ASXListedCompanies.csv will be downloaded from: " + asxlistedcompaniesfile

def downloadCSVFile(url):
    asxlistreq = requests.get(url)
    if asxlistreq.status_code != 200:
        raise Exception(asxlistreq.status_code, 'Error downloading file ' + url)
    else:
        return asxlistreq.text

def csvToList(stream):
    csvreader = csv.reader(stream, delimiter=',', quotechar='"')
    return list(csvreader)

def downloadCompanyHistories(symbollist):
    for symbol in symbollist:
        print symbol
        if len(symbol) > 0:
            #http://ichart.finance.yahoo.com/table.csv?s=BHP.AX&d=8&e=20&f=2013&g=d&a=0&b=29&c=1988&ignore=.csv
            url = 'http://ichart.finance.yahoo.com/table.csv?s=' + symbol + '&d=8&e=20&f=2013&g=d&a=0&b=29&c=1988&ignore=.csv'
            req = requests.get(url)
            if req.status_code == 200:
                with open(symbol + '.csv', 'w') as csvfile:
                    csvfile.write(req.text)


def main():
    try:
        csvstring = downloadCSVFile(asxlistedcompaniesfile)
        asxlist = csvToList(StringIO.StringIO(csvstring))[3:]   #ASXListedCompanies.csv data starts on line 4
        asxlist = [row[1] + '.AX' for row in asxlist if len(row) == 3]

        print 'Downloading ' + str(len(asxlist)) + ' companies data.'

        downloadCompanyHistories(asxlist)
    except:
        print 'Error: ' + sys.exc_info()[0]

main()
