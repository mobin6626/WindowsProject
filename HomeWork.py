
import sympy as sp
I = sp.symbols('I')
b = 0
a = 7


k = 4 - 5*sp.I
v = (1 + 2*sp.I, 4 - 3*sp.I, a*sp.I, -b*sp.I)
u = (a + b*sp.I, a - b*sp.I, a*a + b*a*sp.I, a*b - b*a*sp.I)


kv = [k * x for x in v]
ku = [k * y for y in u]


ukv = [x * y for x, y in zip(u, kv)]
kuv = [x * y for x, y in zip(ku, v)]
uv = [x * y for x, y in zip(u, v)]


print(f"<U, KV>: {ukv}")
print(f"<KU, V>: {kuv}")
print(f"<U, V>: {uv}")