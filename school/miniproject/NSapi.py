import requests
import xmltodict

auth_details = ('stephan.bos@student.hu.nl', 'vUFt25QdHZCKtbbu3kybGwBdwjMGM8BCoyt-8X1cj8jJYCtGjOiDsw')
api_url = 'http://webservices.ns.nl/ns-api-avt?station=ut'
response = requests.get(api_url, auth=auth_details)

vertrekXML = xmltodict.parse(response.text)

print('Dit zijn de vertrekkende treinen: ')
for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
    eindbestemming = vertrek['EindBestemming']

    vertrektijd = vertrek['VertrekTijd']
    vertrektijd = vertrektijd[11:16]

    print('om '+vertrektijd+' vertrekt een trein naar '+ eindbestemming)
