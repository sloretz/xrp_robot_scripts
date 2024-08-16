import math

import matplotlib.pyplot as plt

# vvvvv PASTE YOUR DATA HERE vvvvv
data = [
    (-90, 178.7972),
    (-85, 178.3505),
    (-80, 177.7148),
    (-75, 177.268),
    (-70, 177.1649),
    (-65, 177.0962),
    (-60, 177.1649),
    (-55, 177.1821),
    (-50, 137.0619),
    (-45, 137.5945),
    (-40, 178.7801),
    (-35, 180.2406),
    (-30, 257.1134),
    (-25, 257.0447),
    (-20, 256.6151),
    (-15, 256.5979),
    (-10, 256.1512),
    (-5, 256.1512),
    (0, 179.8625),
    (5, 178.9003),
    (10, 178.7972),
    (15, 178.2646),
    (20, 177.3539),
    (25, 177.7319),
    (30, 177.268),
    (35, 176.9588),
    (40, 178.2302),
    (45, 178.6942),
    (50, 179.1409),
    (55, 179.5876),
    (60, 212.2509),
    (65, 211.7869),
    (70, 210.8935),
    (75, 210.9106),
    (80, 210.5155),
    (85, 212.2337),
]
# ^^^^^^^^^^^^^^^^^^^^^

# Convert to radians
theta = [math.radians(d[0]) for d in data]
r = [d[1] for d in data]

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)
ax.set_rmax(400)
ax.set_rticks([100, 200, 300, 400])
ax.set_rlabel_position(-5)
ax.grid(True)
ax.set_theta_zero_location('N')
ax.set_thetamin(-90)
ax.set_thetamax(90)
plt.show()