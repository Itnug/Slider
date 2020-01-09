'''
Created on 22-Mar-2017

@author: Srinivas Gunti
'''
import random


class Slider(object):
    UP = ['w', 'up']
    LEFT = ['a', 'left']
    DOWN = ['s', 'down']
    RIGHT = ['d', 'right']
    valid_moves = UP+DOWN+LEFT+RIGHT
    _markov_dict = {'w':'wad', 'a':'was', 's':'sad', 'd':'wsd'}
    
    def __init__(self, size, seed=None):
        self.size = size
        self.grid = map(str, xrange(1,size**2))+[' ']
        self.solvedHash = self.hash()
        self.padding = len(self.grid[-2])
        self.open_pos = (size**2) - 1
        if seed:
            random.seed(seed)
        self.scramble(250*(self.size**2))
    
    def __str__(self):
        _str = ''
        for i in range(0, self.size**2,self.size):
            _str += ' '.join('{:>{}}'.format(x,self.padding) for x in self.grid[i:i+self.size])+'\n'
        return _str
    
    def _swap(self, newpos):       
        self.grid[self.open_pos], self.grid[newpos] = self.grid[newpos], self.grid[self.open_pos]
        self.open_pos = newpos
    
    def scramble(self, n_moves):
        next_move = 'd'
        for i in xrange(n_moves):
            self.move(next_move)
            next_move = random.choice(self._markov_dict[next_move])
    
    def hash(self):
        return ''.join(self.grid) 
    
    def isSolved(self):
        return self.hash() == self.solvedHash
        
    def move(self, instruction):
        if instruction in self.UP:
            if self.open_pos / self.size != self.size-1:
                self._swap(self.open_pos + self.size)
        if instruction in self.LEFT:
            if self.open_pos % self.size != self.size-1:
                self._swap(self.open_pos + 1)
        if instruction in self.DOWN:
            if self.open_pos / self.size != 0:
                self._swap(self.open_pos - self.size)
        if instruction in self.RIGHT:
            if self.open_pos % self.size != 0:
                self._swap(self.open_pos - 1)
    
    def execute(self, seq):
        for instruction in seq:
            self.move(instruction)

if __name__ == '__main__':
    puzzle = Slider(4)
    print puzzle
    q = ''
    while q !='exit':
        q = raw_input("next move?")
        if q in puzzle.valid_moves or all(x in puzzle.valid_moves for x in q):
            for x in q:
                puzzle.move(x)
            print puzzle
            if puzzle.isSolved():
                print '~~Yayy! You solved it!~~'
            
                q = raw_input('Go again?(y/n)')
                if q.lower() == 'y':
                    q = int(raw_input('Difficulty? (4/5/6/..)'))
                    puzzle = Slider(q)
                    print puzzle
                else:
                    print 'Bye then'
                    q = 'exit'
        elif q == 'help':
            print 'Valid Moves:', puzzle.valid_moves
        elif q != 'exit':
            print 'INVALID MOVE'