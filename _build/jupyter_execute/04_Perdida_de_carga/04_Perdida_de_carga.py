#!/usr/bin/env python
# coding: utf-8

# # Conservación de energía y pérdida de carga en ductos

# ## Ecuación de conservación de energía

# A partir del teorema de transporte de Reynolds, y considerando la propiedad intensiva de la energía, $\tilde{e}$, definida como la **energía por unidad de masa** ($\mathrm{kJ/kg}$, por ejemplo), tenemos que la **ecuación de conservación de energía aplicada a un volúmen de control** es:

# \begin{equation}
# \dot{Q} - \dot{W} = \frac{d}{dt}\int_\mathrm{VC} \rho\tilde{e}d\forall + \int_\mathrm{VC} \rho\tilde{e}\vec{V}\cdot\hat{n}dA,\quad(\mathrm{kW})
# \end{equation}

# donde:
# - $\dot{Q}$, tasa de transferecia calor recibida por el sistema ($\mathrm{kW}$)
# - $\dot{W}$, tasa de trabajo (potencia) entregada por el sistema ($\mathrm{kW}$)

# ### Energía del fluido ($\tilde{e}$)
# 
# Considera todas las formas de energía presentes en el fluido:
# 
# \begin{equation*}
# \tilde{e} = \tilde{e}_\mathrm{interna} + \tilde{e}_\mathrm{cinética} + \tilde{e}_\mathrm{potencial} + \cdots, \quad\left(\mathrm{\frac{kJ}{kg}}\right)
# \end{equation*}
# 
# donde:
# - $\tilde{e}_\mathrm{interna} = \tilde{u}$ (energía interna)
# - $\tilde{e}_\mathrm{cinética} = \frac{V^2}{2}$ (energía cinética)
# - $\tilde{e}_\mathrm{potencial} = gz$ (energía potencial)
# 
# > $V$ es la velocidad promedio del fluido, $z$ es la altura medida desde un punto de referencia común, y $g$ es la aceleración de gravedad.

# ### Transferencia de calor ($\dot{Q}$)
# 
# Energía asociada al calor transferido por diferencia de temperaturas. 
# >Notar que $\dot{Q} < 0$ si el volúmen de control pierde calor

# ### Transferencia de trabajo ($\dot{W}$)
# 
# Considera el trabajo entregado o recibido por el sistema.
# >Notar que $\dot{W} < 0$ si el sistema recibe trabajo.

# Distinguimos tres formas principales de trabajo:

# - **Trabajo de eje ($\dot{W}_\mathrm{eje}$),** asociado al trabajo intercambiado con maquinarias, por ejemplo, trabajo de bombas ($\dot{W}_\mathrm{eje} < 0$), turbinas ($\dot{W}_\mathrm{eje} > 0$), ventiladores ($\dot{W}_\mathrm{eje} < 0$), etc.
# 

# - **Trabajo por presiones ($\dot{W}_\mathrm{presion}$),** asociado al trabajo de presiones del fluido. Actúa solo en las fronteras del volúmen de control:
# 
#     \begin{equation*}
#     \dot{W}_\mathrm{presion} = \int_{VC} P(\vec{V}\cdot\hat{n})dA
#     \end{equation*}

#  - **Trabajo por fuerzas viscosas ($\dot{W}_\mathrm{viscosas}$),** asociado a la disipación de energía por fricción como resultado de viscosidad del fluido ($\dot{W}_\mathrm{viscosas}$ > 0).

# ## Formulaciones prácticas
# 
# La ecuación de la energía mostrada (4.1) no tiene mucho uso práctico en la ingeniería, debido a que los trabajos asociados a la presión y viscosidad están implícitos en la ecuación. 

# El primer paso es, entonces, determinar una expresión general que separe el trabajo de eje de otros. Una vez obtenida esta expresión, derivaremos otras expresiones prácticas para el análisis de problemas de ingeniería.

# ### Forma general de la ecuación de conservación de energía
# 
# Aplicando las ecuaciones comentadas anteriormente, la ecuación de conservación de energía es:
# 
# <div class="full-width">
# <p style="line-height:2.0em;"></p>
#     
# \begin{equation}
# \dot{Q} - \dot{W}_\mathrm{eje} - \dot{W}_\mathrm{viscoso}  = \frac{d}{dt}\int_\mathrm{VC} \rho\left(\tilde{u}+\frac{V^2}{2}+gz\right)d\forall + \int_\mathrm{VC} \rho\left(\tilde{h}+\frac{V^2}{2}+gz\right)\vec{V}\cdot\hat{n}dA,\quad(\mathrm{kW})
# \end{equation}
#     
#  </div>
#     
# donde $\tilde{h} = \tilde{u} + P/\rho$ es la **entalpía o *energía de flujo* del fluido.**

