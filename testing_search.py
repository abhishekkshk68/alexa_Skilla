import wikipedia

def search_wik(query):
    summary_test=wikipedia.summary(query,sentences=1)
    print (summary_test)

search_wik('Abhishek')
