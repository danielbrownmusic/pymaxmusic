#
# pymax_metronome.py
# by Daniel Brown - daniel@intelligentmusicsystems.com
#
# An example of using the pymax system.
# Use with the Max patch "pymax_metronome.maxpat"

class Click():
    def __init__(self):
        self.pitch      = 60
        self.duration   = 500
        self.volume     = 100

def metronome_generator(click):
    ontime = 0
    step = 1.0
    while True:
        yield [ontime, click.pitch, click.volume, click.duration, 1] 
        ontime += step

#------------------------------------------------------------------------

if __name__ == "__main__":

    import pymax
    
    pymax.open_pymax()
    pymax.add_class("click", Click)
    pymax.add_generator("metronome", metronome_generator, "click")
    pymax.run_pymax()