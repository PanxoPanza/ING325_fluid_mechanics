#!/usr/bin/env python
# coding: utf-8

# <font size="6">ING325 - Mecánica de Fluidos</font>
# # Estática de fluidos
# <br><br><br><br>
# Profesor: Francisco Ramírez Cuevas<br>
# Fecha: 9 de Marzo 2023

# ## Presión hidroestática

# ### Presión en un líquido

# Analicemos el problema de uno y dos cuerpos sólidos en reposo, ambos con densidad $\rho$.

# <img src="./figures/stationary_solids.png" width="300px" align= center>

# Como ilustra el diagrama de cuerpo libre, el cuerpo sólido de volumen $V$ está sugeto a fuerzas iguales y contrarias, equivalentes al peso del mismo, $\rho V g$.

# En el caso de dos sólidos con volúmenes $V_1$ y $V_2$, el de más abajo está sugeto a la fuerza por su propio peso y el peso del cuerpo sobre el mismo. La fuerza resultante en el cuerpo de abajo es, $\rho V_1g + \rho V_2g$

# La situación es similar para un líquido contenido en un estanque. Es decir, un elemento diferencial a una distancia $h$ de la superficie libre está sujeto a una fuerza equivalente a la columna de fluido sobre él.

# <img src="./figures/hydrostatic_presure.png" width="300px" align= center>

# 
# 
# Si asumimos que el área diferencial es $dA$ y la densidad del líquido $\rho$, la fuerza resultante es: $\rho g h dA$.
# 
# Luego la **presión estática**, **definida como la fuerza por unidad de área**, es $P = \rho g h$.

# Debido a que el líquido es un elemento deformable e incompresible, la presión estática actúa sobre todas las caras del elemento diferencial.

# <img src="./figures/pressure_point.png" width="200px" align= center>

# En general, la presión en un punto es igual en todas las direcciones. Esto se conoce como el ***principio de Pascal***

# ### Unidades de medida de la presión

# La unidad de medida fundamental de la presión es el **pascal** ($\mathrm{Pa}$):
# 
# \begin{equation}
# 1~\mathrm{Pa} = 1~\mathrm{N}/\mathrm{m}^2
# \end{equation}

# Sin embargo, en la práctica, esta unidad es muy pequeña. Es, por lo tanto, común el uso de múltiplos como el *kilopascal* ($1~\mathrm{kPa} = 10^3~\mathrm{Pa}$).

# Otras unidades comúnes son:
# 
# \begin{align*}
# 1~\mathrm{MPa} &= 10^3~\mathrm{kPa} \\
# 1~\mathrm{bar} &= 100~\mathrm{kPa}  \\
# 1~\mathrm{atm} &= 101.32~\mathrm{kPa} \\
# 1~\mathrm{kgf/cm}^2 &= 98.07~\mathrm{kPa} \\
# 1~\mathrm{psi} &= 6.895~\mathrm{kPa}
# \end{align*}

# Como recomendación para el curso, **convertir siempre las unidades a *kilopascal***

# ### Presión atmosférica

# De igual forma, los gases atmosféricos, atraídos por la fuerza de gravedad, generan una presión sobre todos los cuerpos en la tierra.

# <img src="./figures/atmospheric_presure.png" width="350px" align= center>

# **La presión atmosférica**, así, es el resultado de la columna de gases atmosférico sobre una superficie.

# **La presión absoluta ($P_\mathrm{abs}$)** en un elemento diferencial de fluido en un estanque es, así:
# 
# \begin{equation}
# P_\mathrm{abs} = P_\mathrm{atm} + \rho gh
# \end{equation}

# La presión atmosférica también cambia con la altura.  Sin embargo, el cambio de presión se percibe en logitudes de escala de $1000~\mathrm{m}$, debido a que la densidad de los gases atmosféricos es mucho menor que los líquidos.

# <img src="./figures/atmospheric_pressure_altitude.png" width="350px" align= center>

