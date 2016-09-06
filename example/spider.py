from bs4 import BeautifulSoup
from urllib import parse
from urllib.request import urlopen

#TODO 현재는 1페이지의 데이터만 가져오고 있다. 페이지 수를 파라미터로 받아 페이지 수만큼의 데이터를 추출하는 로직을 추가해볼까?
def rocketpunchSpider(paramJobKind, paramSpecialty, paramMaxPage):
    rocketpunchUrl = "https://www.rocketpunch.com"

    jobKind = paramJobKind
    jobKind = parse.quote(jobKind)

    specialty = paramSpecialty
    maxPage = paramMaxPage

    res = urlopen(rocketpunchUrl + "/jobs?job=" + jobKind + "&specialty=" + specialty).read().decode('utf-8')

    soup = BeautifulSoup(res, 'html.parser')
    print(soup.title)

    jobs = soup.find_all("div", class_="card job list")

    for job in jobs:
        jobDetail = job.find("div", class_="summary").find("a")
        #카테고리 태그...
        jobTags = job.find("ul", class_="tags").find_all("a", class_="btn-tag")
        #신입, 경력, 경력무관...
        jobIcs = job.select("dd.dd > span.ic-text")
        #등록 or 수정일자
        jobDateReg = job.find("div", class_="date reg")
        #마감일자
        jobDateEnd = job.find("div", class_="date end")
        print("*" * 50)
        print(jobDetail.find("h4", class_="jobtitle").contents[0].string)
        print(jobDetail.find("h4", class_="jobtitle").contents[1].string)
        tagStr = ""
        for jobTag in jobTags:
            tagStr += jobTag.string + "|"
        print(tagStr)

        icStr = ""
        for jobIc in jobIcs:
            icStr += jobIc.string + "|"
        print(icStr)
        print(jobDateReg.string)
        print(jobDateEnd.string)
        print(rocketpunchUrl + job.find("div", class_="summary").a["href"])

def saraminSpider(paramSearchWord):

    #TODO searchWord를 list를 받았을 때에 대한 처리를 추가하고, list만큼 크롤링하도록 수정해야 함. 또한 searchWord가 str, 혹은 list가 아닐 때에 예외 처리하도록 수정할 것.
    if(type(paramSearchWord) == str):
        searchWord = paramSearchWord
    elif(type(paramSearchWord) == list):
        searchWord = paramSearchWord
    else:
        searchWord = None

    searchWord = parse.quote(searchWord, encoding='euc-kr')

    saraminUrl = "http://www.saramin.co.kr"

    res = urlopen(saraminUrl + "/zf_user/search/recruit?company_cd=1&searchword=" + searchWord + "&go=&searchType=").read().decode('euc-kr')
    soup = BeautifulSoup(res, "html.parser")
    print(soup.title)

    jobs = soup.find_all("li", class_="list")

    for job in jobs:
        print("*" * 50)
        print(job.select("dt span")[0]["title"])
        print(job.select("dd.multiline > a")[0]["title"])
