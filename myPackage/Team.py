class Team(object):
    def __init__(self, list_of_dev_and_des):
        self.list_of_dev_and_des = list_of_dev_and_des

    def show(self):
        print('Team:')
        for i in range(len(self.list_of_dev_and_des)):
            self.list_of_dev_and_des[i].show()
