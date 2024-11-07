import pygame
import sys
import numpy as np
import time
import os
import argparse
import json

# Constants
BALL_RADIUS = 10
VELOCITY = 15
SAVE_INTERVAL = 30.0  # Save after 30 seconds

def initialize_screen():
    """Initialize a fullscreen pygame window."""
    pygame.init()
    info = pygame.display.Info()
    return pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)

def save_data(timestamps, coordinates, start_time, end_time, save_path):
    """Save timestamps, coordinates, and execution times to the specified directory."""
    os.makedirs(save_path, exist_ok=True)
    
    # Ensure timestamps and coordinates have matching lengths
    min_length = min(len(timestamps), len(coordinates))
    timestamps = timestamps[:min_length]
    coordinates = coordinates[:min_length]
    
    # Create a dictionary to store the data
    data = {
        'timestamps': timestamps,
        'coordinates': coordinates,
        'start_time': start_time,
        'end_time': end_time
    }
    
    # Save the dictionary as a JSON file
    with open(os.path.join(save_path, 'test_task_info.json'), 'w') as json_file:
        json.dump(data, json_file, indent=4)

def run_test_task(save_path):
    """Run the main test task, capturing ball movements and save data on exit."""
    screen = initialize_screen()
    pygame.display.set_caption("Moving Ball")

    # Initial conditions
    ball_x, ball_y = 50, 50
    velocity_x, velocity_y = VELOCITY, VELOCITY
    timestamps, coordinates = [], []
    start_time = time.time()
    timestamps.append([start_time])  # Log start time

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                end_task(save_path, timestamps, coordinates, start_time)
                return

        if time.time() - start_time > SAVE_INTERVAL:
            end_task(save_path, timestamps, coordinates, start_time)
            return

        # Update ball position and log time and coordinates together
        ball_x, ball_y, velocity_x, velocity_y = update_ball_position(screen, ball_x, ball_y, velocity_x, velocity_y)
        timestamps.append([time.time()])
        coordinates.append((ball_x, ball_y))

        # Render updates
        render(screen, ball_x, ball_y)
        pygame.time.delay(30)  # Control frame rate

def update_ball_position(screen, ball_x, ball_y, velocity_x, velocity_y):
    """Update ball position, reversing direction upon edge collision."""
    ball_x += velocity_x
    ball_y += velocity_y
    if ball_x <= 0 or ball_x >= screen.get_width():
        velocity_x = -velocity_x
    if ball_y <= 0 or ball_y >= screen.get_height():
        velocity_y = -velocity_y
    return ball_x, ball_y, velocity_x, velocity_y

def render(screen, ball_x, ball_y):
    """Render the ball on the screen."""
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), BALL_RADIUS)
    pygame.display.flip()

def end_task(save_path, timestamps, coordinates, start_time):
    """Save data and end the task."""
    end_time = time.time()
    save_data(timestamps, coordinates, start_time, end_time, save_path)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    # Parse output directory argument
    parser = argparse.ArgumentParser(description="Run the test task and save ball movement data.")
    parser.add_argument("--save_path", type=str, default="Calibration", help="Directory to save output files.")
    args = parser.parse_args()

    run_test_task(args.save_path)
