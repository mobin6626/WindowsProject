
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

vless://962a733d-2614-0b9b-7ffe-9ac92ffea8eb@ahmedquran3.xyz:443?path=%2Fcurrent_time&security=tls&encryption=none&type=ws#%40VMESSIR4N+%D8%AE%D8%B1%DB%8C%D8%AF+%DA%A9%D8%A7%D9%86%D9%81%DB%8C%DA%AF+%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%DB%8C

vmess://eyJhZGQiOiJ1czY1Lm5ldGZpbHgubGl2ZSIsImFpZCI6IjAiLCJhbHBuIjoiIiwiZnAiOiIiLCJob3N0IjoidXM2NS5uZXRmaWx4LmxpdmUiLCJpZCI6IjYwZjEyNDM1LWJiNTUtNGRhMi1jYjdkLTRmZWEzNGVjZmEzNyIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJwb3J0IjoiODAiLCJwcyI6IkBWTUVTU0lSNE4g2K7YsduM2K8g2qnYp9mG2YHbjNqvINin2K7Yqti12KfYtduMIiwic2N5IjoiYXV0byIsInNuaSI6IiIsInRscyI6IiIsInR5cGUiOiIiLCJ2IjoiMiJ9

vless://b9ad895b-12ac-40fc-a5ac-a5b2a1285001@172.67.174.190:443?path=%2Ffreecodes&security=tls&encryption=none&host=3k.pureboy.eu.org&type=ws&sni=3k.pureboy.eu.org#%40VMESSIR4N+%D8%AE%D8%B1%DB%8C%D8%AF+%DA%A9%D8%A7%D9%86%D9%81%DB%8C%DA%AF+%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%DB%8C
