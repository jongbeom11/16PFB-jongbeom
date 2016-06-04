# coding:utf8
#http://learnpythonthehardway.org/book/ex47.html
# 각 행 주석 입력 휴 commit


class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)
