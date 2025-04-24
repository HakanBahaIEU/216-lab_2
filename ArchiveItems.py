class ArchiveItem:
    uid = None
    title = None
    year = None
    def __init__(self,guid,gtitle,gyear):
        self.title = gtitle
        self.uid = guid
        self.year = gyear
    def __str__(self):
        return self.uid+" "+self.title+" "+self.year
    def __eq__(self,obj):
        print(self.uid+" "+self.title+" "+self.year)
        print(obj.uid+""+obj.title)
    def is_recent(self,n):
        if(self.year > 2025-n):
            return True
        else: return False
    def save_to_file(items,filename):
        Books =[]
        Articles = []
        Podcasts = []
        i = 0
        content = ArchiveItem.load_from_file()
        for x in content:
            if(x.year < 2020):
                continue
            if(x.doi[0,6]!="10.1234"):
                continue
            if(isinstance(x,Book)):
                Books.append(x)
            elif(isinstance(x,Article)):
                Articles.append(x)
            elif(isinstance(x,Podcast)):
                Podcasts.append(x)
        with open(filename,"w") as f:
            for x in items:
                f.write(x)
    def load_from_file(filename):
        content = []
        with open(filename,"w") as file:
            tempcontent = []
            file.write(tempcontent)
            file.close()
        i = 0
        while(i < len(tempcontent)):
            if(tempcontent[i]=="Book"):
                tempitem = Book(tempcontent[i+1],tempcontent[i+2])
                content.append(tempitem)
                i += 3
            elif(tempcontent[i]=="Article"):
                tempitem = Article(tempcontent[i+1],tempcontent[i+2])
                content.append(tempitem)
                i += 3
            elif(tempcontent[i]=="Podcast"):
                tempitem = Podcast(tempcontent[i+1],tempcontent[i+2])
                content.append(tempitem)
                i += 3
        return content
class Book:
    author = None
    pages = None
    def __init__(self,var1,var2):
        self.author = var1
        self.pages = var2
    def __str__(self):
        return self.author+" "+self.pages
class Article:
    journal = None
    doi = None
    def __init__(self,var1,var2):
        self.journal = var1
        self.doi = var2
    def __str__(self):
        return self.journal+" "+self.doi
class Podcast:
    host = None
    duration = None
    def __init__(self,var1,var2):
        self.host = var1
        self.duration = var2
    def __str__(self):
        return self.host+" "+self.duration
