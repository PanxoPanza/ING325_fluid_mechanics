#!/usr/bin/env python
# coding: utf-8

# # Introducción a la dinámica de fluidos: Conservación de masa

# ## Sistema y volúmen de control

# ### Sistema

# Definimos como **sistema** a una *cantidad de materia de masa fija elegida para el estudio*

# En general, para el estudio de **sólidos**, la definición de sistema es sencilla, ya que este considera la interacción del cuerpo con las fuerzas externas.

# Sin embargo, en el caso de **fluidos**, la definición no es tan sensilla ya que el sistema ocupa un espacio infinito.

# ### Volumen de control

# Para estudiar dinámica de fluidos utilizamos el **volúmen de control**, *una región imagniaria en el espacio para analizar la dinámica de fluidos.*

# <img src="./figures/control_volume.png" width="700px" align= center>
# 
# >**Nota.** Las frontera de un volumen de control pueden ser permeables o impermeables, móbiles o fijas.

# ## Descripción lagrangiana y euleriana

#  - **Descripción lagrangiana** consiste en hacer un seguimiento de las partículas materiales. Este enfoque es comúnmente utilizado en dinámica de sólidos.
# 
# - **Descripción euleriana** consiste en medir lo que pasa en puntos fijos del espacio. Este enfoque es comúnmente utilizado en dinámica de sólidos.

# <img src="./figures/lagrangian_eulerian.png" width="800px" align= center>

# **En el análisis lagrangiano se rastrea la *trayectoria y la velocidad de cada sistema,*** las cuales dependen del tiempo ($t$), únicamente. Por ejemplo, considerando un sistema con múltiples objetos $A, B, C, \cdots$
# 
# \begin{align*}
# \vec{x}_A(t), \vec{x}_B(t), \vec{x}_C(t), \cdots&\quad\quad\mathrm{Trayectoria}\\
# \vec{V}_A(t), \vec{V}_B(t), \vec{V}_C(t), \cdots&\quad\quad\mathrm{Velocidad}
# \end{align*}
# 

# **En el análisis euleriano se definen *variables de campo***, es decir, variables en funcion del tiempo y del espacio  dentro del volumen de control ($x, y,z$). Por ejemplo:
# \begin{align*}
# P(x,y,z,t) &\quad\quad\mathrm{Campo~de~presión}\\
# \rho(x,y,z,t) &\quad\quad\mathrm{Campo~de~densidad}\\
# \vec{V}(x,y,z,t) &\quad\quad\mathrm{Campo~de~velocidad}
# \end{align*}

# Notar que $P$ y $ \rho$ son un **campo escalar *(valor escalar que cambia en el espacio)***, mientras que $\vec{V}$ es un **campo vectorial *(vector cuya magnitud y dirección cambia en el espacio)***

# Así, $\vec{V}$ se puede desarrollar, por ejemplo, en coordenadas cartesianas:
# 
# \begin{equation}
# \vec{V} = u(x,y,z,t)~\hat{x} + v(x,y,z,t)~\hat{y} + w(x,y,z,t)~\hat{z}
# \end{equation}
# 
# donde $u$, $v$ y $w$ son las componentes de la velocidad e direcciones $x$, $y$ y $z$, respectivamente.

# **Ambos enfoques son equivalentes.** Así, existen ocaciones donde el enfoque lagrangiano se aplica a problemas de fluidos, y viceversa.  

# In[1]:


from IPython.display import YouTubeVideo
YouTubeVideo('OWfHoB_t948', width=800, height=500)


# En el video vemos el proceso de mezcla de material partículado (no un fluido). Similarmente, esta herramienta se puede utilizar para modelar un fluído considerando las fuerzas de interacción entre partículas.

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
#         (\vec{V}\cdot\nabla)\vec{V}
# \end{align}
# 
# donde $\nabla = \frac{\partial}{\partial x}\hat{x} + \frac{\partial}{\partial y}\hat{y} + \frac{\partial}{\partial z}\hat{z}$, es el **operador nabla**

# Hemos definido un nuevo operador, denominado **derivada material (o sustancial), $\frac{D}{Dt}$ o $\frac{d}{dt}$** que describe la *variación temporal de una partícula de fluido a medida que se mueve por el campo de flujo:*
# 
# \begin{equation}
# \frac{d}{dt} = \frac{\partial}{\partial t} + \vec{V}\cdot\nabla
# \end{equation}

# - El término $\frac{\partial}{\partial t}$ se denomina **variación temporal local y *es cero para flujos estacionarios.***

