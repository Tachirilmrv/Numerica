import mpmath as mp


mp.mp.dps = 25
mp.mp.pretty = True

mp.cplot(lambda z: z, [-2, 2], [-10, 10])

r, R = 1, 2.5
f = lambda u, v: [r*mp.cos(u), (R+r*mp.sin(u))*mp.cos(v), (R+r*mp.sin(u))*mp.sin(v)]
mp.splot(f, [0, float(2*mp.pi)], [0, float(2*mp.pi)],points=200,dpi=120)

print(mp.mpf(2) ** mp.mpf(0.5) )
print(2 * mp.pi)
print(mp.mp)