# ### Otras formulaciones prácticas
# A partir de la ecuación (4.2) podemos derivar otras relaciones prácticas

# **Caso 1: Conservación de energía mecácica (isotérmico y adiabático)**
# 
# En este caso, $\dot{Q} = 0$ y la energía interna es constante. La ecuación de conservación de energía se simplifica a: 
# 
# <div class="full-width">
# <p style="line-height:2.0em;"></p>
#     
# \begin{equation}
# - \dot{W}_\mathrm{eje} - \dot{W}_\mathrm{viscoso}  = \frac{d}{dt}\int_\mathrm{VC} \rho\left(\frac{V^2}{2}+gz\right)d\forall + \int_\mathrm{VC} \rho\left(\frac{P}{\rho}+\frac{V^2}{2}+gz\right)\vec{V}\cdot\hat{n}dA,\quad(\mathrm{kW})
# \end{equation}
#     
# </div>

# **Caso 2: Valores promedio a la entrada y salida + caso 1**
# 
# <div class="full-width">
# <p style="line-height:2.0em;"></p>
#     
# \begin{equation}
# - \dot{W}_\mathrm{eje} - \dot{W}_\mathrm{viscoso}  = \frac{d}{dt}\int_\mathrm{VC} \rho\left(\frac{V^2}{2}+gz\right)d\forall +\sum_\mathrm{sale}\left(\frac{P}{\rho}+\frac{V^2}{2}+gz\right)\dot{m} - \sum_\mathrm{entra}\left(\frac{P}{\rho}+\frac{V^2}{2}+gz\right)\dot{m},\quad(\mathrm{kW})
# \end{equation}
#     
# </div>
# 

# **Caso 3: Propiedades constantes dentro del V.C + caso 1  + caso 2**
# 
# <div class="full-width">
# <p style="line-height:2.0em;"></p>
#     
# \begin{equation}
# - \dot{W}_\mathrm{eje} - \dot{W}_\mathrm{viscoso}  = \frac{d}{dt}\left[\rho\left(\frac{V^2}{2}+gz\right)\forall\right] +\sum_\mathrm{sale}\left(\frac{P}{\rho}+\frac{V^2}{2}+gz\right)\dot{m} - \sum_\mathrm{entra}\left(\frac{P}{\rho}+\frac{V^2}{2}+gz\right)\dot{m},\quad(\mathrm{kW})
# \end{equation}
#     
# </div>
# 

# **Caso 4: Problema estacionario + caso 1  + caso 2 + caso 3**
# 
# <div class="full-width">
# <p style="line-height:2.0em;"></p>
#     
# \begin{equation}
# - \dot{W}_\mathrm{eje} - \dot{W}_\mathrm{viscoso}  = \sum_\mathrm{sale}\left(\frac{P}{\rho}+\frac{V^2}{2}+gz\right)\dot{m} - \sum_\mathrm{entra}\left(\frac{P}{\rho}+\frac{V^2}{2}+gz\right)\dot{m},\quad(\mathrm{kW})
# \end{equation}
#     
# </div>

# > Notar que estas fórmulas consideran algunos casos particulares. Sin embargo, otros casos basados en combinaciones de los casos expuestos pueden ser facilmente derivadas a partir de esta discusión. 

# ### Ecuación de conservación de energía para una línea de flujo
# 
# En base a los casos anteriores, y considerando **(1) flujo incompresible y (2) volúmen de control con una única entrada y salida**, tenemos:
# 
# \begin{equation}
# \left(\frac{P}{\rho g}+\frac{V^2}{2g}+z\right)_\mathrm{entra} + h_\mathrm{bomba} = \left(\frac{P}{\rho g}+\frac{V^2}{2g}+z\right)_\mathrm{sale} + h_\mathrm{turbina} + h_L,\quad(\mathrm{m})
# \end{equation}
# 
# donde $h_\mathrm{i} = \frac{\dot{W}_\mathrm{i}}{\rho VA}$, ($i=$ $\mathrm{bomba}$, $\mathrm{turbina}$ y $L$) es la **altura de presión equivalente** asociada a la energía transferida por una bomba, turbina o viscosidad, respectivamente.

# El término $h_\mathrm{L}$ se conoce como la **pérdida de carga,** asociada al pérdida irreversible de energía mecánica por fricción y viscosidad.

# La ecuación (4.7) representa la forma más utilizada de la ecuación de conservación energía mecánica. Se expresa en forma de **alturas hidrostáticas,** ya que permite facilmente identificar los cambios de presión en el ducto.
# 
# <img src="./figures/mechanical_energy_conservation.png" width="750px" align= center>

