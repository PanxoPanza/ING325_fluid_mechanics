#!/usr/bin/env python
# coding: utf-8

# # Análisis diferencial de flujos

# ## Introducción
# 
# Hasta ahora hemos utilizado un enfoque integral, donde aplicabamos las ecuaciones de convervación a un volumen de control. El análisis de volumen de control es útil cuando se esta interesado en las características globales de un flujo y los cuerpos con los que interactúa, por ejemplo: fuerzas de arrastre, energía de una bomba o turbina, velocidades promedio en un ducto, etc.
# 
# <img src="./figures/intro_figure.png" width="700px" align= center>

# El análisis diferencial, por otro lado, permite determinar las interacciones de un fluido con una estructura en cada punto dentro del volúmen de control.

# En esta unidad revisaremos los aspectos generales del análisis diferencial de flujos. Comenzaremos por revisar los aspectos básicos de cálculo vectorial y cinemática de fluidos. Luego derivaremos las ecuaciones de conservación de masa y momento lineal en su forma diferencial. Finalizaremos con las ecuaciones de Navier Stokes, que definen la piedra angular de la mecánica de fluidos

# ## Repaso de cálculo vectorial

# ### Campo vectorial y escalar
# 
# Como vimos en la [unidad 3](../03_Intro_dinamica_de_fluidos/03_Intro_dinamica_de_fluidos.ipynb) del curso, en el **análisis euleriano** de mecánica de fluidos trabajamos con *variables de campo*, es decir, variables que dependen del tiempo ($t$) y el espacio dentro del volumen de control ($x, y,z$). Las principales son:
# 
# \begin{align*}
# P(x,y,z,t) &\quad\quad\mathrm{Campo~de~presión~(campo~escalar)}\\
# \rho(x,y,z,t) &\quad\quad\mathrm{Campo~de~densidad~(campo~escalar)}\\
# \vec{V}(x,y,z,t) &\quad\quad\mathrm{Campo~de~velocidad~(campo~vectorial)}
# \end{align*}

# Donde el campo de velocidad se define por la componente de tres vectores:
# 
# \begin{equation}
# \vec{V} = u(x,y,z,t)~\hat{x} + v(x,y,z,t)~\hat{y} + w(x,y,z,t)~\hat{z}
# \end{equation}
# 
# donde $u$, $v$ y $w$ son las componentes de la velocidad e direcciones $x$, $y$ y $z$, respectivamente.

# ### Operadores diferenciales
# 
# Debido a la cantidad de variables independientes presentes en cada variable, es conveniente utilizar operadores para analizar tasas de cambio y otras caracteristicas de una variable de campo.

# Para esto definimos el operador $\nabla$ o "del", como:
# 
# \begin{equation}
# \nabla= \left( \hat{x}\frac{\partial }{\partial x} + \hat{y}\frac{\partial }{\partial y} + \hat{z}\frac{\partial }{\partial z} \right)
# \end{equation}

# El operador $\nabla$ es un *vector que aplica una derivada espacial a una variable de campo*. **La forma que toma este operador depende del tipo de variable y del producto vectorial aplicado.**

# Algunos ejemplos son:

# #### Gradiente. $\nabla(\quad)$
# 
# Es equivalente a la derivada de una función, pero en múltiples dimenciones. Permite identificar zonas de crecimiento o decrecimiento de una variable de campo.

# **Si el gradiente se aplica a un campo escalar, el resultado es un campo vectorial.** Por ejemplo, el gradiente de la densidad es:
# 
# \begin{equation}
# \nabla \rho= \frac{\partial \rho}{\partial x}\hat{x} + \frac{\partial \rho}{\partial y}\hat{y}+ \frac{\partial \rho}{\partial z}\hat{z}
# \end{equation}

# **Si el gradiente se aplica a un campo vectorial, el resultado es un tensor de orden 2.** Por ejemplo, el gradiente de la velocidad es:
# 
# \begin{equation}
# \nabla \vec{V} = 
# \frac{\partial \vec{V}}{\partial x}\hat{x} + \frac{\partial \vec{V}}{\partial y}\hat{y}+ \frac{\partial \vec{V}}{\partial z}\hat{z}
# = \begin{bmatrix}
# \frac{\partial u}{\partial x} & \frac{\partial u}{\partial y} & \frac{\partial u}{\partial z} \\
# \frac{\partial v}{\partial x} & \frac{\partial v}{\partial y} & \frac{\partial v}{\partial z} \\
# \frac{\partial w}{\partial x} & \frac{\partial w}{\partial y} & \frac{\partial w}{\partial z} 
# \end{bmatrix}
# \end{equation}

