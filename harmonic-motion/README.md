## harmonic-motion

### Overview

Model of damped harmonic motion with respect to time
- ***x-axis*** is time  
- ***y-axis*** is displacement *by default*

*y-axis* can be changed by changing the following function in `plot.py`

```python
def plotVals(): return t, x(t)
```

The `x(t)` can be changed to any of the following functions:

- `x(t)` for displacement
- `v(t)` for velocity
- `a(t)` for acceleration
- `KE(t)` for kinetic energy

### Run script

```console
$ git clone https://github.com/dhruvnps/physics-models && cd physics-models/harmonic-motion && python plot.py
```

### Adjustable parameters

- gravitational field strength (g)
- mass (m)
- spring constant (k)
- length
