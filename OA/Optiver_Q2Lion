import heapq

from dataclasses import dataclass


@dataclass
class LionDescription:
    name: str
    height: int


@dataclass
class LionSchedule:
    name: str
    enter_time: int
    exit_time: int


class LionCompetition:
    def __init__(self, lions: list[LionDescription], schedule: list[LionSchedule]):
        # print("lions: ", lions)
        # print("schedule: ", schedule)
        self.lions = {des.height: des.name for des in lions}
        # print("current lion description:", self.lions)
        self.lion_schedule = {person.name: [person.enter_time, person.exit_time] for person in schedule}
        # print("current lion schedule:", self.lion_schedule)
        
        # self.lions: {300: 'marry', 250: 'rob'}
        # self.lion_schedule: {'marry': [10, 15], 'rob': [13, 20]}
        
        self.current_lions = {} # {['marry', 300]: [enter, exit], ['bob', 250]: [enter, exit]}
        

    def lion_entered(self, current_time: int, height: int):
        # print("test test: ", self.current_lions)
        if height in self.lions.keys():
            name = self.lions[height]
            if current_time == self.lion_schedule[name][0]:
                self.current_lions[(name, height)] = [self.lion_schedule[name][0], self.lion_schedule[name][1]]
        else:
            self.current_lions[("na", height)] = [current_time, float("inf")]
        # print("test test test: ", self.current_lions)
        
        

    def lion_left(self, current_time: int, height: int):
        # print("test left: ", self.current_lions)
        if height in self.lions.keys():
            name = self.lions[height]
            if current_time != self.lion_schedule[name][1]:
                self.current_lions[(name, height)][1] = current_time
        else:

            self.current_lions[("na", height)][1] = current_time
        # print("test test test left: ", self.current_lions)


    def get_biggest_lions(self) -> list[str]:
        # print("time:", time)
        # print(self.current_lions)
        newnew = {}
        for key, t in self.current_lions.items():
            # print("key t", key, t)
            name = key[0] 
            height = key[1]
            enter_t = t[0] 
            exit_t = t[1]
            if enter_t <= int(time) and exit_t > int(time):
                # print("name height", name, height)
                if newnew.get(name, None):
                    newnew[name] = max(height, newnew[name]) # newnew: {"na":200} 新进来的"marry":300, newnew: {"marry":300}
                else:
                    newnew[name] = height
        if newnew.get("na", None):
            # print("new none", newnew)
            max_height = newnew.get("na")
        else:
            max_height = float("-inf")
        # print("newnew", newnew)
        returned_res = []
        for name, height in newnew.items():
            if height > max_height:
                returned_res.append(name)
        return returned_res
                    
        

if __name__ == "__main__":
    import sys

    read_line = lambda: sys.stdin.readline().split()

    descriptions: list[LionDescription] = []
    lion_schedule: list[LionSchedule] = []

    parse = True
    while parse:
        line = read_line()
        if line[0] == 'definition':
            name = line[1]
            size = int(line[2])
            description = LionDescription(name, size)
            descriptions.append(description)
        elif line[0] == 'schedule':
            name = line[1]
            enter_time = int(line[2])
            exit_time = int(line[3])
            schedule_entry = LionSchedule(name, enter_time, exit_time)
            lion_schedule.append(schedule_entry)
        elif line[0] == 'start':
            parse = False
        else:
            raise Exception('invalid input')

    lion_competition = LionCompetition(descriptions, lion_schedule)
    parse = True
    while parse:
        line = read_line()
        time = int(line[0])
        if line[1] == 'enter':
            size = int(line[2])
            lion_competition.lion_entered(time, size)
        elif line[1] == 'exit':
            size = int(line[2])
            lion_competition.lion_left(time, size)
        elif line[1] == 'inspect':
            biggest_lions = lion_competition.get_biggest_lions()
            print(len(biggest_lions), end='')
            for lion in biggest_lions:
                print(" " + lion, end='')
            print()
        elif line[1] == 'end':
            parse = False
        else:
            raise Exception('invalid input')
