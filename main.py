import tkinter as tk
import csv

def load_patterns():
    with open('crochet_patterns.csv', 'r') as file:
        reader = csv.reader(file)
        patterns = list(reader)
    return patterns

def next_pattern():
    global completions
    global current_row
    completions += 1
    if completions == int(patterns[current_row % len(patterns)][1]):
        completions = 0
        current_row += 1
    update_display()

def update_display():
    row_label.config(text=f'Carreira {current_row + 1}', fg='#BEADFA', bg='#363062')
    pattern_label.config(text=f'Padrão: {patterns[current_row % len(patterns)][0]}', fg='#F8BDEB', bg='#363062')
    completion_label.config(text=f'Completos: {completions}/{patterns[current_row % len(patterns)][1]}', fg='#FFCD4B', bg='#363062')

def on_key(event):
    global completions
    if event.char == ' ':
        next_pattern()
    elif event.char == 'r' or event.char == 'R':
        global current_row
        current_row += 1
        completions = 0
        update_display()

# Initialize variables
global current_row
global current_pattern
global completions
current_row = 0
current_pattern = 0
completions = 0
patterns = load_patterns()

# Create the main window with larger dimensions
root = tk.Tk()
root.title('Crochet Pattern Tracker')

# Set the background color
root.configure(bg='#363062')

# Center the window on the screen
window_width = 500
window_height = 150
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) / 2
y_coordinate = (screen_height - window_height) / 2
root.geometry(f'{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}')

# Create labels with customized styles and padding
row_label = tk.Label(root, text=f'Carreira {current_row + 1}', font=("Helvetica", 16), padx=10, pady=5)
row_label.pack()

pattern_label = tk.Label(root, text=f'Padrão: {patterns[0][0]}', font=("Helvetica", 20), padx=10, pady=5)
pattern_label.pack()

completion_label = tk.Label(root, text=f'Completos: {completions}/{patterns[0][1]}', font=("Helvetica", 16), padx=10, pady=5)
completion_label.pack()

# Apply font colors and background colors
update_display()

# Bind space key press to the window
root.bind('<Key>', on_key)

# Start the main event loop
root.mainloop()