# #### Divergente. $\nabla\cdot(\quad)$
# 
# **Solo se aplica a campos vectoriales**. Se define como el producto punto entre el operador Del y un campo vectorial:
# 
# \begin{equation}
# \nabla \cdot \vec{V}= \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z}
# \end{equation}

# El divergente permite medir cuanto un campo vectorial diverge o converge respecto de un punto en cuestión.

# Por ejemplo:
# 
# <img src="./figures/divergence.jpg" width="71%" align= center>
# 
# (a) $\nabla\cdot\vec{V} \gt 0$
# 
# (b) $\nabla\cdot\vec{V} = 0$
# 
# (c) $\nabla\cdot\vec{V} \gt 0$

# #### Rotacional. $\nabla\times(\quad)$ 
# 
# Solo se aplica a campos vectoriales. Se define como el producto cruz entre el operador Del y un campo vectorial:
# 
# \begin{equation}
# \nabla \times \vec{V}= 
# \left(\frac{\partial w}{\partial y} - \frac{\partial v}{\partial z}\right)\hat{x}+
# \left(\frac{\partial u}{\partial z} - \frac{\partial w}{\partial x}\right)\hat{y}+
# \left(\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}\right)\hat{z}
# \end{equation}

# El rotacional una medida de cuanto un campo vectorial rota respecto de un punto en cuestión. 

# Por ejemplo:
# 
# <img src="./figures/curl.jpg" width="650"  align= center>
# 
# (a) $\nabla\times\vec{V} \gt 0$
# 
# (b) $\nabla\times\vec{V} \gt 0$
# 
# >Notar que en la figura, el divergente, $\nabla\cdot\vec{V} = 0$ en todos los casos.

# ## Fundamentos de la cinemática de fluidos

# ### Derivada material
# 
# En el enfoque euleriano las variables dependen del tiempo y del espacio. Así, debemos definir un nuevo operador para evaluar la tasa de cambio de una variable. Este operador será equivalente a la derivada temporal $d/dt$ utilizado en el enfoque lagranfiano.

# Analicemos, por ejemplo, la aceleración ($\vec{a}$) de una partícula de fluido considerando ambos enfoques.

# - Según el **enfoque lagrangiano**, la aceleración de una partícula con velocidad $\vec{V}$, es: $\vec{a} = \frac{d \vec{V}}{dt}$

# - Según el **enfoque euleriano**, la aceleración de una partícual en un volumen de control:
# 
# \begin{align}
# \vec{a}=\frac{d\vec{V}}{dt} &= \frac{\partial \vec{V}}{\partial t}\frac{dt}{dt} +
#         \frac{\partial \vec{V}}{\partial x}\frac{dx}{dt}
#         +
#         \frac{\partial \vec{V}}{\partial y}\frac{dy}{dt}
#         +
#         \frac{\partial \vec{V}}{\partial z}\frac{dz}{dt} \notag\\
#         &= \frac{\partial \vec{V}}{\partial t} 
#         +
#         u\frac{\partial \vec{V}}{\partial x}
#         +
#         v\frac{\partial \vec{V}}{\partial y}
#         +
#         w\frac{\partial \vec{V}}{\partial z}  \notag\\
#         &= \frac{\partial \vec{V}}{\partial t} 
#         +
#         \vec{V}\cdot\nabla\vec{V}
# \end{align}

# Hemos definido un nuevo operador, denominado **derivada material (o sustancial), $\frac{D}{Dt}$ o $\frac{d}{dt}$** que describe la *variación temporal de una partícula de fluido a medida que se mueve por el campo de flujo:*
# 
# \begin{equation}
# \frac{d}{dt}(\quad) = \frac{\partial}{\partial t}(\quad) + \vec{V}\cdot\nabla(\quad)
# \end{equation}

# - El término $\frac{\partial}{\partial t}(\quad)$ se denomina **variación temporal local y *es cero para flujos estacionarios.***

