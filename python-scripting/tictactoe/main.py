board_print = """
    1   2   3 
 A  {} | {} | {}
   -----------
 B  {} | {} | {}
   -----------
 C  {} | {} | {}
"""
board = [' ' for _ in range(9)]
current_player = 0
pieces = ['X', 'O']
turns = 9

def has_won(piece, board):
  three = piece*3
  winning_indices = [board[:3], board[3:6], board[6:], board[2:8:2], board[::3], board[1::3], board[2::3], board[::4]]
  for boards in winning_indices:
    if ''.join(boards) == three:
      return True
  return False

while turns:
  print(board_print.format(*board))
  move = input(f"\n Player {current_player%2+1}'s move (e.g. B2): ")

  cell = (ord(move[0])-65)*3 + int(move[1]) - 1
  if board[cell] != ' ':
    print(" You can't do that.")
    continue
  
  board[cell] = pieces[current_player]
  if has_won(pieces[current_player], board):
    print(board_print.format(*board))
    print(f" Player {current_player%2+1} has won!")
    break

  turns -= 1
  current_player = (current_player+1)%2

if not turns:
  print(board_print.format(*board))
  print(" It's a draw.")
