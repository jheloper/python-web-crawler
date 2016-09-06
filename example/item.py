#TODO job에 해당하는 아이템 클래스 생성하여 사용...
#__init__ 이 생성자이므로 생성자를 구현할 필요가 있다...
class rocketpunchJobItem:

    companyName = ""
    jobTitle = ""
    jobTags = ""
    regDate = ""
    endDate = ""

    def setCompanyName(self, companyName):
        self.companyName = companyName
