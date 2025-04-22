import sympy as sp
from sympy import symbols, sin, cos, exp, atan, pi, Matrix, Eq, solve, diff

# Zadanie 1: Macierz odwrotną A^-1 i sprawdzanie równości A^-1 · A = E
print("Zadanie 1:")
A = Matrix([
    [-2, -2, -3],
    [-5, -3, 4],
    [-5, 5, -1]
])

A_inv = A.inv()
print("Macierz odwrotna A^-1:")
sp.pprint(A_inv)

# Sprawdzenie równości A^-1 · A = E
identity_check = A_inv * A
print("\nSprawdzenie A^-1 · A = E:")
sp.pprint(identity_check)
print("\n" + "=" * 80 + "\n")

# Zadanie 2: Znajdź macierz X z równania macierzowego
print("Zadanie 2:")
B = Matrix([
    [2, -1, 0],
    [1, 4, -1],
    [3, 0, 2]
])

C = Matrix([
    [0, 2, 1],
    [1, -2, 0],
    [3, 1, -2]
])

D = Matrix([
    [3, -1, 0],
    [2, 1, 1],
    [0, 1, -1]
])

# Rozwiązanie równania B·X·C = D => X = B^-1·D·C^-1
B_inv = B.inv()
C_inv = C.inv()
X = B_inv * D * C_inv

print("Macierz X:")
sp.pprint(X)

# Sprawdzenie rozwiązania
check = B * X * C
print("\nSprawdzenie rozwiązania:")
sp.pprint(check)
sp.pprint(D)
print("\n" + "=" * 80 + "\n")

# Zadanie 3: Rozwiązanie układu równań z parametrem p
print("Zadanie 3:")
x1, x2, x3, x4, p = symbols('x1 x2 x3 x4 p')

eq1 = Eq(3 * x1 - 2 * x2 - x3 + 2 * x4, 5)
eq2 = Eq(-2 * x1 - 2 * x2 + 4 * x3 - 2 * x4, -8)
eq3 = Eq(-2 * x1 + x2 + 3 * x3 + 2 * x4, 11)
eq4 = Eq(p * x1 + 2 * x2 - 2 * x3 + 4 * x4, 15)

# Rozwiązanie układu dla x1, x2, x3, x4 w zależności od p
solution = solve((eq1, eq2, eq3, eq4), (x1, x2, x3, x4))
print("Rozwiązanie układu równań:")
for var, expr in solution.items():
    print(f"{var} = {expr}")

# Znalezienie wartości p, dla której układ nie ma rozwiązania
# Musimy znaleźć p, dla którego układ jest sprzeczny lub nieoznaczony
# Sprawdzamy, kiedy równania są liniowo zależne

# Tworzymy macierz rozszerzoną układu
M = Matrix([
    [3, -2, -1, 2, 5],
    [-2, -2, 4, -2, -8],
    [-2, 1, 3, 2, 11],
    [p, 2, -2, 4, 15]
])

# Szukamy wartości p, dla której rząd macierzy głównej jest mniejszy niż rząd macierzy rozszerzonej
# Lub gdy wyznacznik macierzy głównej jest zerowy
A_matrix = M[:, :-1]
det_A = A_matrix.det()
critical_p = solve(det_A, p)
print(f"\nUkład nie ma rozwiązania dla p = {critical_p[0]}")

# Sprawdzenie rozwiązania dla przykładowej wartości p (różnej od critical_p)
if critical_p:
    p_value = critical_p[0] + 1  # bierzemy wartość różną od critical_p
else:
    p_value = 0

substituted_solution = {var: expr.subs(p, p_value) for var, expr in solution.items()}
print(f"\nSprawdzenie rozwiązania dla p = {p_value}:")
for var, val in substituted_solution.items():
    print(f"{var} = {val}")

# Podstawiamy rozwiązanie z powrotem do równań
check1 = eq1.subs(substituted_solution).simplify()
check2 = eq2.subs(substituted_solution).simplify()
check3 = eq3.subs(substituted_solution).simplify()
check4 = eq4.subs({**substituted_solution, p: p_value}).simplify()

print("\nSprawdzenie podstawienia:")
print(f"Równanie 1: {check1}")
print(f"Równanie 2: {check2}")
print(f"Równanie 3: {check3}")
print(f"Równanie 4: {check4}")
print("\n" + "=" * 80 + "\n")

# Zadanie 4: Gradient funkcji F(x,y,z)
print("Zadanie 4:")
x, y, z = symbols('x y z')
F = atan(x + z) / y

grad_F = [
    diff(F, x),
    diff(F, y),
    diff(F, z)
]

M_point = {'x': -2, 'y': -1, 'z': 1}
grad_F_at_M = [expr.subs(M_point) for expr in grad_F]

print("Gradient funkcji F(x,y,z):")
sp.pprint(Matrix(grad_F))
print("\nGradient w punkcie M(-2, -1, 1):")
sp.pprint(Matrix(grad_F_at_M))
print("\n" + "=" * 80 + "\n")

# Zadanie 5: Całki oznaczone
print("Zadanie 5:")

# Całka 1
print("Całka 1:")
integral1 = sp.integrate((sin(x) + cos(2 * x)) / (sin(x) + 2), (x, 0, pi))
print("Wynik:")
sp.pprint(integral1)
print("Wartość numeryczna:")
print(integral1.evalf())

# Całka 2 - zakładając, że k i b są stałymi (używamy symboli)
print("\nCałka 2:")
k, b = symbols('k b', real=True)
integral2 = sp.integrate(atan(k * x + b), (x, -pi / 4, sp.oo))
print("Uwaga: Ta całka może nie być zbieżna dla wszystkich wartości k i b.")
print("Próba obliczenia symbolicznie:")
try:
    sp.pprint(integral2)
except:
    print("Nie udało się obliczyć symbolicznie.")

# Dla konkretnych wartości (np. k=1, b=0)
print("\nDla k=1, b=0:")
integral2_num = sp.integrate(atan(x), (x, -pi / 4, sp.oo))
print("Wynik:")
sp.pprint(integral2_num)
print("Wartość numeryczna:")
print(integral2_num.evalf())

# Całka 3
print("\nCałka 3:")
integral3 = sp.integrate(2 ** (x ** 2 + x + 1), (x, -2, 1))
print("Wynik:")
sp.pprint(integral3)
print("Wartość numeryczna:")
print(integral3.evalf())
print("\n" + "=" * 80 + "\n")

# Zadanie 6: Całki niewłaściwe
print("Zadanie 6:")

# Całka 1
print("Całka 1:")
integral_improper1 = sp.integrate(sin(x) / x, (x, 0, sp.oo))
print("Wynik:")
sp.pprint(integral_improper1)
print("Wartość numeryczna:")
print(integral_improper1.evalf())

# Całka 2
print("\nCałka 2:")
integral_improper2 = sp.integrate(exp(-x ** 3), (x, -2, sp.oo))
print("Wynik:")
sp.pprint(integral_improper2)
print("Wartość numeryczna:")
print(integral_improper2.evalf())
