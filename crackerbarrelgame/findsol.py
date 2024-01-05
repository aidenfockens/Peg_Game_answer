
from queue import PriorityQueue


JUMPS = {0: [(1,3),(2,5)],
    1: [(3,6),(4,8)],
    2: [(4,7),(5,9)],
    3: [(1,0),(4,5),(6,10),(7,12)],
    4: [(7,11),(8,13)],
    5:[(2,0),(9,14),(8,12)],
    6: [(3,1),(7,8)],
    7: [(4,2),(8,9)],
    8: [(7,6),(4,1)],
    9: [(8,7), (5,2)],
    10: [(6,3),(11,12)],
    11: [(12,13),(7,4)],
    12: [(11,10),(13,14),(7,3),(8,5)],
    13: [(12,11),(8,4)],
    14: [(9,5),(13,12)]}
def possmoves(board):
        moves = []
        for i in range(len(board)):
            if board[i] == 1:
                for tup in JUMPS[i]:
                    if board[tup[0]] == 1 and board[tup[1]] == 0:
                        moves.append((i,tup))
        return moves

class board:
    
    


    def __init__(self,prev, move,num):
        if num != None:
            self.parent = None
            self.num_moves = 0
            self.board = [0] * 15
            for i in range(15):
                if i == num:
                    self.board[i] = 0
                else:
                    self.board[i] = 1
            self.poss_moves = possmoves(self.board)
        else:
            self.parent = prev
            self.board = prev.make_move(move)
            self.num_moves = prev.num_moves + 1
            self.poss_moves = possmoves(self.board)
    
    def make_move(self,move):
        next_board = self.board.copy()
        next_board[move[0]] = 0
        next_board[move[1][0]] = 0
        next_board[move[1][1]] = 1
        return next_board


    # compares the state objects when they're put in the priority queue, improving the efficiency of the algorithm
    def __lt__(self,other):
        return self.num_moves > other.num_moves
    def get_board(self):
        return self.board
    def get_poss_moves(self):
        return self.poss_moves
    def get_num_moves(self):
        return self.num_moves
    def get_parent(self):
        return self.parent
    def print_board(self):
        print("    " + str(self.board[0]) + "\n   " +  str(self.board[1]) + " " + str(self.board[2]) + "\n  " + str(self.board[3]) + " "+ str(self.board[4]) + " " + str(self.board[5]) + "\n "+ str(self.board[6]) + " " + str(self.board[7]) + " " + str(self.board[8]) + " " + str(self.board[9]) + "\n" + str(self.board[10]) + " " + str(self.board[11]) + " " + str(self.board[12]) + " " + str(self.board[13]) + " " + str(self.board[14])) 

        



def run_game():
    states = PriorityQueue()
    prev_states = []
    path = []

    #for i in range(15):
    #    states.put(board(None,None,i))
    states.put(board(None,None,2))
    
    while not states.empty():
        state = states.get()
        # if you have won, then find the path you took and print it out
        if state.get_num_moves() ==  13:
            
            while state != None:
                path.append(state)
                state = state.get_parent()
            path.reverse()
            
            for step in path:
                step.print_board()
                print()
            print(len(prev_states))
            break

        prev_states.append(state.get_board())

        for move in state.get_poss_moves():
  
            next_state = board(state,move,None)
            if next_state.get_board() not in prev_states:
                states.put(next_state)

        
            
        
        

run_game()