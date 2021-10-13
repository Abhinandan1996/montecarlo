from fenics import *
from dolfin import *
import matplotlib.pyplot as plt
L = 10
W = .2
rho = 1
mu = 1
delta = W/L
gamma = .4 * delta ** 2
beta = 1.25
lambda_ = beta
g = gamma

mesh = BoxMesh(Point(0,0,0),Point(L,W,W),20,10,10)

tol = 1E-12
V = VectorFunctionSpace(mesh, 'P', 1)
def clamped(on_boundary):
    return (on_boundary and abs(x[0]) < tol) or (on_boundary and x[0] < tol + L)

bc= DirichletBC(V, Constant((0, 0,0)), boundary)

def epsilon(u):
    return 0.5*(grad(u) + grad(u).T)

def sigma(u):
    return lambda_*div(u) * Identity(d) + 2*mu*epsilon(u)

u = TrialFunction(V)
d = u.geometric_dimension()  # space dimension
v = TestFunction(V)
f = Constant((0, 0, -rho*g))
T = Constant((0, 0, 0))
a = inner(sigma(u), epsilon(v))*dx
L = dot(f,v)*dx + dot(T,v)*ds
u = Function(V)
solve(a==L, u, bc)
file = XDMFFile("out.xdmf")
file.write(u,0)