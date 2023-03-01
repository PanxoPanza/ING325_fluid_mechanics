#!/usr/bin/env python
# coding: utf-8

# <font size="6">ING325 - Mecánica de Fluidos</font>
# # Introducción a la mecánica de fluidos
# <br><br><br><br>
# Profesor: Francisco Ramírez Cuevas<br>
# Fecha: 2 de Marzo 2023

# ## Aspectos generales

# ### Definición de un fluido
# 
# - Sustancia en fase líquida o gaseosa
# - En comparación con un sólido, los enlaces entre moléculas son débiles y no elásticos.

# <img src="./figures/matter_phase.png" width="650px" align= center>

# A partir de esta configuración molecular:
# - Un sólido se caracteriza por ser un elemento rígido que opone resistencia ante un esfuerzo (dentro del límite elástico)
# - Un fluido, en cambio, se deforma constantemente tomando la forma del recipiente que lo contiene.

# 
# <img src="./figures/solid_vs_fluid.png" width="600px" align= center>

# - En el caso de un líquido, **el volumen del fluido se mantiene relativamente constante** debido a las fuerzas de cohesión. Así, un líquido forma una superficie libre.
# - El gas, por otro lado, se expande constantemente ya que las fuerzas de coheción son débiles.

# ### Clasificación de flujos

# ***Flujo externo/interno.***
# Se define dependiendo si el fluido fluye por un canal confinado (interno), o sobre alrededor de una superficie (externo).

# 
# <img src="./figures/external_vs_internal_flow.png" width="700px" align= center>

# ***Flujo compresible/incompresible.*** Corresponde a la variación de la densidad (masa/volumen) del fluido en un flujo.
# - Flujo incompresible: la densidad se mantiene relativamente constante
# - Flujo compresible: la densidad varía en el flujo

# Como regla general, **el flujo con líquidos es típicamente incompresible**. En el caso de **gases, los flujos se pueden aproximar como incompresibles cuando $\mathrm{Ma} < 0.3$**, donde
# 
# \begin{equation*}
# \mathrm{Ma} = \frac{\mathrm{Velocidad~del~flujo}}{\mathrm{Velocidad~del~sonido}},
# \end{equation*}
# 
# es el **número de Mach.**

# ***Flujo Laminar/Turbulento.*** Define el grado de orden de un flujo

# 
# <img src="./figures/laminar_vs_turbulent.png" width="400px" align= center>

# - Flujo laminar: flujo suave y ordenado donde las líneas de flujo adyacentes se mueve en forma de láminas (o capas). Se presenta comúnmente en flujos a bajas velocidades
# 
# - Flujo turbulento: caracterizado por fluctuaciones caóticas, comúnmente en velocidades altas.

# ***Flujo transiente/estacionario*** define la variación temporal de un flujo.

# <img src="./figures/stationary_flow.png" width="380px" align= center>

# Un flujo es estacionario si no hay cambio de las propiedades en un punto con el tiempo. En caso contrario, el flujo es transciente.
# 
# Si el flujo es estacionario las propiedades del fluido pueden cambiar en el espacio, pero en un punto fijo permanecen constantes.

# ### Mécanica de fluidos en la ingeniería
# Existen innumerables aplicaciones donde la mecánica de fluidos juega un rol central, tales como conversión de energía, procesos industriales (como minería), medio ambiente, aerodinámica, etc.

# <img src="./figures/aplicaciones.png" width="800" align= center>

# ## Propiedades de los fluidos

# ### Densidad y variables asociadas

# **Densidad ($\rho$).** Se define como *la masa por unidad de volúmen*.

# Comúnmente se mide en $\mathrm{kg/m^3}$ o $\mathrm{g/cm^3}$.

# El recíproco de la densidad es el **volumen específico** $v = 1/\rho$.

# La densidad de una sustancia depende de la temperatura y la presión:

# - **Líquidos.** ***La variación de la densidad con la presión es despreciable***. Por ejemplo, la densidad del agua a $20°\mathrm{C}$ cambia de $998~\mathrm{kg/m}^3$ a $1~\mathrm{atm}$ a $1003~\mathrm{kg/m}^3$ a $100~\mathrm{atm}$. ***Frente a cambios de temperatura, la densidad sufre cambios un poco más significativos, aunque es posible despreciarlos en algunos casos.***

# 
# 
# - **Gases.** ***Generalmente obedecen a la ley de gas ideal $PMv=RT$***, donde $P$ es la presión absoluta, $M$ es la masa molar del gas, $T$ es la temperatura y $R = 8.3145~\mathrm{kJ/kmol~K}$ es la constante universal del gas ideal.

# **Gravedad específica ($\mathrm{GE}$).** Se define como *la razón de la densidad de una sustancia a la densidad de una sustancia estándar, a una temperatura específica* (por lo general, agua a $4°\mathrm{C}$, tal que $\rho_{\mathrm{H}_2\mathrm{O}} = 1000~\mathrm{kg/m}^3$).

#  Es decir:
# \begin{equation}
# \mathrm{GE} = \frac{\rho}{\rho_{\mathrm{H}_2\mathrm{O}}}
# \end{equation}

