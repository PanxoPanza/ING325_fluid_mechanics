#!/usr/bin/env python
# coding: utf-8

# # Máquinas hidráulicas

# ## Introducción

# Definimos como **bomba** a cualquier máquina hidráulica que *entrega* energía a un fluido. Por otro lado, definimos como **turbina** a las máquinas que *extraen* energía de un fluido.

# <img src="./figures/bombas_vs_turbinas.png" width="800px" align= center>

# ### Máquinas hidráulicas para líquidos
# En el caso de interacción con líquidos:
# 
# - **La energía suministrada por bombas se manifiesta como un aumento de presión del fluido**. La velocidad del fluido no aumenta, necesariamente.
# 
# - **La energía extraida por turbinas se manifiesta como un aumento de presión del fluido**. La velocidad del fluido no disminuye, necesariamente.

# <img src="./figures/hydraulic_pump_turbine.png" width="800px" align= center>

# ### Máquinas hidráulicas para gases
# 
# En el caso de gases, la clasificación del tipo de bomba depende de la función:
# - **Ventilador** diseñado para aumentar la velocidad ($V_\mathrm{sale}\gg V_\mathrm{entra}$), con un aumento mínimo en la presión ($\Delta P$, bajo).
# - **Compresor** diseñado para aumentar la presión ($\Delta P$, alto), con bajo aumento en la velocidad ($V_\mathrm{sale}\sim V_\mathrm{entra}$).

# <img src="./figures/gas_pump.png" width="800px" align= center>

# En el caso de turbinas, la transferencia de energía generalmente se manifiesta en una disminución de la velocidad o presión dependiendo del tipo. Por ejemplo, en el caso de turbinas abiertas, la velocidad cambia y la presión se mantiene apróximadamente constante.
# 
# <img src="./figures/wind_turbine.png" width="800px" align= center>
# 
# En turbinas cerradas, los gases experimentan cambios en ambos, presión y velocidad.

# ### Clasificación de máquinas hidráulicas
# 
# Existen dos grandes tipos de máquinas hidráulicas

# **Máquinas de desplazamiento positivo**
# El fluido se dirige hacia adentro de un *volúmen cerrado deformable o con fronteras móviles*, que permite la succión o impulsión del fluído.

# <img src="./figures/desplazamiento_positivo.png" width="800px" align= center>

# **Máquinas dinámicas** En este caso, el volúmen no es cerrrado. Los álabes rotatorios suministran energía al fluido o la extraen de él.

# Ejemplos de máquinas dinámicas son las bombas centrífugas y las turbinas hidráulicas.

# > En este curso nos enfocaremos en máquinas dinámicas. **Específicamente, bombas centrífugas y turbinas eólicas**

# ## Bombas

# ### Tipos de bombas

# #### Bombas de desplazamiento positivo
# Ideales cuando se necesitan altas presiones, como el bombeo de líquidos viscosos o mezclas, lodos, etc. También son útiles cuando se necesita despachar cantidades de líquido con precisión (aplicaciones médicas).
# 
# <img src="./figures/Bombas_de_desplazamiento_positivo.png" width="800px" align= center>

# **Ventajas**
# - Menor esfuerzo cortante inducido (mejor para líquidos sensibles al esfuerzo cortante, como sangre)
# - Es capaz de elevar un líquido varios metros debajo de la bomba
# - Menor velocidad de funcionamiento lo que prolonga la vida útil de los sellos

# **Desventajas**
# - Se requiere cambiar la velocidad de rotación para cambiar  el caudal (difícil)
# - Muy sensible a fallas por bloqueo en el flujo. Se necesitan válvulas de seguridad

# #### Bombas dinámicas
# 
# Ideales cuando se requiere proporcionar caudales altos. Podemos clasificarlas en tres tipos:
# 
# <img src="./figures/bombas_dinamicas.png" width="800px" align= center>

# Un ejemplo de bomba de flujo radial es la **bomba centrífuga**
# 
# <img src="./figures/centrifugal_pump.png" width="700px" align= center>

# **Ventajas** 
# - Entregan mayor caudal que las de desplazamiento positivo
# - Permiten una descarga más estacionaria, idependiente de los cambios de presión en el sistema.

# **Desventajas**
# - Poco efectivas para bombar líquidos muy viscosos
# - No pueden succionar líquido si están vacías (llenas de gas) y, por lo tanto, se debe remover el gas interior antes de arrancar el sistema (cebado de la bomba).

# ### Análisis teórico
# 
# Los **parámetros fundamentales** para caracterizar una bomba son:

# <img src="./figures/pump_analysis.png" width="350px" align= center>

