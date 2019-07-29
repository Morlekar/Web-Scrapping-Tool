import urllib.request
import urllib.parse
import requests
import bs4 as bs 
import os


x=0
file=open("partsToGetCost.txt","r")
sent = file.read().split('\n')
box=[]
for line in sent:
    line = line.replace(';',' ')
    line = line.split(' ')
    box.append(line)
y=len(box)
#print(box)
#print(box[0])
#print(box[0][0])
file.close()

while(x<y):
    part = box[x][0]
    print(part)
    url = "https://www.digikey.in/products/en?"
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686 AppleWebkit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'

    searchParams = {'keywords':part}
    req = requests.get (url ,params = searchParams, headers=headers)
    url = req.url
    print(url)
    resp = req.text
    soup = bs.BeautifulSoup(resp,'lxml')
    gtable = soup.find('table', id='product-dollars')
    if(gtable == None):
        print("Re-defining search \n")
        savefile=open('sample.txt','w+')
        lookfor = '/product-detail/en'
        for c in soup.find_all('a'):
            linkgot=c.get('href')
            if(linkgot == None):
                pass
            elif(linkgot.find(lookfor)!= -1):
                savefile.write('https://www.digikey.in')
                savefile.write(linkgot)
                savefile.write("\n")
        savefile.close()
        fp=open('sample.txt','r')
        lists=[]
        for line in fp.readlines():
            if line not in lists:
                lists.append(line)
        i=len(lists)
        j=0
        while(j!=i):
            print(lists[j])
            req1=urllib.request.urlopen(lists[j])
            soup=bs.BeautifulSoup(req1,'lxml')
            table=soup.find('table' ,id='product-dollars')
            if(table == None):
                print("Product out of stock\n\n")
                j=j+1
                pass
            else:
                content=table.text
                #content=content.replace('\n',' ')
                content=content.replace('$' ,' ')
                print(content)
                print('\n')
                j=j+1

    else:
        content=gtable.text
        #content=content.replace('\n',' ')
        content=content.replace('$' ,' ')
        print(content)
        print('\n')
    x=x+1

print("Task complete!!!")
sample.close()