# - El término $(\vec{V}\cdot\nabla)$, se denomina **término convectivo, *este término puede ser diferente de cero inclusive para flujos estacionarios***

# La derivada material se puede aplicar a otras propiedades de fluidos, como por ejemplo, la densidad:
# 
# \begin{equation*}
# \frac{d\rho}{dt} = \frac{\partial\rho}{\partial t} + \vec{V}\cdot\nabla\rho
# \end{equation*}

# ## Teorema de transporte de Reynolds (TTR)

# ### Leyes de conservación aplicadas a un sistema

# Consideremos algunas **leyes de conservación fundamentales** aplicadas a un sistema:

# - Masa ($m_\mathrm{sys}$), 
# 
# $$\frac{d}{dt}m_\mathrm{sys} = 0$$
# 
# - Momento lineal $(m\vec{V})_\mathrm{sys}$, 
# 
# $$\frac{d}{dt}(m\vec{V})_\mathrm{sys} = \vec{F}_\mathrm{neta}$$

# - Momento angular $(\vec{r}\times m\vec{V})_\mathrm{sys}$, 
# 
# $$\frac{d}{dt}(\vec{r}\times m\vec{V})_\mathrm{sys} = \vec{M}_\mathrm{neto}$$
# 
# - Energía $E_\mathrm{sys} =(m\tilde{e})_\mathrm{sys}$, 
# 
# $$\frac{d}{dt}(m\tilde{e})_\mathrm{sys} = \dot{Q} - \dot{W}$$

# donde $\vec{F}_\mathrm{neta}$ y $\vec{M}_\mathrm{neto}$ son, respectivamente, *la fuerza y torque aplicado sobre el sistema*, $\tilde{e}$ es la *energía específica (energía por unidad de masa)*, $\dot{Q}$ es la *tasa de transferencia de calor*, y $\dot{W}$ es *potencia*.

# En cada ley de conservación notamos que hay una ***propiedad extensiva (por ejemplo, $E_\mathrm{sys}$)***, y una ***propiedad intensiva (por ejemplo, $\tilde{e}_\mathrm{sys} = E_\mathrm{sys}/m_\mathrm{sys}$)***

# ### Formulación general
# 
# El **teorema de transporte de Reynolds** establece una relación entre la **variación temporal de una propiedad extensiva del sistema ($B_\mathrm{sys}$)** y su respectiva **propiedad intensiva dentro del volumen de control ($\beta$)**

# En su forma más general, para un **volumen de control móvil y deformable**:
# 
# \begin{equation}
# \frac{d}{dt}B_\mathrm{sys} = \frac{d}{dt}\int_\mathrm{VC} \rho\beta d\forall + \int_\mathrm{VC} \rho\beta\vec{V}\cdot\hat{n}dA
# \end{equation}

# - El término a la izquierda representa la **tasa de cambio de $B_\mathrm{sys}$ en el sistema.**
# 
# - El primer término a la derecha representa la **tasa de cambio de $\beta$ en el volúmen de control $\mathrm{VC}$.**
# 
# - El segundo término a la derecha representa el **flujo de $\beta$ a través de las fronteras del volúmen de control ($\mathrm{VC}$)**

# <img src="./figures/Reynolds_theorem_general.png" width="350px" align= center>

# Notar que el rol de la normal a la superficie del volumen de control ($\hat{n}$) en la ecuación, que define un **valor positivo para flujos que salen del volúmen de control**, y un **valor negativo para los flujos que entran**.

# Matemáticamente, el flujo neto de $B$ en el volúmen de control:
# 
# \begin{equation*}
# \dot{B}_\mathrm{neto} = \dot{B}_\mathrm{sale} - \dot{B}_\mathrm{entra} = \int_\mathrm{VC} \rho\beta\vec{V}\cdot\hat{n}dA
# \end{equation*}

# ### Simplificaciones

# **Caso 1:** Volumen de control fijo
# 
# \begin{equation}
# \frac{d}{dt}B_\mathrm{sys} = \int_\mathrm{VC} \frac{\partial}{\partial t}(\rho\beta) d\forall + \int_\mathrm{VC} \rho\beta\vec{V}\cdot\hat{n}dA
# \end{equation}

# **Caso 2:** Flujo estacionario
# 
# \begin{equation}
# \frac{d}{dt}B_\mathrm{sys} = \int_\mathrm{VC} \rho\beta\vec{V}\cdot\hat{n}dA
# \end{equation}

