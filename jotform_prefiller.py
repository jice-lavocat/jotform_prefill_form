import urllib
import csv
import requests
import json
from urlparse import urljoin

# Get Config
with open('settings.json', 'r') as f:
    config = json.load(f)


def setShortUrlMessage(longUrl):
    """
    Fetch a short URL for this message using Google shortner
    And saves it in the message
    """
    ggShortUrl = "https://www.googleapis.com/urlshortener/v1/url?key=" + config["google_shortener_api_key"]
    params = {"longUrl": longUrl}
    headers = {'content-type': 'application/json'}
    req = requests.post(ggShortUrl, data=json.dumps(params), headers=headers)

    result = req.json()

    try:
        shortUrl = result["id"]
    except:
        shortUrl = longUrl
        print "Error while minifying with %s" % longUrl

    return shortUrl


c = csv.writer(open(config["output_file"], "wb"), delimiter=',', quotechar='"')
with open(config["data_set_file"], 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"', dialect=csv.excel_tab)
    i = 0
    for row in spamreader:
        for idx in config["phone_numbers"]:
            if row[idx] != "":
                row[idx] = "0" + row[idx]

        data = {k: row[idx] for k, idx in config['data_map'].items()}

        url = config["form_url"]
        full_url = url + "?" + urllib.urlencode(data)

        if row[config["main_email_field"]] != "" and "@" in row[config["main_email_field"]]:
            if "google_shortener_api_key" in config and config["google_shortener_api_key"] != "":
                c.writerow([row[config["main_email_field"]], setShortUrlMessage(full_url)])
            else:
                c.writerow([row[config["main_email_field"]], setShortUrlMessage(full_url)])
        else:
            print "There is no email for this entry"
        print i
        i += 1
