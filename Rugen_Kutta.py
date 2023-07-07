import copy


def cargar_r_k(vec,h,beta,  numero_funcion):
    def funcion(x,y , beta,  numero_funcion):
        if numero_funcion == 1:
            sol = y * beta
        elif numero_funcion == 2:
            sol = -(y/(0.8 * x**2)) - y
        elif numero_funcion == 3:
            sol = (0.2 * y) + 3 - x
        else:
            sol = 0
        return sol

    vec[0] += h
    vec[1] = copy.copy(vec[12])

    x = vec[0]
    y = vec[1]
    vec[2] = funcion(x,y, beta, numero_funcion) # k1
    vec[3] = x + h/2
    vec[4] = y + h * vec[2] /2
    vec[5] = funcion(vec[3],vec[4], beta, numero_funcion) #k2
    vec[6] = x + h/2
    vec[7] = y + h * vec[5] /2
    vec[8] = funcion(vec[6],vec[7], beta, numero_funcion) # k3
    vec[9] = x + h
    vec[10] = y + h* vec[8]
    vec[11] = funcion(vec[9],vec[10], beta, numero_funcion) # k4
    vec[12] = y + h/6 * (vec[2] + 2 * vec[5] + 2 * vec[8] + vec[11])
    return vec

def runge_kutta_1(beta, a, h):
    fila = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    fila[0] = - h
    fila[12] = a
    vec_rk = []
    while fila[1] < 3*a:
        fila = copy.deepcopy(cargar_r_k(fila,h,beta,  1))
        vec_rk.append(fila)

    return vec_rk

def runge_kutta_2(t_0, h):
    fila = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    fila[0] = 0
    fila[12] = t_0
    vec_rk = []
    beta = 0
    fila_nueva = copy.deepcopy(fila)

    while True:

        fila = copy.deepcopy(fila_nueva)

        fila_nueva = copy.deepcopy(cargar_r_k(copy.deepcopy(fila),h,beta,  2))
        vec_rk.append(fila)

        print(fila_nueva)
        if (abs(fila_nueva[1] - fila[1])) < 1:
           break

    return vec_rk




vector = runge_kutta_2(50, 0.1)

