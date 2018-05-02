#Athlete类记录选手信息
class AthleteList(list):
    def __init__(self,a_name,a_dob=None,a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
        #self.top3_times = top3(self) #:增加该字段会降低灵活性

    def top3(self):
        return (sorted(set([sanitize(t) for t in self]))[0:3])
