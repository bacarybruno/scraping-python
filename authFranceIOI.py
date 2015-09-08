import mechanicalsoup

browser = mechanicalsoup.Browser()

URL = 'http://www.france-ioi.org/'

user = {
    "username": "msoup.user",
    "password": "msoup_user"
}

page_formulaire = browser.get(URL)

formulaire = page_formulaire.soup.select("form")[0]

formulaire.select("#sLogin")[0]['value'] = user['username']
formulaire.select("#sPassword")[0]['value'] = user['password']

page_accueil = browser.submit(formulaire, URL)

page_informations = browser.get("http://www.france-ioi.org/user/compte.php")

email = page_informations.soup.select('input[name=sEmail]')[0]['value']

print("Adresse email du compte: ", email)
