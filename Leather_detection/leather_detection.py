# # Leather/leather.py
# import streamlit as st
# import pandas as pd
# from datetime import datetime
# import os

# # Page setup
# st.title("Leather Product Analysis")

# # Create two columns
# col1, col2 = st.columns(2)

# with col1:
#    st.subheader("Upload Images")
#    uploaded_files = st.file_uploader("Choose images", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])
   
#    if uploaded_files:
#        for file in uploaded_files:
#            st.image(file)

# with col2:
#    st.subheader("Product Details Form")
   
#    with st.form("leather_form"):
#        # Small table filling section
#        st.markdown("### Small table filling")
#        small_category_name = st.text_input("Small category name")
#        small_category_content = st.text_area("Small category content")
       
#        # With image filling section
#        st.markdown("### With image filling")
#        fields = {
#            "Product Type": st.text_input("Product Type"),
#            "Brand": st.text_input("Brand"),
#            "Shape": st.text_input("Shape"),
#            "Size": st.text_input("Size"),
#            "Materials": st.text_input("Materials"),
#            "Color": st.text_input("Color"),
#            "Damage location": st.text_input("Damage location"),
#            "Stain": st.text_input("Stain"),
#            "Product condition": st.text_input("Product condition"),
#            "Stain condition": st.text_input("Stain condition"),
#            "Mold": st.text_input("Mold"),
#            "Zipper condition": st.text_input("Zipper condition"),
#            "Stitch": st.text_input("Stitch"),
#            "Fastener condition": st.text_input("Fastener condition"),
#            "Vanish status": st.text_input("Vanish status")
#        }
       
#        submit = st.form_submit_button("Submit")
       
#        if submit:
#            # Prepare data for Excel
#            data = {
#                "Small_category_name": [small_category_name],
#                "Small_category_content": [small_category_content],
#                **{k: [v] for k, v in fields.items()}
#            }
           
#            df = pd.DataFrame(data)
           
#            # Create Excel file with timestamp
#            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#            filename = f"leather_data_{timestamp}.xlsx"
#            df.to_excel(filename, index=False)
           
#            st.success(f"Data saved to {filename}")






# Leather/leather.py
import streamlit as st
import pandas as pd
import os

st.title("Leather Product Analysis")

col1, col2 = st.columns([0.4, 0.6])

with col1:
   st.subheader("Upload Images")
   uploaded_files = st.file_uploader("Choose images", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])
   
   if uploaded_files:
       cols = st.columns(2)
       for idx, file in enumerate(uploaded_files):
           with cols[idx % 2]:
               st.image(file, use_column_width=True)

with col2:
   with st.form("leather_form", clear_on_submit=False):  # Changed to False to verify data
       st.markdown("### Small table filling")
       small_category_name = st.text_input("Small category name")
       small_category_content = st.text_area("Small category content", height=100)
       
       st.markdown("### With image filling")
       col3, col4 = st.columns(2)
       
       fields = {}
       with col3:
           fields.update({
               "Product_Type": st.text_input("Product Type"),
               "Brand": st.text_input("Brand"),
               "Shape": st.text_input("Shape"),
               "Size": st.text_input("Size"),
               "Materials": st.text_input("Materials"),
               "Color": st.text_input("Color"),
               "Damage_location": st.text_input("Damage location"),
               "Stain": st.text_input("Stain"),
           })
           
       with col4:
           fields.update({
               "Product_condition": st.text_input("Product condition"),
               "Stain_condition": st.text_input("Stain condition"),
               "Mold": st.text_input("Mold"),
               "Zipper_condition": st.text_input("Zipper condition"),
               "Stitch": st.text_input("Stitch"),
               "Fastener_condition": st.text_input("Fastener condition"),
               "Vanish_status": st.text_input("Vanish status")
           })
       
       submit = st.form_submit_button("Submit")
       
       if submit:
           filepath = 'leather/jbc.xlsx'
           os.makedirs('leather', exist_ok=True)
           
           data = {
               "Small_category_name": small_category_name,
               "Small_category_content": small_category_content,
               **fields
           }
           
           df_new = pd.DataFrame([data])
           
           if os.path.exists(filepath):
               df_existing = pd.read_excel(filepath)
               df_final = pd.concat([df_existing, df_new], ignore_index=True)
           else:
               df_final = df_new
           
           df_final.to_excel(filepath, index=False)
           st.success(f"Data saved successfully! Row count: {len(df_final)}")



