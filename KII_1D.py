import numpy as np
from MyFunc import zero_cross

v0 = float(input("vo: "))
gamma = float(input("gamma: "))
qn = int(input("q#:"))

# (a) time array: 0 ≤ t < 7 s, step = 0.01 s
dt = 0.01
t = np.arange(0.0, 7.0, dt)

# (b) velocity v(t) = v0 * e^{-γ t} * cos(10 γ t)
v = v0 * np.exp(-gamma * t) * np.cos(10.0 * gamma * t)

# (c) acceleration a(t) via numerical derivative
a = np.gradient(v, t)  # central differences, same length as t

# (d) position x(t) by numerical integration of v with x(0)=0
#     use left Riemann sum so x has same length as t
x = np.concatenate(([0.0], np.cumsum(v[:-1]) * dt))

# (e) third instant the body stops (v crosses zero): use zero_cross on v
zc_idx = zero_cross(v)            # indices BEFORE each sign change
t3rd_stop = t[zc_idx[2]]          # the 3rd stop (0-based index 2), 0.01s resolution

Answers = [0, t[:10], v[:10], a[:10], x[:10], t3rd_stop]
print(Answers[qn])