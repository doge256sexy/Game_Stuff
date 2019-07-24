
Click for Video:  
[![Pygame Simulations](https://img.youtube.com/vi/NF_c2LwmPXo/0.jpg)](https://www.youtube.com/watch?v=NF_c2LwmPXo)

## Simple PyGame Demos

Navigate to the directory
```
$ cd Game_stuff
```
Move a ball with WASD, with friction simple physics.
```
$ python3 not_tests/acceleration.py
```
Applies a blur filter each pixel's neighborhood.
```
$ python3 not_tests/blur.py
```
The 1-dimensional cellular automaton rule 122, which generates chaotic behavior. Might be turing complete?
```
$ python3 not_tests/elementary_cellular_automaton.py
```
Flood fill around the cursor, inspired by a game somewhere.
```
$ python3 not_tests/floodit.py
```

Sort pixels according to colors, I thought it looked cool
```
$ python3 not_tests/sifts_sift.py
```

A statically rendered mandelbrot set.
```
$ python3 not_tests/simplemandlebrot.py
```

The "Traffic" cellular automaton, that simulates deadlock. Each cell moves either right or down, but a cell cannot move into an occupied cell.
```
$ python3 not_tests/trafficca.py
```

Bezier curves
```
$ python3 tests/bezier_curves_test.py
```
Voronoi diagram, with auxiliary shapes
```
$ python3 tests/voronoi_test.py
```
Bitmapped drawing
```
$ python3 tests/doodles_grid_test.py
```
Finding the convex hull of a set of points. The points randomly move around.
```
$ python3 tests/wrapping_test.py
```
I forget what this algorithm is called, but it finds the shortest path from one place to another on a 2D grid.
```
$ python3 tests/maze_ca_test.py
```