# ### Ecuación de Bernoulli
# 
# Si aplicamos la ecuación anterior en un tramo de un ducto, donde $h_\mathrm{bomba} = h_\mathrm{turbina} = 0$, y asumimos **fluido ideal, es decir, sin fricciones por viscosidad ($h_L = 0$)**, tenemos la **ecuación de Bernoulli.**

# \begin{equation}
# \left(\frac{P}{\rho}+\frac{V^2}{2}+gz\right)_\mathrm{sale} = \left(\frac{P}{\rho}+\frac{V^2}{2}+gz\right)_\mathrm{entra}
# \end{equation}

# Esta ecuación, aunque tiene poco uso práctico, permite comprender en términos simples la conservación de energía en un fluido producto de los cambios de presión, velocidad y elevación.
# 
# <img src="./figures/bernoulli.png" width="850px" align= center>

# ## Flujo laminar y turbulento

# En la unidad introductoria mencionamos, brevemente, las caracteristicas que diferencian un flujo laminar de uno turbulento
# <img src="./figures/laminar_vs_turbulent_illustration.png" width="800px" align= center>

# La principal diferencia entre ambos está dada por las fluctuaciones en las propiedades del flujo.
# - **Flujo laminar**: flujo ordenado caracterizado por líneas suaves
# - **Flujo turbulento**: flujo desordenado, caracterizado por fluctuaciones en torno a valores promedio

# La mejor forma de visualizar esto es mediante el experimento diseñado por Osborne Reynolds. En este experimento, un tubo con colorante es introducido en el centro de un ducto transparente por donde fluye agua. 
# 
# <img src="./figures/reynolds_experiment.png" width="700px" align= center>
# 
# Las fluctuaciones inducidas por la turbulencia se manifiestan mediante la mezcla del colorante con el agua.

# En el siguiente podemos ver el famoso experimento.

# In[1]:


from IPython.display import YouTubeVideo
YouTubeVideo('nl75BGg9qdA', width=700, height=400)


# ### Número de Reynolds

# Físicamente, las características de un flujo que definen si es laminar o turbulento son:
# - Viscosidad dinámica
# - Densidad
# - Velocidad del flujo

# La relación entre estos tres parámetros está dado por el **número de Reynolds**
# 
# \begin{equation}
# \mathrm{Re} = \frac{VL_c}{\nu}
# \end{equation}
# 
# donde $\nu = \mu/\rho,~(\mathrm{m^2/s})$ es la viscosidad cinemática y **$L_c$ es una longitud caractéristica** relativa al problema estudiado.

# En el caso de flujo en ductos circulares de diámetro $D$, la longitud característica $L_c = D$. 

# La clasificación está dada por el siguiente criterio
# 
# \begin{eqnarray*}
# &~\mathrm{Re}_D &\lesssim 2300,\quad&&\mathrm{Flujo~laminar}\\
# 2300\lesssim &~\mathrm{Re}_D &\lesssim 4000,\quad&&\mathrm{Flujo~en~transición}\\
# 4000\lesssim &~\mathrm{Re}_D&\quad&&\mathrm{Flujo~turbulento}\\
# \end{eqnarray*}

# En el caso de ductos no circulares, utilizamos el **diámetro hidráulico**:
# 
# \begin{equation}
# D_h = \frac{4A}{P_h}
# \end{equation}
# 
# donde **$A$ es el área de la sección transversal del ducto** y **$P_h$ es el perímetro mojado** (perímetro del ducto en contacto con el fluido).

# <img src="./figures/diametro_hidraulico.png" width="700px" align= center>

# ## Pérdida de carga
# 
# Podemos diferenciar dos grandes grupos para la pérdida de carga en sistemas de tuberías:
# 
# \begin{equation}
# h_L = h_{L,\mathrm{mayor}} + h_{L,\mathrm{menor}}
# \end{equation}
# 
# Donde: 
# - $h_{L,\mathrm{mayor}}$: **pérdidas mayores**, asociadas a pérdidas por fricción en la longitud del ducto
# 
# - $h_{L,\mathrm{menor}}$: **pérdidas menores**, asociadas a pérdidas por fricción en singularidades, como: válvulas, codos, cambios de sección, etc.

# > El término "mayor" y "menor" no está directamente relacionado con la magnitud de cada pérdida. Es decir, es posible encontrar casos donde las pérdidas menores sean superiores a las mayores, y viceversa.

