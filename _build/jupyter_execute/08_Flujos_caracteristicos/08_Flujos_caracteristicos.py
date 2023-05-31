#!/usr/bin/env python
# coding: utf-8

# # Análisis de las ecuaciones de Navier-Stokes

# ## Introducción
# 
# En la unidad anterior dedujimos las ecuaciones de conservación de masa y momento lineal en su forma diferencial. Respecto a esta última, derivamos las ecuaciones de Navier-Stokes, las cuales corresponden a un caso particular para:
# 
# - Fluido incompresible
# - Fluido Newtoniano

# 
# Estas ecuaciones son la base de la mecánica de fluidos. Técnicamente, cualquier problema de la mecánica de fluidos asociado a las condiciones *incompresible-newtoniano* puede ser caracterizado a partir de la solución de estas ecuaciones. Sin embargo, la complejidad asociada al número de incógnitas, variables independientes, y sobre todo a su condición no-lineal, hacen imposible su solución, salvo en casos particulares.

# En esta unidad analizaremos estas ecuaciones y mostraremos su comportamiento para estos casos.

# ## Soluciones de N-S y continuidad
# 
# A pesar de su complejidad, existen problemas sencillos donde las ecuaciones de Navier-Stokes en conjunto con la ecuación de continuidad tienen solución analítica.

# Para poder resolver estas ecuaciones es fundamental aplicar las *condiciones iniciales y de borde adecuadas*. Si analizamos estas ecuaciones involucradas, notamos que tenemos que tenemos **derivadas de primer orden en el tiempo ($t$)** y **derivadas de segundo orden en el espacio ($x$, $y$, $z$)**. En general, necesitaremos:
# 
# - Una condición inicial
# - Dos condiciones de borde en $x$, $y$, $z$.

# Considerando las incognitas $u$, $v$, $w$ y $p$, esto nos da como resultado **4 condiciones iniciales  y 12 condiciones de borde.**

# En la práctica, sin embargo, es común aplicar supuestos que permiten reducir el tamaño de la ecuación diferencial.

# ### Supuestos típicos

# #### Flujo estacionario
# Este supuesto asume que la variación temporal es despreciable. Las ecuaciónes se simplifican a:
# 
# \begin{align}
# \begin{aligned}
# \nabla\cdot\vec{V} &= 0 \\
# \rho\vec{V}\cdot\nabla\vec{V} &= -\nabla p + \rho\vec{g} + \mu\nabla^2\vec{V}
# \end{aligned}
# \end{align}

# #### Flujo bidimensional
# Este supuesto es útil para reducir una de las tres componentes de la velocidad. En coordenadas cartesianas, la bidimensionalidad permitiría, por ejemplo, ignorar la componente $z$, es decir $w = 0$. Las ecuaciones de continuidad y Navier-Stokes se simplifican a:

# **Encuación de continuidad flujo incompresible**
# 
# \begin{equation*}
# \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} = 0
# \end{equation*}
# 
# **Navier-Stokes**
# 
# \begin{align*}
# \rho \left(\frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} + v\frac{\partial u}{\partial y}\right) &= -\frac{\partial p}{\partial x} + \mu \left(\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2}\right) + g_x
# \\
# \rho \left(\frac{\partial v}{\partial t} + u\frac{\partial v}{\partial x} + v\frac{\partial v}{\partial y}\right) &= -\frac{\partial p}{\partial y} + \mu \left(\frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2}\right) + g_y
# \end{align*}
# 

# Notar que, en este caso, si $g_z \neq 0$ la componente $z$ de las ecuaciones de Navier-Stokes quedaría como:
# 
# \begin{equation*}
# 0 = \frac{\partial p}{\partial z} + \rho g_z
# \end{equation*}
# 
# Que corresponde a la ecuación para presión hidrostática.

# El razonamiento análogo en coordenadas cilindricas se denomina, **flujo con simetría axial o axial-simétrico**. En este caso $\frac{\partial}{\partial \theta} = 0$, y las ecuaciones se simplifican a:

# **Encuación de continuidad flujo incompresible**
# 
# \begin{equation*}
# \frac{1}{r}\frac{\partial}{\partial r}(ru_r) + \frac{\partial u_z}{\partial z} = 0
# \end{equation*}
# 
# **Navier-Stokes**
#     
# \begin{align*}
# \rho \left(\frac{\partial u_r}{\partial t} + u_r\frac{\partial  u_r}{\partial r} + u_z\frac{\partial u_r}{\partial z}\right) &= -\frac{\partial p}{\partial r} + \mu\left[\frac{1}{r}\frac{\partial}{\partial r}\left(r\frac{\partial u_r}{\partial r}\right)  - \frac{u_r}{r^2}  + \frac{\partial^2 u_r}{\partial z^2}\right] + \frac{g_r}{\rho} 
#     \\
# \rho \left(\frac{\partial u_z}{\partial t} + u_r\frac{\partial  u_z}{\partial r} + u_z\frac{\partial u_z}{\partial z}\right) &= -\frac{\partial p}{\partial z} + \mu\left[\frac{1}{r}\frac{\partial}{\partial r}\left(r\frac{\partial u_z}{\partial r}\right) + \frac{\partial^2 u_z}{\partial z^2} \right] + \frac{g_z}{\rho}
# \end{align*}
# 

# #### Flujo desarrollado
# 
# Este supuesto se aplica para **despreciar la tasa de cambio en la dirección paralela a alguna de las componentes de velocidad**.

# El concepto nace del flujo en tuberías, donde la tasa de cambio de la componente longitudinal, $\frac{\partial u_z}{\partial z} \approx 0$ despues de la región de desarrollo del flujo. 
# 
# <img src="./figures/condicion_flujo_desarrollado.png" width="800px" align= center>

# Sin embargo, se puede aplicar a otros problemas como veremos más adelante.

# ### Condiciones de borde típicas
# 
# Una vez establecidos los supuestos, es necesario implementar las condiciones de borde necesarias para resolver el problema.

# Las más comunes son.
# 
# <img src="./figures/condicion_de_frontera.png" width="800px" align= center>

# ### Flujos característicos

# Existen 3 problemas característicos que pueden ser resueltos analiticamente a partir de las ecuaciones de continuidad y Navier-Stokes.
# 
# <img src="./figures/tipos_de_flujo.png" width="800px" align= center>

# La solución a estos problemas se verá en la sesión de cátedra.

# ## Referencias
# **Çengel Y. A. y Cimbala M. J. *Mecánica de Fluidos: Fundamentos y Aplicaciones*, 4ta Ed., McGraw Hill, 2018**
# - Capitulo 9. Análisis diferencial de flujo de fluidos
# - Capitulo 10. Soluciones aproximadas de la ecuación de Navier-Stokes
# 
# **White F. M. *Mecánica de Fluidos*, 5ta Ed., McGraw Hill, 2004**
# - Capítulo 4. Relaciones diferenciales para una partícula fluida
# 
