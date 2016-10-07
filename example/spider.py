from bs4 import BeautifulSoup
import requests as rqsts

# 현재는 1페이지의 데이터만 가져오고 있다. 페이지 수를 파라미터로 받아 페이지 수만큼의 데이터를 추출하는 로직을 추가해볼까?
def rocketpunch_spider(
        param_job_kind, param_specialty, param_max_page):

    rocketpunch_url = "https://www.rocketpunch.com"

    job_kind = param_job_kind

    specialty = param_specialty
    maxPage = param_max_page

    res = rqsts.get(rocketpunch_url + "/jobs?job=" + job_kind + "&specialty=" + specialty)

    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup.title)

    jobs = soup.find_all("div", class_="card job list")

    for job in jobs:
        job_detail = job.find("div", class_="summary").find("a")
        # 카테고리 태그...
        job_tags = job.find("ul", class_="tags").find_all("a", class_="btn-tag")
        # 신입, 경력, 경력무관...
        job_ics = job.select("dd.dd > span.ic-text")
        # 등록 or 수정일자
        job_reg_date = job.find("div", class_="date reg")
        # 마감일자
        job_end_date = job.find("div", class_="date end")
        print("*" * 50)
        print(job_detail.find("h4", class_="jobtitle").contents[0].string)
        print(job_detail.find("h4", class_="jobtitle").contents[1].string)
        tag_str = ""
        for jobTag in job_tags:
            tag_str += jobTag.string + "|"
        print(tag_str)

        ic_str = ""
        for job_ic in job_ics:
            ic_str += job_ic.string + "|"
        print(ic_str)
        print(job_reg_date.string)
        print(job_end_date.string)
        detail_url = rocketpunch_url + job.find("div", class_="summary").a["href"]
        print(detail_url)
        detail_res = rqsts.get(detail_url)
        detail_soup = BeautifulSoup(detail_res.text, 'html.parser')
        print(detail_soup.find("dl", class_="infoset"))


def saramin_spider(param_search_word):
    # TODO searchWord를 list를 받았을 때에 대한 처리를 추가하고, list만큼 크롤링하도록 수정해야 함.
    # 또한 searchWord가 str, 혹은 list가 아닐 때에 예외 처리하도록 수정할 것.
    if(type(param_search_word) == str):
        search_word = param_search_word
    elif(type(param_search_word) == list):
        search_word = param_search_word
    else:
        search_word = None

    saramin_url = "http://www.saramin.co.kr"

    res = rqsts.get(saramin_url + "/zf_user/search/recruit?company_cd=1&searchword=" + search_word + "&go=&searchType=")

    soup = BeautifulSoup(res.text, "html.parser")
    print(soup.title)

    jobs = soup.find_all("li", class_="list")

    for job in jobs:
        print("*" * 50)
        print(job.select("dt span")[0]["title"])
        print(job.select("dd.multiline > a")[0]["title"])
        print(saramin_url + job.select("dd.multiline > a")[0]["href"])
        detail_res = rqsts.get(saramin_url + job.select("dd.multiline > a")[0]["href"])
        detail_soup = BeautifulSoup(detail_res.text, 'html.parser')
        # 있을 수도 있고, 없을 수도 있다. 말하자면 필수가 아니다...
        print(detail_soup.select("div.recruit_summary")[1])
