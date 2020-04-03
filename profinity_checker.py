import urllib.request

def read_text():
    quotes = open("C:\movies_quote.txt")
    contents_of_files = quotes.read()
    print(contents_of_files)
    quotes.close()
    check_profanity(contents_of_files)

def check_profanity(text_to_check):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output =  connection.read()
    output1 = output.decode("ascii")
    print(output)
    connection.close()
    
read_text()