# <img src="./figures/specific_gravity.png" width="300" align= center>

# **Peso específico ($\gamma$).** Se define como el *peso por unidad de volúmen*, y se expresa como:
# 
# \begin{equation}
# \gamma = \rho g\quad\quad\frac{\mathrm{N}}{m^3}
# \end{equation}
# 
# donde $g$ es la aceleración gravitacional.

# ### Viscosidad
# 
# Corresponde a la resistencia de un fluido al movimiento o, en otras palabras, a la "fluidez". **Esta propiedad establece una relación entre los esfuerzos cortantes ($\tau$) y la taza de deformación de un fluido.**

# Recordemos que, a diferencia de un sólido, un fluido se deforma constantemente frente a un esfuerzo cortante. Así, **en el caso de fluidos es importante considerar *la taza de cambio de la deformación en el tiempo***, y no la deformación instantanea (como en el caso de sólidos).

# Un ejemplo simple es el que se ilustra en la figura. En este caso, el cuerpo (sólido o líquido) entre dos placas planas es sometido a una fuerza cortante debido al movimiento relativo entre ellas.
# <img src="./figures/fluid_solid.png" width="600" align= center>

# Al aplicar una fuerza $F$ constante, el fluido se deforma contínuamente, mientras que el sólido alcanza una deformación máxima (bajo el límite elástico del sólido). En ambos casos, **el esfuerzo cortante se define como $\tau = F/A$ donde $A$ es el área de contacto entre el cuerpo y la placa.**

# Matemáticamente, **la taza de deformación** corresponde al ***cambio de la velocidad de un fluido en el espacio***. En el ejemplo, el movimiento de las placas induce un perfil de velocidades como se indica en la figura, donde $u$ es la velocidad en la dirección $x$.

# <img src="./figures/deformation_rate.png" width="300px" align= center>

# En algunos fluidos (como el agua, aire y aceites), la taza de deformación es proporcional al esfuerzo cortante
# 
# \begin{equation}
# \tau = \mu\frac{du}{dy},\quad\quad\frac{\mathrm{N}}{\mathrm{m}^2}
# \end{equation}
# 
# y se denominan **fluidos newtonianos.** 

# En esta relación $\mu$ es la **viscocidad dinámica**. Comúnmente, se mide en $\mathrm{kg/m}\cdot\mathrm{s}$,  $\mathrm{Pa}\cdot\mathrm{s}$, o *centipose* $\mathrm{cP} = 0.001~\mathrm{kg/m}\cdot\mathrm{s}$. 

# En un fluido newtoniano, la gráfica esfuerzo de corte vs taza de deformación sigue una línea recta cuya pendiente está defnida por $\mu$.

# 
# <img src="./figures/newtonian_fluids.png" width="700" align= center>

# Los fluidos que no siguen esta relación lineal se conocen como **no newtonianos.**

# 
# <img src="./figures/non-newtonian_fluid.png" width="300" align= center>

# En esta categoría tenemos:
# - ***Seudoplástico,*** tales como pinturas, y otros fluidos con partículas en suspención.
# - ***Dialante,*** tales como soluciones con almidon o arena.
# - ***Plástico de Bingham,*** tales como Pasta de dientes, mayonesa, ketchup, etc.

# Un ejemplo interesante de un fluido no newtoniano, es la mezcla de almidón de maíz con agua (también conocida *Oobleck*). Otro ejemplo conocido, es el *Slime*.

# In[1]:


from IPython.display import YouTubeVideo
YouTubeVideo('RIUEZ3AhrVE', width=700, height=400)


# Con frecuencia, en algunas ecuaciones aparece la razón entre la viscocidad dinámica y a densidad. Esta variables, denominada **viscocidad cinemática  ($\nu = \mu/\rho$),** representa la capacidad de fluidez frente a la fuerza de gravedad.

# <img src="./figures/Viscosities.gif" width="400" align= center>

# Generalmente, ambas viscocidades cambian proporcionalmente
# 
# <img src="./figures/viscosity_table.png" width="450" align= center>

# Debido a que los métodos para medir viscocidad cinemática y dinámica son diferentes, es común encontrar ambas unidades en tablas

# <img src="./figures/viscocity_vs_temperature.png" width="400" align= center>

# El cambio en la viscocidad con la temperatura es diferente dependiendo de si es un gas o un líquido.

# Si la temperatura aumenta: 
# - **líquidos:** $\mu$ disminuye.
# 
# - **gases:** $\mu$ aumenta.

# Esto ocurre debido a las diferencias en la estructura molecular de gases y líquidos

# ## Referencias
# **Çengel Y. A. y Cimbala M. J. *Mecánica de Fluidos: Fundamentos y Aplicaciones*, 4ta Ed., McGraw Hill, 2018**
# - Capitulo 1: Introducción y conceptos básicos
# - Capítulo 2: Propiedades de los fluidos
# 
# **White F. M. *Mecánica de Fluidos*, 5ta Ed., McGraw Hill, 2004**
# - Capitulo 1: Introducción
