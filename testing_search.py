import wikipedia
import ddg3


def search_wik(query):
    summary_test=wikipedia.summary(query,sentences=1)
    print ("\n"+"Wikiepdia"+"\n"+summary_test)


def search_duck(query):
    r = ddg3.query(query)
    print("\n"+"Duck and Duck"+"\n"+r.related[1].text)


search_wik('Abhishek')
search_duck("Abhishek")

