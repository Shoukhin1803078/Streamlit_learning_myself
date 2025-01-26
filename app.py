# app.py (main file)
import streamlit as st
st.set_page_config(layout="wide")  # Move this to main app.py

from streamlit_option_menu import option_menu
import importlib.util
from pathlib import Path

EXAMPLE_NO = 1
def streamlit_menu(example=1):
   if example == 1:
       with st.sidebar:
           return option_menu(
               menu_title="Main Menu",
               options=["Home", "Projects", "Contact","Chatbot","Leather_detection"],
               icons=["house", "book", "envelope"],
               menu_icon="cast",
               default_index=0
           )
   
   if example == 2:
       return option_menu(
           menu_title=None,
           options=["Home", "Projects", "Contact"],
           icons=["house", "book", "envelope"],
           menu_icon="cast",
           default_index=0,
           orientation="horizontal"
       )
   
   if example == 3:
       return option_menu(
           menu_title=None,
           options=["Home", "Projects", "Contact"],
           icons=["house", "book", "envelope"],
           menu_icon="cast",
           default_index=0,
           orientation="horizontal",
           styles={
               "container": {"padding": "0", "background-color": "#fafafa"},
               "icon": {"color": "orange", "font-size": "25px"},
               "nav-link": {
                   "font-size": "25px",
                   "text-align": "left",
                   "margin": "0px",
                   "--hover-color": "#eee",
               },
               "nav-link-selected": {"background-color": "green"},
           }
       )

# EXAMPLE_NO = st.selectbox('Select Menu Style:', [1, 2, 3])
selected = streamlit_menu(example=EXAMPLE_NO)

if selected:
   page = Path(__file__).parent / f"{selected}/{selected.lower()}.py"
   spec = importlib.util.spec_from_file_location(selected, page)
   module = importlib.util.module_from_spec(spec)
   spec.loader.exec_module(module)








# # import streamlit as st
# # from streamlit_option_menu import option_menu

# # import streamlit as st 
# # from streamlit_option_menu import option_menu 
# # import sys from pathlib import Path # Add parent directory to path for imports 

# # sys.path.append(str(Path(__file__).parent)) 
# # from Home.home import show_home 
# # from Projects.projects import show_projects 
# # from Contact.contact import show_contact


# # # 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
# # EXAMPLE_NO = 1


# # def streamlit_menu(example=1):
# #     if example == 1:
# #         # 1. as sidebar menu
# #         with st.sidebar:
# #             selected = option_menu(
# #                 menu_title="Main Menu",  # required
# #                 options=["Home", "Projects", "Contact"],  # required
# #                 icons=["house", "book", "envelope"],  # optional
# #                 menu_icon="cast",  # optional
# #                 default_index=0,  # optional
# #             )
# #         return selected

# #     if example == 2:
# #         # 2. horizontal menu w/o custom style
# #         selected = option_menu(
# #             menu_title=None,  # required
# #             options=["Home", "Projects", "Contact"],  # required
# #             icons=["house", "book", "envelope"],  # optional
# #             menu_icon="cast",  # optional
# #             default_index=0,  # optional
# #             orientation="horizontal",
# #         )
# #         return selected

# #     if example == 3:
# #         # 2. horizontal menu with custom style
# #         selected = option_menu(
# #             menu_title=None,  # required
# #             options=["Home", "Projects", "Contact"],  # required
# #             icons=["house", "book", "envelope"],  # optional
# #             menu_icon="cast",  # optional
# #             default_index=0,  # optional
# #             orientation="horizontal",
# #             styles={
# #                 "container": {"padding": "0!important", "background-color": "#fafafa"},
# #                 "icon": {"color": "orange", "font-size": "25px"},
# #                 "nav-link": {
# #                     "font-size": "25px",
# #                     "text-align": "left",
# #                     "margin": "0px",
# #                     "--hover-color": "#eee",
# #                 },
# #                 "nav-link-selected": {"background-color": "green"},
# #             },
# #         )
# #         return selected


# # selected = streamlit_menu(example=EXAMPLE_NO)

# # if selected == "Home":
# #     st.title(f"You have selected {selected}")
# # if selected == "Projects":
# #     st.title(f"You have selected {selected}")
# # if selected == "Contact":
# #     st.title(f"You have selected {selected}")






# # myproject/app.py
# import streamlit as st
# from streamlit_option_menu import option_menu
# import importlib.util
# import sys
# from pathlib import Path

# st.markdown("""
# <style>
# .stAppHeader {
#    display: none;
# }
# footer {
#    display: none;
# }
# </style>
# """, unsafe_allow_html=True)

# selected = option_menu(
#    menu_title=None,
#    options=["Home", "Projects", "Contact"], 
#    icons=["house", "book", "envelope"],
#    menu_icon="cast",
#    default_index=0,
#    orientation="horizontal",
#    styles={
#        "container": {"padding": "0", "background-color": "#fafafa"},
#        "icon": {"color": "orange", "font-size": "25px"},
#        "nav-link": {
#            "font-size": "25px",
#            "text-align": "left",
#            "margin": "0px",
#            "--hover-color": "#eee",
#        },
#        "nav-link-selected": {"background-color": "green"},
#    },
# )

# if selected:
#    page = Path(__file__).parent / f"{selected}/{selected.lower()}.py"
#    spec = importlib.util.spec_from_file_location(selected, page)
#    module = importlib.util.module_from_spec(spec)
#    spec.loader.exec_module(module)





