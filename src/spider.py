from bs4 import BeautifulSoup
import requests

from src.item import RocketpunchJobItem


class RocketpuchSpider:

    def __init__(self, **kwargs):

        params = None
        if 'job' in kwargs.keys() and 'specialty' in kwargs.keys():
            params = {'job': kwargs['job'], 'specialty': kwargs['specialty']}
        elif 'job' in kwargs.keys():
            params = {'job': kwargs['job']}
        elif 'specialty' in kwargs.keys():
            params = {'specialty': kwargs['specialty']}

        self.response = requests.get('https://www.rocketpunch.com/jobs', params=params)
        self.beautiful_soup = BeautifulSoup(self.response.text, 'html.parser')

    def get_max_page(self):
        last_page = self.beautiful_soup.select_one('li.last a.btn-last')
        last_page_link = str(last_page['href'])
        max_page = int(last_page_link[last_page_link.find('&page=') + 6:len(last_page_link)])
        if max_page > 0:
            return max_page
        else:
            raise Exception('max page is wrong. please check this page.')

    def get_job_info(self):
        jobinfo_list = self.beautiful_soup.select('div.card.job.list')
        job_item_list = []
        for jobinfo in jobinfo_list:
            # 타이틀
            title = str.strip(jobinfo.select_one('h4.jobtitle').contents[0].string)
            # 회사명
            company = jobinfo.select_one('small.worksfor').string
            # 직무
            role_list = []
            for role in jobinfo.select('dl.dl-info.dl-role.clearfix dd.role span.ic-text'):
                role_list.append(role.text)
            # 경력여부
            career_list = []
            for career in jobinfo.select('dl.dl-info.dl-role.clearfix dd.dd > span.ic-text'):
                career_list.append(career.text)
            # 전문분야
            specialty_list = []
            for specialty in jobinfo.select('a.btn.btn-xs.btn-tag'):
                specialty_list.append(specialty.text)
            # 기타 태그들
            tag_list = []
            for tag in jobinfo.select('p.nowrap.area span.ic-text'):
                tag_list.append(tag.text)
            job_item_list.append(RocketpunchJobItem(title=title, company=company, role=role_list, career=career_list,
                                                    specialty=specialty_list, tags=tag_list))
        return job_item_list


def saramin_spider(param_search_word):
    """
    TODO searchWord를 list를 받았을 때에 대한 처리를 추가하고, list만큼 크롤링하도록 수정해야 함.
    또한 searchWord가 str, 혹은 list가 아닐 때에 예외 처리하도록 수정할 것.
    """
    if(type(param_search_word) == str):
        search_word = param_search_word
    elif(type(param_search_word) == list):
        search_word = param_search_word
    else:
        search_word = None

    saramin_url = "http://www.saramin.co.kr"

    res = requests.get(saramin_url + "/zf_user/search/recruit?company_cd=1&searchword=" + search_word + "&go=&searchType=")

    soup = BeautifulSoup(res.text, "html.parser")
    print(soup.title)

    jobs = soup.find_all("li", class_="list")

    for job in jobs:
        print("*" * 50)
        print(job.select("dt span")[0]["title"])
        print(job.select("dd.multiline > a")[0]["title"])
        print(saramin_url + job.select("dd.multiline > a")[0]["href"])
        detail_res = requests.get(saramin_url + job.select("dd.multiline > a")[0]["href"])
        detail_soup = BeautifulSoup(detail_res.text, 'html.parser')
        # 있을 수도 있고, 없을 수도 있다. 말하자면 필수가 아니다...
        print(detail_soup.select("div.recruit_summary")[1])
