import mechanicalsoup

browser = mechanicalsoup.Browser()

URL = 'http://www.supinfo.com/articles/'

page_articles = browser.get(URL)

infos_articles = page_articles.soup.select('.courseContent')[0].select('li')[0]

nbLiens = len(infos_articles.select('a'))

dernier_article = {
    "titre": infos_articles.select('div')[0].select('h4')[0].select('a')[0].text,
    "niveau": infos_articles.select('div')[1].select('i')[0].text,
    "etat": infos_articles.select('div')[1].select('i')[1].text,
    "auteur": infos_articles.select('a')[nbLiens-1].text
}

print("Informations recueillies: ")
for item in dernier_article:
    print(item.capitalize() + ": " + dernier_article[item])

