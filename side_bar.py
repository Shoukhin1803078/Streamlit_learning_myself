import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# st.markdown(
# """
# <style>
# .stAppToolbar.st-emotion-cache-15ecox0.e10jh26i2 {
# visibility: hidden;
# }
# </style>

# """,unsafe_allow_html=True
# )




st.sidebar.title('Side Bar')
st.sidebar.write ("This is a side bar")


x=np.linspace(0,10,100)
y=np.sin(x)
fig= plt.figure()
plt.plot(x,y)
st.write(fig)