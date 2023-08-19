import random
import tkinter as tk

def spawn_tile():
    empty_cells = [(row, col) for row in range(4) for col in range(4) if board[row][col] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 2 if random.random() < 0.9 else 4
        update_board()

def move_left():
    for row in board:
        new_row = [cell for cell in row if cell != 0]
        new_row += [0] * (4 - len(new_row))
        for i in range(3):
            if new_row[i] == new_row[i + 1] and new_row[i] != 0:
                new_row[i] *= 2
                new_row[i + 1] = 0
        new_row = [cell for cell in new_row if cell != 0]
        new_row += [0] * (4 - len(new_row))
        row[:] = new_row
    spawn_tile()

def move_right():
    for row in board:
        row.reverse()
    move_left()
    for row in board:
        row.reverse()

def move_up():
    board_transposed = [list(row) for row in zip(*board)]
    move_left()
    for row_idx in range(4):
        for col_idx in range(4):
            board[col_idx][row_idx] = board_transposed[row_idx][col_idx]
    spawn_tile()

def move_down():
    board_transposed = [list(row) for row in zip(*board)]
    move_right()
    for row_idx in range(4):
        for col_idx in range(4):
            board[col_idx][row_idx] = board_transposed[row_idx][col_idx]
    spawn_tile()

def update_board():
    for i in range(4):
        for j in range(4):
            cell = board[i][j]
            cell_label = board_labels[i][j]
            cell_label.config(text=str(cell) if cell != 0 else "", bg=cell_colors.get(cell, "white"))

def key_pressed(event):
    key = event.keysym.lower()
    if key == 'w':
        move_up()
    elif key == 'a':
        move_left()
    elif key == 's':
        move_down()
    elif key == 'd':
        move_right()

root = tk.Tk()
root.title("2048")

board = [[0 for _ in range(4)] for _ in range(4)]
board_labels = [[None for _ in range(4)] for _ in range(4)]
cell_colors = {
    2: "light gray", 4: "light yellow", 8: "light pink", 16: "light blue",
    32: "light green", 64: "orange", 128: "yellow", 256: "pink",
    512: "blue", 1024: "green", 2048: "red"
}

frame = tk.Frame(root, bg="black")
frame.grid(row=0, column=0, padx=10, pady=10)

for i in range(4):
    for j in range(4):
        label = tk.Label(frame, text="", width=6, height=3, font=("Helvetica", 24, "bold"), bg="white")
        label.grid(row=i, column=j, padx=5, pady=5)
        board_labels[i][j] = label

spawn_tile()
update_board()

root.bind("<Key>", key_pressed)
root.mainloop()
