'''
    This code is garbage dont use it
'''

import PySimpleGUI as sg

# Define constants
GRID_SIZE = (10, 10)
SQUARE_SIZE = 50

# Create initial grid with default colors
grid = [[(255, 255, 255) for _ in range(GRID_SIZE[0])]
        for _ in range(GRID_SIZE[1])]

# Define the layout of the window
layout = [
    [sg.Graph(canvas_size=(GRID_SIZE[0] * SQUARE_SIZE, GRID_SIZE[1] * SQUARE_SIZE),
              graph_bottom_left=(0, GRID_SIZE[1] * SQUARE_SIZE),
              graph_top_right=(GRID_SIZE[0] * SQUARE_SIZE, 0),
              key='-GRAPH-')],
    [sg.Button('Change Square Color'), sg.Button('Exit')]
]

# Create the window
window = sg.Window('Grid of Squares', layout, finalize=True)
graph = window['-GRAPH-']

# Function to update a square's color
def change_square_color(row, col, color):
    grid[row][col] = color
    draw_grid()

# Function to draw the grid with the current colors
def draw_grid():
    graph.erase()
    for row in range(GRID_SIZE[1]):
        for col in range(GRID_SIZE[0]):
            color = grid[row][col]
            graph.draw_rectangle((col * SQUARE_SIZE, row * SQUARE_SIZE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE,
                                  row * SQUARE_SIZE + SQUARE_SIZE),
                                 fill_color=color,
                                 line_color=color)


# Initial drawing of the grid
draw_grid()

# Main event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Change Square Color':
        row = sg.popup_get_text("Enter row:")
        col = sg.popup_get_text("Enter column:")
        r = sg.popup_get_text("Enter red value (0-255):")
        g = sg.popup_get_text("Enter green value (0-255):")
        b = sg.popup_get_text("Enter blue value (0-255):")
        try:
            row = int(row)
            col = int(col)
            r = int(r)
            g = int(g)
            b = int(b)
            if 0 <= row < GRID_SIZE[1] and 0 <= col < GRID_SIZE[0] and 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                change_square_color(row, col, (r, g, b))
            else:
                sg.popup_error("Invalid input. Please enter valid values.")
        except ValueError:
            sg.popup_error("Invalid input. Please enter valid values.")

# Close the window when the loop ends
window.close()