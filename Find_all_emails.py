__author__ = 'pjha'
import sys
import re

def main():
    f=open('test.txt','r')
    print f
    match = re.search(r'pi+', 'piiig')
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', f.read())
    print emails











if __name__ == '__main__':
    main()