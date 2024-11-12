import streamlit as st
import numpy as np
import time

# Set up the game environment
GRID_SIZE = 20
snake = [(10, 10)]
direction = (0, 1)
food = (5, 5)
score = 0

# Initialize game state
st.title("Snake Game in Streamlit")
game_over = False
move_map = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

# Main game loop
while not game_over:
    st.title(f"Score: {score}")
    
    # Draw the grid
    grid = np.zeros((GRID_SIZE, GRID_SIZE))
    for cell in snake:
        grid[cell] = 1
    grid[food] = 2
    st.image(grid, width=400)

    # Get player input
    new_direction = st.sidebar.selectbox("Direction", ["up", "down", "left", "right"])
    if new_direction:
        direction = move_map[new_direction]

    # Update snake position
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake = [head] + snake[:-1]

    # Check for food collision
    if head == food:
        score += 1
        snake.append(snake[-1])  # Grow snake
        food = (np.random.randint(0, GRID_SIZE), np.random.randint(0, GRID_SIZE))

    # Check for collisions
    if head[0] < 0 or head[0] >= GRID_SIZE or head[1] < 0 or head[1] >= GRID_SIZE or head in snake[1:]:
        st.write("Game Over!")
        st.write(f"Final Score: {score}")
        game_over = True

    time.sleep(0.3)