# **Caso 3:** Valores promedio en la entrada y salida
# 
# \begin{equation}
# \frac{d}{dt}B_\mathrm{sys} = \int_\mathrm{VC} \frac{\partial}{\partial t}(\rho\beta) d\forall + \sum_\mathrm{sale}\overline{\rho}\overline{\beta}\overline{V}A - \sum_\mathrm{entra}\overline{\rho}\overline{\beta}\overline{V}A
# \end{equation}

# En la última fórmula, el símbolo $\bar{b}$ representa el **valor promedio por área de una variable $b$:**
# 
# \begin{equation}
# \bar{b} = \frac{1}{A}\int_A bdA
# \end{equation}

# La aproximación es útil en muchas aplicaciones prácticas de ingeniería, donde solo se conocen valores promedios del flujo en base a mediciones.

# ## Ecuación de conservación de masa

# ### Formulación general

# En el caso de la conservación de masa del sistema
# 
# $$\frac{d}{dt}m_\mathrm{sys} = 0$$

# Aplicando el teorema de transporte de Reynold con $B_\mathrm{sys} = m_\mathrm{sys}$ y $\beta = 1$, deducimos la ecuación de **conservación de masa para un volúmen de control**:
# 
# \begin{equation}
# 0 = \frac{d}{dt}\int_\mathrm{VC} \rho d\forall + \int_\mathrm{VC} \rho\vec{V}\cdot\hat{n}dA
# \end{equation}

# Lidiamos con la ecuación de conservación de masa a menúdo en nuestra vida cotidiana
# 
# <img src="./figures/conservacion_masa_manguera.png" width="700px" align= center>

# Aplicando la ecuación de conservación de masa al ejemplo, tenemos:
# 
# \begin{equation*}
# 0 = 0 + \rho V_2 A_2 - \rho V_1 A_1 \Rightarrow 
# V_2 = V_1 \frac{A_1}{A_2}
# \end{equation*}

# Debido a que $A_1 > A_2$, entonces:
# 
# \begin{equation*}
# V_2 > V_1
# \end{equation*}

# ### Variables relevantes
# 
# Aprovechamos esta ecuación para definir algunas variables relevantes:

# **Flujo másico ($\dot{m}$),** se define como la tasa de cambio de la mása que cruza un área, matemáticamente:
# 
# \begin{eqnarray}
# \begin{split}
# \dot{m} &= \int_A \rho \vec{V}\cdot\hat{n}dA &\quad\left(\mathrm{\frac{kg}{s}}\right) &\quad\mathrm{(fórmula~general)}
# \\
# \dot{m} &= \overline{\rho} \overline{V}A &\quad\left(\mathrm{\frac{kg}{s}}\right) &\quad\mathrm{(valores~promedio)}
# \end{split}
# \end{eqnarray}

# **Caudal ($Q$),** se define como la tasa de cambio del volúmen de fluido que cruza un área, matemáticamente:
# 
# \begin{eqnarray}
# \begin{split}
# Q &= \int_A \vec{V}\cdot\hat{n}dA&\quad\left(\mathrm{\frac{m^3}{s}}\right) &\quad\mathrm{(fórmula~general)}
# \\
# Q &=  \overline{V}A &\quad\left(\mathrm{\frac{m^3}{s}}\right) &\quad\mathrm{(valores~promedio)}
# \end{split}
# \end{eqnarray}

# > El caudal se usa comúnmente en líquidos, debido a que son incompresibles ($\rho$ no cambia).

# ### Ejemplo

# <img src="./figures/estanque.png" width="350px" align= center>

# Un tanque cilíndrico abierto a la atmósfera está lleno con agua. Al quitar el tapón de descarga, la velocidad promedio a la salida es $V = \sqrt{2gh}$, donde $h$ es el nivel instantáneo de agua en el tanque
# medida desde el centro del agujero, y $g$ es la aceleración de gravedad. **Determíne el tiempo para que el nivel del agua descienda de $h_0$ hasta $h_2$.**

# ## Referencias
# **Çengel Y. A. y Cimbala M. J. *Mecánica de Fluidos: Fundamentos y Aplicaciones*, 4ta Ed., McGraw Hill, 2018**
# - Capitulo 4.1: Descripciones lagrangiana y euleriana
# - Capítulo 4.6: Teorema de transporte de Reynolds
# - Capítulo 5.2: Conservación de la masa
# 
# **White F. M. *Mecánica de Fluidos*, 5ta Ed., McGraw Hill, 2004**
# - Capítulo 3.1: Leyes básicas de la mecánica de fluidos
# - Capítulo 3.2: Teorema de transporte de Reynolds
# - Capítulo 3.3: Conservación de masa
