#!/usr/bin/env python
# coding: utf-8

# # Flujo externo

# En este capítulo revisaremos el flujo alrededor de cuerpos que están inmersos en un fluido. Categorizamos este tipo de casos como *Flujo externo*.

# <img src="./figures/intro.jpg" width="600px" align= center>

# En el flujo externo estudiamos las **fuerzas resultantes** que ocurren en cuerpos producto de la presión y esfuerzo cortante en un cuerpo.
# 
# <img src="./figures/drag_and_lift_force.png" width="800px" align= center>

# La fuerza resultante se descompone en: 
# - **Fuerza de arrastre** ($F_D$) que corresponde a la componente en la dirección del flujo
# - **Fuerza de sustentación** ($F_L$) que  corresponde a la componente perpendicular al flujo

# >La fuerza resultante se asocia al movimiento relativo entre el flujo y el cuerpo. Es decir, un cuerpo en reposo sometido a un flujo externo, o un cuerpo moviendose dentro de un fluido en reposo

# En base a la figura anterior, ambas componentes se pueden expresar matemáticamente como:
# 
# \begin{align*}
# F_D &= \int_A (-P\cos\theta + \tau_w\sin\theta)dA
# \\
# F_L &= \int_A (-P\sin\theta - \tau_w\cos\theta)dA
# \end{align*}

# Las ecuaciones permiten entender conceptualmente el efecto de la presión ($P$) y esfuerzo cortante ($\tau_w$) en el arrastre y sustentación.

# Estas ecuaciones, sin embargo, tienen poca aplicación práctica debido a la dificultad de predecir la distribución de $P$ y $\tau_w$.

# In[1]:


from IPython.display import YouTubeVideo
YouTubeVideo('nl75BGg9qdA', width=700, height=400)


# ## Referencias
# **Çengel Y. A. y Cimbala M. J. *Mecánica de Fluidos: Fundamentos y Aplicaciones*, 4ta Ed., McGraw Hill, 2018**
# - Capitulo 5: Ecuaciones de Bernoulli y de la energía
# - Capítulo 8: Flujo en tuberías
# 
# **White F. M. *Mecánica de Fluidos*, 5ta Ed., McGraw Hill, 2004**
# - Capítulo 3.6: Ecuación de la energía
# - Capítulo 3.7: Flujo sin fricción: La ecuación de Bernoulli
# - Capítulo 6: Flujo viscoso en conductos