# - El término $\vec{V}\cdot\nabla(\quad)$, se denomina **término convectivo, *este término puede ser diferente de cero inclusive para flujos estacionarios***

# La derivada material se puede aplicar a otras propiedades de fluidos, como por ejemplo, la densidad:
# 
# \begin{equation*}
# \frac{d\rho}{dt} = \frac{\partial\rho}{\partial t} + \vec{V}\cdot\nabla\rho
# \end{equation*}

# ### Tipos de movimiento o deformación de un elemento fluido
# 
# Un elemento fluido puede pasar por cuatro tipos fundamentales de movimiento.

# <img src="./figures/movimiento_fluido.png" width="750px" align= center>

# La **traslación** está simplemente dada por $\vec{V}$.

# La **razón de rotación** está caracterizada como el promedio del operador rotacional, on $\omega = \frac{1}{2}\nabla\times \vec{V}$

# En el caso de los esfuerzos, utilizamos un **tensor de deformación**:
# 
# \begin{equation}
# \bar{\varepsilon} = \frac{1}{2}\left[\left(\nabla\vec{V}\right) + \left(\nabla\vec{V}\right)^T \right] 
# \end{equation}

# En coordenadas cartesianas:
# 
# \begin{equation*}
# \bar{\varepsilon} =
# \begin{bmatrix}
# \varepsilon_{xx} & \varepsilon_{xy} & \varepsilon_{xz} \\
# \varepsilon_{yx} & \varepsilon_{yy} & \varepsilon_{yz} \\
# \varepsilon_{zx} & \varepsilon_{zy} & \varepsilon_{zz}
# \end{bmatrix} = 
# \begin{bmatrix}
# \frac{\partial u}{\partial x} & 
# \frac{1}{2}\left(\frac{\partial u}{\partial y} + \frac{\partial v}{\partial x}\right) & 
# \frac{1}{2}\left(\frac{\partial u}{\partial z} + \frac{\partial w}{\partial x}\right) 
# \\
# \frac{1}{2}\left(\frac{\partial v}{\partial x} + \frac{\partial u}{\partial y}\right) & 
# \frac{\partial v}{\partial y} & 
# \frac{1}{2}\left(\frac{\partial v}{\partial z}  + \frac{\partial w}{\partial y}\right)
# \\
# \frac{1}{2}\left(\frac{\partial w}{\partial x} + \frac{\partial u}{\partial z}\right) & 
# \frac{1}{2}\left(\frac{\partial w}{\partial y} + \frac{\partial v}{\partial z}\right) & 
# \frac{\partial w}{\partial z}
# \end{bmatrix}
# \end{equation*}

# Los **elementos de la diagonal** ($\varepsilon_{xx}$, $\varepsilon_{yy}$ y $\varepsilon_{zz}$) representan la **deformación por esfuerzos normales**. El **resto de los elementos**, corresponde a la **deformación por esfuerzos cortantes**.

# ## Ecuaciones de conservación en forma diferencial
# 
# A partir de los conceptos revisados anteriormente podemos intepretar los patrones de flujo y perfiles de velocidad que caracterizan la interacción de un fluido con una estructura

# <img src="./figures/Ejemplo_CFD.png" width="800px" align= center>

# A continuación derivaremos las ecuaciones diferenciales que gobiernan estos patrones de flujo.

# La derivación de cada ecuación fundamental puede ser realizado de dos formas:

# - Mediante un balance en un volúmen de control diferencial (revisar referencias)
# - Utilizando el *teorema de Gauss* o *teorema de la divergencia* que establece: 
#     >*la integral en una superficie cerrada $S$ de un campo vectorial $\vec{f}$ es igual a la integral de la divergencia de $\vec{f}$ sobre un volumen $V$ dentro de la superficie*
# 
#     Matemáticamente:
#     \begin{equation}
#     \oint_A \vec{f}\cdot\hat{n} dA = \int_V \nabla\cdot \vec{f} d\forall
#     \end{equation}

# ### Ecuación de conservación de masa (continuidad)

# Comenzamos con la ecuación de conservación de masa aplicado sobre un volumen de control fijo e indeformable:

