import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
import random

fireWidth = 40
fireHeight = 40
firePixelsArray = []
fireColorsPalette = [
    {"r": 7, "g": 7, "b": 7}, {"r": 31, "g": 7, "b": 7}, {"r": 47, "g": 15, "b": 7},
    {"r": 71, "g": 15, "b": 7}, {"r": 87, "g": 23, "b": 7}, {"r": 103, "g": 31, "b": 7},
    {"r": 119, "g": 31, "b": 7}, {"r": 143, "g": 39, "b": 7}, {"r": 159, "g": 47, "b": 7},
    {"r": 175, "g": 63, "b": 7}, {"r": 191, "g": 71, "b": 7}, {"r": 199, "g": 71, "b": 7},
    {"r": 223, "g": 79, "b": 7}, {"r": 223, "g": 87, "b": 7}, {"r": 223, "g": 87, "b": 7},
    {"r": 215, "g": 95, "b": 7}, {"r": 215, "g": 95, "b": 7}, {"r": 215, "g": 103, "b": 15},
    {"r": 207, "g": 111, "b": 15}, {"r": 207, "g": 119, "b": 15}, {"r": 207, "g": 127, "b": 15},
    {"r": 207, "g": 135, "b": 23}, {"r": 199, "g": 135, "b": 23}, {"r": 199, "g": 143, "b": 23},
    {"r": 199, "g": 151, "b": 31}, {"r": 191, "g": 159, "b": 31}, {"r": 191, "g": 159, "b": 31},
    {"r": 191, "g": 167, "b": 39}, {"r": 191, "g": 167, "b": 39}, {"r": 191, "g": 175, "b": 47},
    {"r": 183, "g": 175, "b": 47}, {"r": 183, "g": 183, "b": 47}, {"r": 183, "g": 183, "b": 55},
    {"r": 207, "g": 207, "b": 111}, {"r": 223, "g": 223, "b": 159}, {"r": 239, "g": 239, "b": 199},
    {"r": 255, "g": 255, "b": 255},
]


def start_simulation():
    create_fire_source()
    render_fire()


def create_fire_source():
    for column in range(fireWidth):
        overflow_pixel_index = fireWidth * fireHeight
        pixel_index = (overflow_pixel_index - fireWidth) + column
        firePixelsArray.append(36)


def calculate_fire_propagation(current_pixel_index):
    below_pixel_index = current_pixel_index + fireWidth

    if below_pixel_index >= fireWidth * fireHeight:
        return

    decay = random.randint(0, 3)
    below_pixel_fire_intensity = firePixelsArray[below_pixel_index]
    new_fire_intensity = below_pixel_fire_intensity - decay

    if new_fire_intensity < 0:
        new_fire_intensity = 0

    firePixelsArray[current_pixel_index - decay] = new_fire_intensity


def render_fire():
    fire_canvas = st.empty()
    fire_table = [[0] * fireWidth for _ in range(fireHeight)]

    while True:
        for row in range(1, fireHeight):
            for column in range(fireWidth):
                pixel_index = column + (fireWidth * row)
                fire_intensity = firePixelsArray[pixel_index]

                if fire_intensity > 0:
                    decay = random.randint(0, 1)
                    calculate_fire_propagation(pixel_index)

                color = fireColorsPalette[fire_intensity]
                fire_table[row - 1][column] = f"rgb({color['r']}, {color['g']}, {color['b']})"

        fire_canvas.table(fire_table, width=fireWidth, height=fireHeight, key='fire_table')


if __name__ == "__main__":
    start_simulation()
