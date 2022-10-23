#
# pymax_sine_wave.py
# by Daniel Brown - daniel@intelligentmusicsystems.com
#
# An example of using the pymax system.
# Use with the Max patch "pymax_sine_wave.maxpat"

import math

def sine_wave():
    ontime_in_ms = 0
    x = 0
    y = 0
    while True:
        yield [ontime_in_ms, x, y]
        ontime_in_ms += 20
        x = ontime_in_ms
        y = math.sin(2 * math.pi * (ontime_in_ms % 1000)/1000)

if __name__ == "__main__":

    from pymaxmusic import pymax

    pymax.open_pymax()
    pymax.add_generator("sine_wave", sine_wave)
    pymax.run_pymax()

