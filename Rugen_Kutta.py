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
    vec[0] = round(vec[0],3)
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
    #vec[0] = round(vec[0],6)
    #vec[1] = round(vec[1], 6)
    #vec[2] = round(vec[2], 6)
    #vec[3] = round(vec[3], 6)
    #vec[4] = round(vec[4], 6)
    #vec[5] = round(vec[5], 6)
    #vec[6] = round(vec[6], 6)
    #vec[7] = round(vec[7], 6)
    #vec[8] = round(vec[8], 6)
    #vec[9] = round(vec[9], 6)
    #vec[10] = round(vec[10], 6)
    #vec[11] = round(vec[11], 6)
    #vec[12] = round(vec[12], 6)

    return vec

def runge_kutta_1(beta, a, h, multiplicador_rk1):
    fila = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    fila[0] = - h
    fila[12] = a
    vec_rk = []
    while fila[1] < 3*a:
        fila = copy.deepcopy(cargar_r_k(fila,h,beta,  1))

        vec_rk.append(copy.deepcopy(fila))

    tiempo_real = vec_rk[-1][0] * multiplicador_rk1

    return tiempo_real, vec_rk

def runge_kutta_2(L, h, multiplicador_rk2):
    fila = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    fila[0] = 0
    fila[12] = L
    vec_rk = []
    beta = 0
    fila_nueva = copy.deepcopy(fila)

    while True:

        fila = copy.deepcopy(fila_nueva)

        fila_nueva = copy.deepcopy(cargar_r_k(copy.deepcopy(fila),h,beta,  2))
        vec_rk.append(fila)


        if (abs(fila_nueva[1] - fila[1])) < 1:
           break

    tiempo_real = vec_rk[-1][0] * multiplicador_rk2
    return tiempo_real, vec_rk


def runge_kutta_3(t_0, h, multiplicador_rk3):
    fila = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    fila[0] = - h
    fila[12] = t_0
    vec_rk = []
    beta = 0
    while fila[1] < 1.5 * t_0:
        fila = copy.deepcopy(cargar_r_k(fila,h,beta,  3))
        vec_rk.append(copy.deepcopy(fila))

    tiempo_real = vec_rk[-1][0] * multiplicador_rk3
    return tiempo_real, vec_rk
# multiplicadores  5, 27, 8

if __name__ == "__main__":
    runge_kutta_1(0.5, 450, 0.1)