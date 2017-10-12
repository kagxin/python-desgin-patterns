"""
mvc
"""
# Model

class Peoples(object):

    def __init__(self):
        self.peoples = []

    def __len__(self):
        return len(self.peoples)

    def __getitem__(self, index):
        
        return self.peoples[index]

    def add(self, people):
        if isinstance(people, str):
            self.peoples.append(people)
            return True
        else:
            return False

    def dec(self, people):
        try:
            self.peoples.remove(people)
            return True
        except ValueError:
            return False

# View
class View(object):
    def show_list(self, peoples):
        print('show peoples list:{}'.format(' '.join(peoples)))
        

    def show_item(self, people):
        print('show a people : {}'.format(people))

    def show_error(self, e):
        print('show error:{}'.format(str(e)))

# Control
class Control(object):
    def __init__(self):
        self.peoples = Peoples()
        self.view = View()

    def show_item_people(self, index):
        try:
            self.view.show_item(self.peoples[index])
        except IndexError as e:
            self.view.show_error(e)

    def show_all_peoples(self):
        self.view.show_list(self.peoples)

    def add_people(self, people):
        self.peoples.add(people)

    def remove(self, people):
        self.peoples.dec(people)

if __name__ == '__main__':
    ctrl = Control()
    ctrl.add_people('xiaoming')
    ctrl.add_people('xiaogang')
    ctrl.show_item_people(1)
    ctrl.show_all_peoples()
    ctrl.remove('xiaoming')
    ctrl.show_all_peoples()
    ctrl.show_item_people(10)