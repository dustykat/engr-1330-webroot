#!/usr/bin/env python
# coding: utf-8

# # Assessing the Accuracy of a Solution
# 
# Suppose the solution below is presented for the example above.
# 
# $$\begin{matrix}
# i = 1.68 \text{ amperes}& i_1 = 0.48 \text{ amperes}& i_2 = 1.20 \text{ amperes} \\
# V_1 = 12.0 \text{ volts} & V_2 = 9.6 \text{ volts}  & V_3 = 2.4 \text{ volts}  \\
# \end{matrix}$$
# 
# 1. Is the solution clear and complete?
# 2. Does the solution seem correct?
# 
# The solution is clear and complete values are supplied for relevant knowns and unknowns.
# 
# Of the two branch currents, $i_1$ and $i_2$, the larger current in the solution is flowing through the rightmost path which has greater resistance - this result does not make sense.  Furthermore the larger voltage drop is reported on the smaller resistor in the path, this result too does not make much sense (Ohm's law is being violated).  Upon examination we could conclude that the values are correct, but the results transposed during transcription.
# 
# The corrected solution is
# 
# $$\begin{matrix}
# i = 1.68 \text{ amperes}& i_1 = 1.20 \text{ amperes}& i_2 = 0.48 \text{ amperes} \\
# V_1 = 12.0 \text{ volts} & V_2 = 2.4 \text{ volts}  & V_3 = 9.6 \text{ volts}  \\
# \end{matrix}$$
# 
# This contemplative step is very important; ignore at your own risk.
# 
# 

# In[ ]:




