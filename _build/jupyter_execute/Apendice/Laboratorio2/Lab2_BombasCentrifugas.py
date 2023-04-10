#!/usr/bin/env python
# coding: utf-8

# # Laboratorio 2: Bombas Centrifugas

# ## Descripción de la práctica

# El objetivo de esta experiencia es estudiar y comprender las curvas caracterisiticas de una bomba centrifuga y la utilización de esta en un sistema de conducción de flujo de fluido.

# <img src="./figuras/banco_de_ensayo.jpg" width="600px" align= center>
# 
# <center> Banco de ensayo de bombas centrífugas</center>

# La experiencia consiste en medir el caudal y la diferencia de presiones que sufre el agua al circular a través de una bomba centrífuga. Estos valores serán contrastados con la potencia de la bomba, la cual se determinará a través del potencial eléctrico (voltaje) y corriente suministrados. Por último, la temperatura del agua también será monitoriada para posterior estimación de la densidad y viscosidad.
# 
# La experiencia considera el ensayo con una bomba, y luego con dos bombas en paralelo.

# ## Metodología experimental

# El video a continuación detalla los pasos para poder llevar a cabo la experiencia

# In[1]:


from IPython.display import YouTubeVideo
YouTubeVideo('SqieHq9g4Ig', width=600, height=400,  playsinline=0)


# ### Ensayo con una bomba. Resumen de los pasos 

# **Paso 1. Configuración del sistema**
# 
# 1. Encender equipo desde el panel principal
# 2. Girar reostato en el panel izquierdo hasta obtener una velocidad de 2600 rpm.
# 3. Verificar que la válvula de compuerta este 100% abierta

# **Paso 2. Registrar diferencia de presiones, voltaje y corriente en función del caudal**
# 1. Cronometrar el tiempo en el que pasan 10 litros (0.01m$^3$) en el medidor de volúmen
# 2. Registrar las presiones a la entrada y salida de la bomba
# 3. Registrar la diferencia de potencial indicada en el voltímetro (panel a la izquierda)
# 4. Registrar la corriente indicada en el amperímetro (panel a la izquierda)
# 5. Registrar temperatura del agua
# 6. Girar la válvula en 180° en dirección del reloj
# 7. Repetir desde el punto 1

# **Paso 3. Detener el sistema**
# 1. Reducir la velocidad de giro a 0 rpm
# 2. Apagar el equipo girando el switch principal

# ### Ensayo con dos bombas en paralelo. Resumen de los pasos 

# **Paso 1. Configuración del sistema**
# 
# 1. Encender equipo desde el panel principal
# 2. Girar ambos reostatos en el panel izquierdo hasta obtener una velocidad de 2600 rpm en cada bomba
# 3. Verificar que la válvula de compuerta superior este 100% abierta
# 4. Verificar que la válvula de compuerta inferior este cerrada

# **Paso 2. Registrar diferencia de presiones, voltaje y corriente en función del caudal**
# 
# *Repetir los pasos indicados en el paso 2 del ensayo anterior*

# **Paso 3. Detener el sistema**
# 1. Reducir la velocidad de giro a 0 rpm en ambas bombas
# 2. Apagar el equipo girando el switch principal

# ## Actividades a realizar
# Posterior a la experiencia, se deben realizar las siguientes actividades. Los resultados de estas actividades deben ser detalladas en el informe

# ### Actividad 1. Obtención de curvas características de una bomba centrífuga
# 
# Representar gráficamente las curvas caracterísitcas de una bomba centrífuga girando a aproximadamente $2600~\mathrm{rpm}$.
# 
# 1. Altura hidrostática, $H_m$ ($\mathrm{m.c.a}$)
# 2. Potencia de accionamiento, $P_a$ ($\mathrm{kW}$)
# 3. Potencia util, $P_u$ ($\mathrm{kW}$)
# 4. Eficiencia de la bomba, $\eta_t$ ($\%$)

# ### Actividad 2. Obtención de curvas características de dos bomba centrífugas en paralelo
# 
# Representar gráficamente las curvas características de bombas centrífugas conectadas en paralelo girando a aproximadamente $2600~\mathrm{rpm}$.
# 
# 1. Altura hidrostática, $H_m$ ($\mathrm{m.c.a}$)
# 2. Potencia de accionamiento, $P_a$ ($\mathrm{kW}$)
# 3. Potencia util, $P_u$ ($\mathrm{kW}$)
# 4. Eficiencia de la bomba, $\eta_t$ ($\%$)

# ### Actividad 3. Ejercicio propuesto
# Resolver el ejercicion propuesto al final la experiencia