# - Gasto volumétrico, $Q = \dot{m}/\rho,\quad(\mathrm{m}^3/s)$
# 
# - Carga hidrostática neta, $H_\mathrm{b} \approx \Delta P/\rho g,\quad(\mathrm{m})$
# 
# - Potencia útil: $
# \dot{W}_\mathrm{util} = \rho g QH_\mathrm{b},\quad(\mathrm{W})$
# 
# - Potencia al freno o de accionamiento $\dot{W}_\mathrm{bhp} = \omega M_\mathrm{flecha},\quad(\mathrm{W})$
# 
# - Eficiencia de la bomba $\eta_\mathrm{bomba} = \dot{W}_\mathrm{util}/\dot{W}_\mathrm{bhp}$
# 
# donde $\omega$ es la velocidad de rotación ($\mathrm{rpm}$) y $M_\mathrm{flecha}$ es el torque aplicado

# Estos parámetros están interrelacionados, y cambian según el caudal a suministrar. La gráfica está representada por las **curvas de rendimiento**

# <img src="./figures/curva_característica_bomba.png" width="350px" align= center>

# De está gráfica distinguimos tres puntos importantes:
# - Carga al cierre, $Q = 0$
# - Descarga libre, $H_b = 0$
# - Punto de máxima eficiencia o nominal, $\mathrm{PME}$

# En condiciones estacionarias, la bomba operará en su curva de rendimiento. Así, **el punto de operación** en un sistema de cañerías se determina cuando la **curva de demanda del sistema coincide con la curva de rendimiento de la bomba**. 

# <img src="./figures/punto_de_operacion.png" width="350px" align= center>

# En el punto de operación, la altura hidrostática requerida para impulsar el fluido por las cañerías, $H_\mathrm{req}$ y la altura hidrostática disponible por la bomba, $H_\mathrm{dis}$
# 
# \begin{equation*}
# H_\mathrm{req} = H_\mathrm{dis}
# \end{equation*}

# Consideremos el siguiente ejemplo

# <img src="./figures/ejemplo_punto_operacion.png" width="400px" align= center>

# Por balance de energía tenemos:
# \begin{equation*}
# H_\mathrm{b} = \left(\frac{V^2}{2g} + \frac{P}{\rho g} + z\right)\Bigg|_\mathrm{~entra}^\mathrm{~sale} + h_L
# \end{equation*}

# Evaluando a la entrada y salida, y la considerando la relación $Q = V_\mathrm{sale}A_d$, donde $A_d$ es el área transversal del ducto:
# 
# \begin{equation*}
# H_\mathrm{req}(Q) = \Delta z+\left(1 + f\frac{L}{D}+\sum_i K_i\right)\frac{Q^2}{2gA_d^2}
# \end{equation*}
# 
# > notar que $f$ depende de $\mathrm{Re}_D$ y $\varepsilon_R$

# Esta curva aumenta con $Q$. El punto de operación estará en la intersección de esta curva con la curva de rendimiento de la bomba

# En la práctica los fabricantes entregan una serie de curvas características (velocidad constante) que consideran varios diámetros de rodete para una misma carcaza.

# <div class="full-width">
# 
# <img src="./figures/curva_caracteristica.png" width="900px" align= center>
#     
# </div>

# En la gráfica se aprecia una curva de **carga de aspiración neta positiva (*net positive suction head*, NPSH** por sus siglas en ingles). Esta curva indica **el NPSH mínimo para evitar la cavitación de la bomba.**

# > La **cavitación** corresponde al desgaste en los álabes de la bomba producto del colapso de burbujas de vapor. Esto **se produce cuando la presión del líquido a la entrada de la bomba es menor que la presión de vapor a la temperatura de operación**.

# Para diseñar el sistema, el **NPSH real debe ser mayor o igual que el NPSH mínimo requerido**. 
# 

# <img src="./figures/NPSH.png" width="300px" align= center>

# El **NPSH real** se calcula a partir de un **balance de energía entre el punto de succión y la entrada de la bomba**, considerando el **caso crítico en que el fluido ingresa a la bomba a velocidad 0 y a la presión de vapor a la temperatura de operación ($P_v$)**.

# 
# 
# \begin{equation*}
# \mathrm{NPSH}_\mathrm{real} = \left(\frac{P}{\rho g} + \frac{V^2}{2g} + z\right)_\mathrm{succión} - h_L - z_\mathrm{entrada} - \frac{P_v}{\rho g}
# \end{equation*}

# ### Bombas en serie y paralelo
# Utilizamos sistemas de bombeos en serie y paralelo para aumentar la altura hidroestática o el caudal total, respectivamente.

# <img src="./figures/series_parallel_pump.png" width="800px" align= center>

# Al operar bombas en serie o paralelo, las curvas de rendimiento se modifican

# **Bombas en serie**
# <img src="./figures/series_pump_curve.png" width="700px" align= center>

# **Bombas en paralelo**
# <img src="./figures/parallel_pump_curve.png" width="700px" align= center>

# ## Referencias
# **Çengel Y. A. y Cimbala M. J. *Mecánica de Fluidos: Fundamentos y Aplicaciones*, 4ta Ed., McGraw Hill, 2018**
# - Capitulo 14: Turbomáquinas
# 
# **White F. M. *Mecánica de Fluidos*, 5ta Ed., McGraw Hill, 2004**
# - Capítulo 11: Turbomáquinas
