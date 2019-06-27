import copy, random
def print_board(s,board):
	print " ",
	for i in range(10):
		print "  " + str(i+1) + "  ",
	print "\n"

	for i in range(10):
	

		if i != 9: 
			print str(i+1) + "  ",
		else:
			print str(i+1) + " ",


		for j in range(10):
			if board[i][j] == -1:
				print '  ',	
			elif s == "t":
				print board[i][j],
			elif s == "s":
				if board[i][j] == "*" or board[i][j] == "$":
					print board[i][j],
				else:
					print " ",
			
			if j != 9:
				print " | ",
		print
		

		if i != 9:
			print "   ----------------------------------------------------------"
		else: 
			print 


def print_board(s,board):


	#chap line haye ofoqis
	print " ",
	for i in range(10):
		print "  " + str(i+1) + "  ",
	print "\n"

	for i in range(10):
	
		
		if i != 9: 
			print str(i+1) + "  ",
		else:
			print str(i+1) + " ",
		for j in range(10):
			if board[i][j] == -1:
				print ' ',	
			elif s == "t":
				print board[i][j],
			elif s == "s":
				if board[i][j] == "*" or board[i][j] == "$":
					print board[i][j],
				else:
					print " ",
			
			if j != 9:
				print " | ",
		print
		
		#chape line haye khat kshi
		if i != 9:
			print "   ----------------------------------------------------------"
		else: 
			print 

def computer_place_ships(board,ships):

	for ship in ships.keys():
	
		#sakhte makane random va taed drosstish
		valid = False
		print "naqshe sakhte shod"  
		while(not valid):

			x = random.randint(1,10)-1
			y = random.randint(1,10)-1
			o = random.randint(0,1)
			if o == 0: 
				ori = "v"
			else:
				ori = "h"
			valid = validate(board,ships[ship],x,y,ori)

		#kashti hara qarar bde dar board
		
		board = place_ship(board,ships[ship],ship[0],ori,x,y)
	
	return board


def place_ship(board,ship,s,ori,x,y):

	#h baraye horizintal va v baraye vertikal b tarrib ( amodi ya ofoqi budn ro tain mikonn)
	if ori == "v":
		for i in range(ship):
			board[x+i][y] = s
	elif ori == "h":
		for i in range(ship):
			board[x][y+i] = s

	return board
	
def validate(board,ship,x,y,ori):

	#baresi emkan qrr girie kashti 
	if ori == "v" and x+ship > 10:
		return False
	elif ori == "h" and y+ship > 10:
		return False
	else:
		if ori == "v":
			for i in range(ship):
				if board[x+i][y] != -1:
					return False
		elif ori == "h":
			for i in range(ship):
				if board[x][y+i] != -1:
					return False
		
	return True

def get_coor():
	
	while (True):
		user_input = raw_input("entekhab khor ra vared knin ( bein 1 ta 10) (row,col) ? ")
		try:
			#baresi vorodi va  tabdil b araye 'coor'
			coor = user_input.split(",")
			if len(coor) != 2:
				raise Exception("Tedad Adad vrodi qeir qabel qabol ast.");

			#baresie adad budn 
			coor[0] = int(coor[0])-1
			coor[1] = int(coor[1])-1

			#baresie rayate meqdar vorodi dar baze 1 ta 10
			if coor[0] > 9 or coor[0] < 0 or coor[1] > 9 or coor[1] < 0:
				raise Exception("lotfan bein 1 ta 10 entekhab konin")

			
			return coor
		
		except ValueError:
			print "Lotfan vorodi ra droros va tanha ba adad por knin"
		except Exception as e:
			print e

def make_move(board,x,y):
	
	#try again dar soorati k user hit bzne va mitone baz shelik kne 
	if board[x][y] == -1:
		return "miss"
	elif board[x][y] == '*' or board[x][y] == '$':
		return "try again"
	else:
		return "hit"

def user_move(board):
	while(True):
		x,y = get_coor()
		res = make_move(board,x,y)
		if res == "hit":
			print "Hit at " + str(x+1) + "," + str(y+1)
			check_sink(board,x,y)
			board[x][y] = '$'
			if check_win(board):
				return "WIN"
		elif res == "miss":
			print "bbakhshid, " + str(x+1) + "," + str(y+1) + " is a miss."
			board[x][y] = "*"
		elif res == "try again":
			print "eshtebah bood , bazam talash kn"	

		if res != "try again":
			return board


def check_sink(board,x,y):

	#baresie inke che chizio zade
	if board[x][y] == "A":
		ship = "A"
	elif board[x][y] == "B":
		ship = "B"
	elif board[x][y] == "S":
		ship = "S" 
	elif board[x][y] == "D":
		ship = "D"
	elif board[x][y] == "P": 
		ship = "P"
	
	#check hameye kashti ha zade shodnya na
	board[-1][ship] -= 1
	if board[-1][ship] == 0:
		print ship + " Sunk"
		

def check_win(board):
	for i in range(10):
		for j in range(10):
			if board[i][j] != -1 and board[i][j] != '*' and board[i][j] != '$':
				return False
	return True

def main():
	ships = {"A":5,
		     "B":4,
 		     "S":3,
		     "D":3,
		     "P":2}
	board = []
	for i in range(10):
		board_row = []
		for j in range(10):
			board_row.append(-1)
		board.append(board_row)
	comp_board = copy.deepcopy(board)
	comp_board.append(copy.deepcopy(ships))
	comp_board = computer_place_ships(comp_board,ships)
	while(1):
		print_board("s",comp_board)
		comp_board = user_move(comp_board)
		if comp_board == "WIN":
			print "User WON! :)"
			quit()


	
if __name__=="__main__":
	main()