# ### Pérdida de carga en la longitud (mayores)
# 
# Es posible demostrar que, para ductos circulares de diámetro $D$, la pérdida de carga entre dos puntos separados por una longitud $L$ está dada por la **ecuación de Darcy-Weisbach:**
# 
# \begin{equation}
# h_L = f\frac{L}{D}\frac{V^2}{2g},\quad(\mathrm{m})
# \end{equation}
# 
# donde **$f$ es el factor de fricción de Darcy,** y $V$ es la velocidad promedio del flujo en el ducto

# La fórmula para el factor de fricción depende de si el flujo es laminar o turbulento.

# #### Factor de fricción para flujo laminar
# En el caso de flujo laminar, el factor de fricción está dado por:
# 
# \begin{equation}
# f = \frac{64}{\mathrm{Re}_D}
# \end{equation}

# Para ductos no circulares, usamos las siguientes relaciones en función del diámetro hidráulico ($D_h$)
# 
# <img src="./figures/head_loss_laminar_non-circular.png" width="850px" align= center>

# #### Factor de fricción para flujo turbulento
# Para flujo en transición y turbulento, el factor de fricción depende de la rugosidad del ducto, $\epsilon$. Esto porque *la inestabilidad del flujo será mayor cuando la rugosidad aumenta.*

# El factor de fricción, así, depende de $\mathrm{Re}_D$ y la rugosidad relativa $\epsilon_R =\epsilon/D$, y se define por 
# **ecuación de Colebrook:**
# 
# \begin{equation*}
# \frac{1}{\sqrt{f}} = - 2 \log\left(\frac{\epsilon_R}{3.7} + \frac{2.51}{\mathrm{Re}_D\sqrt{f}}\right)
# \end{equation*}

# Esta ecuación es no lineal y su solución, por lo tanto, requiere de métodos númericos.

# Una alternativa a la ecuación de Colebrook es el diagrama de Moody.
# 
# 
# <div class="full-width">
#     
# <img src="./figures/Moody_diagram.png" width="1000px" align= center>
# 
# </div>

# Otra alternativa es utilizar relaciones empíricas que expresan $f$ de forma explicita, pero aproximada. Por ejemplo:
# 
# \begin{eqnarray}
# f &=& 0.25\left[\log\left(\frac{\epsilon_R}{3.7}+\frac{5.74}{\mathrm{Re}_D^{0.9}}\right)\right]^{-2}\quad\quad&&\mathrm{Miller}
# \\[10pt]
# \frac{1}{\sqrt{f}} &=& -1.8\log\left[\left(\frac{\epsilon_R}{3.7}\right)^{1.11}+\frac{6.9}{\mathrm{Re}_D}\right]\quad\quad&&\mathrm{Haaland}
# \end{eqnarray}

# ### Pérdidas de carga por singularidades (menores)
# Estas pérdidas están dadas por singularidades, tales como: cambios de sección en el flujo, cambios de dirección en codos, válvulas, etc.

# La relación universal es:
# \begin{equation}
# h_{L,\mathrm{menores}} = \sum_i K_i\frac{V_i^2}{2g}
# \end{equation}
# 
# donde $K_i$ y $V_i$ son el coeficiente de pérdida y la velocidad en la singularidad $i$.

# > Notar que el valor de $V_i$ depende del tipo de singularidad.

# A continuación mostramos algunos ejemplos

# **Singularidad a la entrada y salida**
# 
# <img src="./figures/singularidad1.png" width="800px" align= center>

# **Expansión y contracción brusca**
# 
# <img src="./figures/singularidad2.png" width="800px" align= center>

# **Codos y "tes"**
# 
# <img src="./figures/singularidad3.png" width="800px" align= center>

# **Válvulas**
# 
# <img src="./figures/valves.png" width="600px" align= center>

# ### Tuberías en serie y paralelo
# 
# Los sistemas de cañerías a menudo consideran sistemas conectados en série y paralelo. En este caso, las relaciones para caudal y diferencia de presiones se ajustan como indica la figura:
# 
# <img src="./figures/series_and_parallel_pipe.png" width="700px" align= center>

# ## Referencias
# **Çengel Y. A. y Cimbala M. J. *Mecánica de Fluidos: Fundamentos y Aplicaciones*, 4ta Ed., McGraw Hill, 2018**
# - Capitulo 5: Ecuaciones de Bernoulli y de la energía
# - Capítulo 8: Flujo en tuberías
# 
# **White F. M. *Mecánica de Fluidos*, 5ta Ed., McGraw Hill, 2004**
# - Capítulo 3.6: Ecuación de la energía
# - Capítulo 3.7: Flujo sin fricción: La ecuación de Bernoulli
# - Capítulo 6: Flujo viscoso en conductos