# En la figura, $P_{\mathrm{O}_2}$, es la *presión parcial de oxígeno* (no es relevante para el curso).

# Debido a la caída de la presión con la altura, la densidad del aire disminuye y la cantidad de oxígeno por $\mathrm{m}^3$ es menor.  

# **A 25 °C al nivel del mar, la presión atmosférica es $1~\mathrm{atm} = 101.325~\mathrm{kPa}$.**

# En resumen, **la presión hidroestática en un punto depende de la columna de fluido sobre él y, por lo tanto, cambia sólamente con la profundidad**.
# 
# <img src="./figures/equal_hydrostatic_presure.png" width="800px" align= center>

# > Notar que **la presión en dos fluidos distintos a la misma profundidad no es la misma**, debido a la diferencia de densidades.

# A partir del principio de Pascal, podemos explicar el funcionamiento de una gata hidráulica

# <img src="./figures/gata_hidraulica.png" width="300px" align= center>

# En el ejemplo, $A_1 < A_2$.

# Considerando que ***el fluído contenido es incompresible***, $P_1 = P_2 = F_1/A_1 = F_2/A_2$, donde concluimos que:
# 
# \begin{equation*}
# F_1 = F_2 \frac{A_1}{A_2} < F_2
# \end{equation*}

# ### Presión en gases
# 
# Los gases se expanden constantemente. Así, la presión en un tanque cerrado es igual en todas las direcciones.

# <img src="./figures/presure_gass.jpg" width="600px" align= center>

# En la figura de la **izquierda**, el líquido está en un contenedor vacío. Debido a que el exterior también es vacío, la columna de líquido en el tubo tiene la misma altura.

# En la **derecha**, el gas producto de la evaporación del líquido genera una presión igual en todas las direcciones. 

# La presión absoluta ejercida por el gas, está dada por la diferencia de altura en el tubo, $P_\mathrm{abs} = \rho_\mathrm{tubo} h g$, donde $\rho_\mathrm{tubo}$ es la densidad del líquido en el tubo ($P_\mathrm{atm} = 0$, en este caso).

# ### Instrumentos para medir la presión

# Llamamos ***presión manométrica ($P_\mathrm{man}$), a la diferencia entre la presión absoluta y la presión atmosférica***,
# 
# \begin{equation}
# P_\mathrm{man} = P_\mathrm{abs} - P_\mathrm{atm}
# \end{equation}
# 
# El instrumento para medir $P_\mathrm{man}$ es el **manómetro**
# <img src="./figures/manometer.png" width="700px" align= center>

# Llamamos ***presión vacuométrica o de vacío ($P_\mathrm{vac}$), a la diferencia entre la presión atmosférica y la absoluta***,
# 
# \begin{equation}
# P_\mathrm{vac} = P_\mathrm{atm} - P_\mathrm{abs}
# \end{equation}

# El instrumento de medida se llama **vacuómetro**.
# <img src="./figures/vacuometer.jpg" width="300px" align= center>

# Por lo general, la presión de vacío se indica con un valor negativo, para mejor interpretación, es decir $P_\mathrm{vac} = P_\mathrm{abs} - P_\mathrm{atm}$.

# El término ***presión barómetrica es equivalente a la presión atmosférica ($P_\mathrm{atm}$)***. 
# 
# Comúnmente, se mide en *milimetros de Mercurio*, $\mathrm{mmHg}$, o *hectapascales*, $\mathrm{hPa}$. El instrumento de medida es el **barómetro**.

# <img src="./figures/barometer.png" width="700px" align= center>

# La conversión de unidades es $760~\mathrm{mmHg} = 1013.2~\mathrm{hPa} = 1~\mathrm{atm}$

# La siguiente figura ilustra todas las presiones
# <img src="./figures/all_pressures.png" width="700px" align= center>

# ## Fuerza hidrostática sobre superficies

