winner = None
current_player = 'X'

board = [
  [None, None, None],
  [None, None, None],
  [None, None, None]
]

def printBoard(board):
  for row in board:
    print('%s | %s | %s' % (row[0] or ' ', row[1] or ' ', row[2] or ' '))

  print('')

def gameEnded(board):
  for row in board:
    if None in row:
      return False

  return True

def checkForWinner(board):
  # left to right diagonal line
  if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
    return board[1][1]

  # right to left diagonal line
  if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
    return board[1][1]

  # horizontal lines
  for row in board:
    if row[0] == row[1] and row[1] == row[2]:
      return row[0]

  # vertical lines
  for i in range(0, 3):
    if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
      return board[0][i];

  return None

def getInput():
  row = int(input('Please enter row number: ') or '0')
  column = int(input('Please enter column number: ') or '0')

  while (row < 1 or row > 3) or (column < 1 or column > 3) or (board[row - 1][column - 1] != None):
    if board[row - 1][column - 1] != None:
      print('Oops... try an empty spot!')
    else:
      print('Please enter a number between 1 and 3.')

    print('')

    row = int(input('Please enter row number: ') or '0')
    column = int(input('Please enter column number: ') or '0')

  return (row, column)

def main():
  global board, winner, current_player
  printBoard(board)

  while not winner:
    print('It\'s %s turn' % (current_player))

    [row, column] = getInput()

    board[row - 1][column - 1] = current_player

    winner = checkForWinner(board);

    print('')
    printBoard(board)

    if winner:
      print('The game ended')
      print('The winner is %s!' % (winner))

    if gameEnded(board) and not winner:
      print('The game ended, it\'s a tie :(')
      return

    if current_player == 'X':
      current_player = 'O'
    else:
      current_player = 'X'


if __name__ == '__main__':
  main()