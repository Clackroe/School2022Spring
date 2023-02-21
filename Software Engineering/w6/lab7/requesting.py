import requests


def indeed_request():
    # TODO 2: Put the code from the Postman steps of the lab here.
    # - Make sure you used the correct URL
    # - Also, erase any unnecessary code like the import statement
    url = "https://www.indeed.com/jobs?q=Software Engineer&l=Charlotte"

    payload={}
    headers = {
    'Cookie': 'CTK=1gpqukgu5joos800; __cf_bm=8Z87lLRUSH2s.D_aAIiKRYFYYTkiXfPLw..7UGEyV1M-1677015532-0-Af4lUpl7URet4LRZw7ABeghipH/pAlfwdlP6jFA5oQ5X2rO26pCilhR1igCVlarMfRYHUSulelTC3f5waetsWcI=; _cfuvid=ZXgmRla1CpGF9ohQusbtfG_J4pFjP_KTsNOwmLcCtaY-1677015532866-0-604800000; INDEED_CSRF_TOKEN=gwTbRZXy4e1E45MSnSqF6ZF0BOHUqdAb; JSESSIONID=CDB50D6E5930836ABC70741B81344393; LV="LA=1677015532:CV=1677015532:TS=1677015532"; PREF="TM=1677015532494:L=Charlotte"; RQ="q=Software+Engineer&l=Charlotte&ts=1677015532534"; UD="LA=1677015532:CV=1677015532:TS=1677015532:SG=ab15b6b63eb945a8746ae3c36051169e"; ctkgen=1; indeed_rcc=""; jaSerpCount=1'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)



if __name__ == '__main__':
    indeed_request()