# \begin{align*}
# 0 &= \frac{d}{dt}\int_\mathrm{VC} \rho d\forall + \int_\mathrm{VC} \rho\vec{V}\cdot\hat{n}dA 
# \\[5pt]
# 0 &= \int_\mathrm{VC} \frac{\partial\rho}{\partial t} d\forall + \int_\mathrm{VC} \nabla\cdot\left(\rho\vec{V} \right) d\forall  
# \\[5pt]
# 0 &= \int_\mathrm{VC} \left[\frac{\partial\rho}{\partial t} + \nabla\cdot\left(\rho\vec{V} \right) \right]d\forall 
# \end{align*}

# Para satisfacer esta ecuación el integrando debe ser cero. Después de unas operaciones matemáticas, derivamos la **ecuación de conservación de masa en su forma diferencial**:
# \begin{equation}
# \frac{d\rho}{dt} + \rho\left(\nabla\cdot\vec{V}\right) = 0
# \end{equation}

# Esta ecuación también se conoce como la **ecuación de continuidad**.

# ### Ecuación de conservación de momento lineal

# Podemos aplicar el mismo criterio sobre la ecuación de conservación de momento lineal:
# 
# \begin{align}
# \sum\vec{F}_\mathrm{ext} &= \frac{d}{dt}\int_\mathrm{VC} \rho\vec{V} d\forall + \int_\mathrm{VC} \rho\vec{V}(\vec{V}\cdot\hat{n})dA \notag
# \\
#  &= \int_\mathrm{VC} \left[\frac{\partial}{\partial t}\left(\rho\vec{V}\right)  + \nabla\cdot\left(\rho\vec{V}\vec{V}\right)\right]d\forall
# \end{align}

# Como vimos en la [unidad 6](../06_Flujo_externo/06_Flujo_externo.ipynb), la fuerza externa sobre un volumen de control es el resultado de la distribución de presiones y tensiones de corte. En una perspectiva general, también debemos considerar el efecto de la gravedad. La expresión para  las fuerzas externas es, entonces: 
# 
# \begin{equation}
# \sum\vec{F}_\mathrm{ext} = - \int_A p~\hat{n}dA + \int_A \bar{\tau}\cdot\hat{n}dA  + \int_\mathrm{VC} \rho\vec{g}d\forall
# \end{equation}

# Donde $\bar{\tau}$ es el **tensor de esfuerzos**
# 
# \begin{equation}
# \bar{\tau} =
# \begin{bmatrix}
# \tau_{xx} & \tau_{xy} & \tau_{xz} \\
# \tau_{yx} & \tau_{yy} & \tau_{yz} \\
# \tau_{zx} & \tau_{zy} & \tau_{zz}
# \end{bmatrix}
# \end{equation}

# Usando el teorema de la divergencia, podemos reordenar la expresión (7.13) como:
# 
# \begin{equation}
# \sum\vec{F}_\mathrm{ext} = \int_\mathrm{VC} \left[\nabla\cdot\left( - p\bar{I} + \bar{\tau}\right)  + \rho\vec{g}\right]d\forall 
# \end{equation}
# 
# donde $\bar{I}$ es el tensor identidad.

# Combinando las ecuaciones (7.12) y (7.16), tenemos:
# 
# \begin{equation*}
# \frac{\partial}{\partial t}\left(\rho\vec{V}\right)  + \nabla\cdot\left(\rho\vec{V}\vec{V}\right) = - \nabla p + \nabla\cdot\bar{\tau} +  \rho\vec{g}
# \end{equation*}

# El termino de la izquierda se puede simplificar a partir de la ecuación de continuidad (7.11) para, finalmente, derivar la **ecuación de conservación de momento lineal en su forma diferencial**:
# 
# \begin{equation}
# \rho\frac{d\vec{V}}{dt} = - \nabla p + \nabla\cdot\bar{\tau} + \rho\vec{g}
# \end{equation}

# Esta ecuación también se conoce como la **Ecuación de Cauchy.**

# ## Referencias
# **Çengel Y. A. y Cimbala M. J. *Mecánica de Fluidos: Fundamentos y Aplicaciones*, 4ta Ed., McGraw Hill, 2018**
# - Capitulo 4. Cinemática de fluidos
# - Capitulo 9. Análisis diferencial de flujo de fluidos
# 
# **White F. M. *Mecánica de Fluidos*, 5ta Ed., McGraw Hill, 2004**
# - Capítulo 4. Relaciones diferenciales para una partícula fluida
# 