# ### Superficicies planas
# 
# El principio de Pascal nos permite determinar la fuerza resultante sobre superficies planas. En el caso de **superficies rectangulares**, *la distribución de presiones forma un trapecio rectángulo de sección cuadrada*. **Las fórmulas de fuerza resultante ($F_R$) y línea de acción ($y_p$),** así, corresponden al **área y centroide del trapecio, respectivamente**.
# 
# <img src="./figures/force_rectangular_plate.png" width="900px" align= center>

# En el caso de superficies de geometría irregular, las solución es más compleja.
# 
# <img src="./figures/force_irregular_plate.png" width="750px" align= center>

# Para una superficie de área $A$, es posible demostrar que la fuerza resultante es:
# 
# \begin{equation}
# F_R = (P_0 + \rho g h_C)A
# \end{equation}
# 
# donde $h_C = y_C\sin\theta$ es la **distancia vertical del centroide de la superfice ($y_C$) al nivel libre del líquido**.

# <img src="./figures/yforce_irregular_plate.png" width="370px" align= center>

# La línea de acción ($y_p$), está dada por la relación:
# 
# \begin{equation}
# y_pF_R = P_0y_CA + \rho g \sin\theta I_{xx,O}
# \end{equation}
# 
# donde $I_{xx,O} = \int y^2dA$ es el *segundo momento de inercia del área*

# La demostración de las ecuaciones para $F_R$ y $y_p$, se deja como ejercicio.

# ### Superficies curvas
# 
# En el caso de superficies curvas, la fuerza resultante se puede obtener mediante un diagrama de cuerpo libre sobre un volumen de fluido, convenientemente seleccionado. 
# 
# <img src="./figures/Force_curved_surface_theory.png" width="800px" align= center>

# Según el diagrama, tenemos: $F_H = F_x$, y $F_V = F_y + W$, donde $W$ es el peso del bloque de fluido.

# Podemos aplicar la misma técnica para una superficie curva en la parte superior.

# <img src="./figures/Force_curved_surface_upwards.png" width="300px" align= center>

# En este ejemplo,
# \begin{align*}
# F_H &= F_x \\
# F_V &= F_y - W
# \end{align*}

# **Cuando la superficie es un arco circular, la línea de acción de la fuerza resultante coincide con el centro del arco**

# <img src="./figures/Force_curved_surface_excercise.png" width="300px" align= center>

# Esto se debe a que la presión en cada punto de la superficie es normal a su área y, por lo tanto, su línea de acción pasa por el centro del arco circular.

# ### Flotación
# 
# Analicemos la fuerza resultante que actúa sobre una placa horizontal sumergida en un fluido de densidad $\rho$.

# <img src="./figures/Buoyancy_derivation.png" width="300px" align= center>

# La fuerza resultante en los bordes es 0 debido al equilibro de fuerzas.

# Por otro lado, el balance entre la fuerza inferior y superior es:
# 
# \begin{align*}
# F_B &= F_\mathrm{inf} - F_\mathrm{sup} \\
#     &= \rho g(s+h)A - \rho gsA \\
#     &= \rho ghA \\
#     &= \rho gV
# \end{align*}
# 
# donde $V$ es el volúmen de la placa.

# El resultado es similar en cuerpos de forma arbitraria. Concluimos que ***la fuerza de flotación que actúa sobre un cuerpo sumergido, es igual al peso del volumen de líquido desplazado por el cuerpo***

# <img src="./figures/Buoyancy_principle.png" width="350px" align= center>

# La posición de un cuerpo, así, depende de la relación entre la densidad del cuerpo $\rho$ y la densidad del fluido $\rho_f$
# 
# <img src="./figures/Buoyancy_example.png" width="350px" align= center>

# ## Referencias
# **Çengel Y. A. y Cimbala M. J. *Mecánica de Fluidos: Fundamentos y Aplicaciones*, 4ta Ed., McGraw Hill, 2018**
# - Capitulo 3: Presión y estática de fluidos
# 
# **White F. M. *Mecánica de Fluidos*, 5ta Ed., McGraw Hill, 2004**
# - Capitulo 2: Distribución de presiones en un fluido
