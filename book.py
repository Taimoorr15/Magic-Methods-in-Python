class Book:
    def __init__(self,name,author,num_pages):
        self.name = name
        self.author = author
        self.num_pages = num_pages

    def __str__(self): # Allows you to print the object directly with all its attributes
        return f"{self.name} is written by {self.author} and it has a total of {self.num_pages} pages"
    
    def __lt__(self,other): # Checksif the value is lesser than and returns a boolean
        return self.num_pages < other.num_pages
    
    def __gt__(self,other): # Checks if the value is greater than and returns a boolean
        return self.num_pages > other.num_pages
    
    def __add__(self,other): # This adds two values and returns their sum
        return self.num_pages+other.num_pages
    
    def __contains__(self,keyword): # Checks if the object contains the keywords or not
        return keyword in self.name or keyword in self.author
    
    def __getitem__(self,key): # Checks if the object contain the 'key' item or not
        if key == 'name':
            return self.name
        elif key == 'author':
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else:
            return f"key '{key}' was not found"
        
#Now we will run __str__ magic method
#book1 = Book("Maths","Taimoor",213)
#print("--str-- METHOD")
#print(book1)
#This returns 'Maths is written by Taimoor and it has a total of 213 pages'

# Now we will test the __lt__ magic method
#print("--lt-- METHOD")
#book1 = Book("Maths","Taimoor",213)
#book2 = Book("Physics","Owais",435)
#print(book1 < book2)
#This return True

#print("--gt-- METHOD")
#book1 = Book("Maths","Taimoor",213)
#book2 = Book("Physics","Owais",435)
#print(book1 > book2)
#This returns False

#print("--add-- METHOD")
#book1 = Book("Maths","Taimoor",213)
#book2 = Book("Physics","Owais",435)
#print(book1 + book2)
#This returns 648 after adding both the number of pages of the books

#print("--contains-- METHOD")
#book1 = Book("Maths","Taimoor",213)
#book2 = Book("Physics","Owais",435)
#print("Taimoor" in book1)
#This returns True as book1 contains "Taimoor" in author

#print("--getitem-- METHOD")
#book1 = Book("Maths","Taimoor",213)
#book2 = Book("Physics","Owais",435)
#print(book2['name'])
#This returns Physics as book2 name is Physics
