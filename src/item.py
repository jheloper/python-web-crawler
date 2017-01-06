class RocketpunchJobItem:

    def __init__(self, **kwargs):
        if 'title' in kwargs.keys():
            self.job_title = kwargs.get('title')
        if 'company' in kwargs.keys():
            self.company_name = kwargs.get('company')
        if 'role' in kwargs.keys():
            self.role = kwargs.get('role')
        if 'career' in kwargs.keys():
            self.career = kwargs.get('career')
        if 'specialty' in kwargs.keys():
            self.specialty = kwargs.get('specialty')
        if 'tags' in kwargs.keys():
            self.tags = kwargs.get('tags')
