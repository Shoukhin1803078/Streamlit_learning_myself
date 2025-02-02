
# import streamlit as st
# import ollama
# import re

# # st.set_page_config(page_title="Ollama Chat", layout="wide")

# # Custom CSS to reduce width and fix input at bottom
# st.markdown("""
# <style>
#     /* Container width control */
#     .main .block-container {
#         max-width: 800px;
#         padding-top: 2rem;
#         padding-bottom: 2rem;  /* Space for fixed input */
#         margin: 0 auto;
#     }
    
#     /* Message styling */
#     .stChatMessage {
#         background-color: #f0f2f6;
#         border-radius: 10px;
#         padding: 1rem;
#         margin: 0.5rem 0;
#     }

#     /* Fixed bottom input styling */
#     [data-testid="stChatInput"] {
#         position: fixed !important;
#         bottom: 0 !important;
#         left: 45% !important;
#         transform: translateX(-50%) !important;
#         max-width: 400px !important;
#         width: 100% !important;
#         padding: 1rem !important;
#         z-index: 1000 !important;
#     }
# </style>
# """, unsafe_allow_html=True)





# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Create columns for narrower layout
# col1, col2, col3 = st.columns([1, 3, 1])

# with col2:
#     st.title("💬 Live Thinking Chat using Deepseek 1.5B by Al Amin ")

#     def is_thinking_complete(text):
#         """Check if thinking process is complete"""
#         return '</think>' in text

#     def has_think_tags(text):
#         """Check if text contains think tags"""
#         return '<think>' in text

#     def extract_current_thinking(text):
#         """Extract current thinking content"""
#         if '<think>' in text:
#             thinking = text.split('<think>')[1]
#             if '</think>' in thinking:
#                 thinking = thinking.split('</think>')[0]
#             return thinking.strip()
#         return ""

#     def get_response_after_thinking(text):
#         """Get text after </think> tag if it exists, or the full text if no tags"""
#         if '</think>' in text:
#             return text.split('</think>')[1].strip()
#         return text.strip()

#     # Display chat history
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             if message["role"] == "assistant":
#                 thinking = extract_current_thinking(message["content"])
#                 response = get_response_after_thinking(message["content"])
#                 if thinking:
#                     with st.expander("✨ Thinking completed", expanded=False):
#                         st.markdown(thinking)
#                 st.markdown(response)
#             else:
#                 st.markdown(message["content"])

#     # User input and response generation (fixed at bottom)
#     if prompt := st.chat_input("What would you like to know?"):
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user"):
#             st.markdown(prompt)

#         with st.chat_message("assistant"):
#             full_response = ""
#             thinking_complete = False
#             has_thinking = False
#             thinking_placeholder = st.empty()
#             response_placeholder = st.empty()
            
#             # Stream the response
#             for chunk in ollama.chat(
#                 model="deepseek-r1:1.5b",
#                 messages=[{"role": "user", "content": prompt}],
#                 stream=True
#             ):
#                 if chunk['message']['content']:
#                     full_response += chunk['message']['content']
                    
#                     # Check if response has think tags
#                     if not has_thinking and has_think_tags(full_response):
#                         has_thinking = True
                    
#                     if has_thinking:
#                         current_thinking = extract_current_thinking(full_response)
                        
#                         # Show live thinking
#                         if current_thinking and not thinking_complete:
#                             with thinking_placeholder.expander("🤔 Thinking in progress...", expanded=True):
#                                 st.markdown(current_thinking + "▌")
                        
#                         # When thinking is complete
#                         if is_thinking_complete(full_response) and not thinking_complete:
#                             with thinking_placeholder.expander("✨ Thinking completed", expanded=False):
#                                 st.markdown(current_thinking)
#                             thinking_complete = True
                            
#                         # Show response after thinking
#                         if thinking_complete:
#                             response = get_response_after_thinking(full_response)
#                             response_placeholder.markdown(response + "▌")
#                     else:
#                         # Direct response without thinking
#                         response_placeholder.markdown(full_response + "▌")
            
#             # Final update without cursor
#             final_response = get_response_after_thinking(full_response)
#             response_placeholder.markdown(final_response)
#             st.session_state.messages.append({"role": "assistant", "content": full_response})
















# import streamlit as st
# import ollama

# st.title("💬 Live Thinking Chat using Deepseek 1.5B")

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Helper functions
# def is_thinking_complete(text):
#     return '</think>' in text

# def has_think_tags(text):
#     return '<think>' in text

# def extract_current_thinking(text):
#     if '<think>' in text:
#         thinking = text.split('<think>')[1]
#         if '</think>' in thinking:
#             thinking = thinking.split('</think>')[0]
#         return thinking.strip()
#     return ""

# def get_response_after_thinking(text):
#     if '</think>' in text:
#         return text.split('</think>')[1].strip()
#     return text.strip()

# # Display chat history
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         if message["role"] == "assistant":
#             thinking = extract_current_thinking(message["content"])
#             response = get_response_after_thinking(message["content"])
#             if thinking:
#                 with st.expander("✨ Thinking process", expanded=False):
#                     st.markdown(thinking)
#             st.markdown(response)
#         else:
#             st.markdown(message["content"])

# # Chat input
# if prompt := st.chat_input("What would you like to know?"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     with st.chat_message("assistant"):
#         full_response = ""
#         thinking_complete = False
#         has_thinking = False
#         thinking_placeholder = st.empty()
#         response_placeholder = st.empty()
        
#         # Stream the response
#         for chunk in ollama.chat(
#             model="deepseek-r1:1.5b",
#             messages=[{"role": "user", "content": prompt}],
#             stream=True
#         ):
#             if chunk['message']['content']:
#                 full_response += chunk['message']['content']
                
#                 if not has_thinking and has_think_tags(full_response):
#                     has_thinking = True
                
#                 if has_thinking:
#                     current_thinking = extract_current_thinking(full_response)
                    
#                     if current_thinking and not thinking_complete:
#                         with thinking_placeholder.expander("🤔 Thinking...", expanded=True):
#                             st.markdown(current_thinking + "▌")
                    
#                     if is_thinking_complete(full_response) and not thinking_complete:
#                         with thinking_placeholder.expander("✨ Thinking process", expanded=False):
#                             st.markdown(current_thinking)
#                         thinking_complete = True
                        
#                     if thinking_complete:
#                         response = get_response_after_thinking(full_response)
#                         response_placeholder.markdown(response + "▌")
#                 else:
#                     response_placeholder.markdown(full_response + "▌")
        
#         final_response = get_response_after_thinking(full_response)
#         response_placeholder.markdown(final_response)
#         st.session_state.messages.append({"role": "assistant", "content": full_response})








# -----------------------------------------------simple----------------------------------------?



# import streamlit as st
# import ollama

# st.title("💬 Live Thinking Chat using Deepseek 1.5B")

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat history
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # Chat input and response
# if prompt := st.chat_input("What would you like to know?"):
#     # Add user message to chat
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Generate assistant response
#     with st.chat_message("assistant"):
#         message_placeholder = st.empty()
#         full_response = ""
        
#         # Stream the response
#         for chunk in ollama.chat(
#             model="deepseek-r1:1.5b",
#             messages=[{"role": "user", "content": prompt}],
#             stream=True
#         ):
#             if chunk['message']['content']:
#                 full_response += chunk['message']['content']
#                 message_placeholder.markdown(full_response + "▌")
        
#         message_placeholder.markdown(full_response)
#         st.session_state.messages.append({"role": "assistant", "content": full_response})







import streamlit as st
import ollama
import base64

# st.title("💬 Live Thinking Chat using Deepseek 1.5B")

# Add image after title
try:
    image_path = "assets/deepseek.png"
    encoded_image = base64.b64encode(open(image_path, "rb").read()).decode()
    st.markdown(
        f"""
        # 💬 Live Thinking Deepseek <img src="data:image/png;base64,{encoded_image}" width="120" style="vertical-align: -50px;">
        """,
        unsafe_allow_html=True
    )
except FileNotFoundError:
    st.error("Image file not found. Please make sure 'assets/deepseek.png' exists.")

# Helper functions
def is_thinking_complete(text):
    """Check if thinking process is complete"""
    return '</think>' in text

# Rest of your code remains the same...

def has_think_tags(text):
    """Check if text contains think tags"""
    return '<think>' in text

def extract_current_thinking(text):
    """Extract current thinking content"""
    if '<think>' in text:
        thinking = text.split('<think>')[1]
        if '</think>' in thinking:
            thinking = thinking.split('</think>')[0]
        return thinking.strip()
    return ""

def get_response_after_thinking(text):
    """Get text after </think> tag if it exists, or the full text if no tags"""
    if '</think>' in text:
        return text.split('</think>')[1].strip()
    return text.strip()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant":
            thinking = extract_current_thinking(message["content"])
            response = get_response_after_thinking(message["content"])
            if thinking:
                with st.expander("✨ Thinking completed", expanded=False):
                    st.markdown(thinking)
            st.markdown(response)
        else:
            st.markdown(message["content"])

# Chat input and response
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        full_response = ""
        thinking_complete = False
        has_thinking = False
        thinking_placeholder = st.empty()
        response_placeholder = st.empty()
        
        # Stream the response
        for chunk in ollama.chat(
            model="deepseek-r1:1.5b",
            messages=[{"role": "user", "content": prompt}],
            stream=True
        ):
            if chunk['message']['content']:
                full_response += chunk['message']['content']
                
                # Check if response has think tags
                if not has_thinking and has_think_tags(full_response):
                    has_thinking = True
                
                if has_thinking:
                    current_thinking = extract_current_thinking(full_response)
                    
                    # Show live thinking
                    if current_thinking and not thinking_complete:
                        with thinking_placeholder.expander("🤔 Thinking in progress...", expanded=True):
                            st.markdown(current_thinking + "▌")
                    
                    # When thinking is complete
                    if is_thinking_complete(full_response) and not thinking_complete:
                        with thinking_placeholder.expander("✨ Thinking completed", expanded=False):
                            st.markdown(current_thinking)
                        thinking_complete = True
                    
                    # Show response after thinking
                    if thinking_complete:
                        response = get_response_after_thinking(full_response)
                        response_placeholder.markdown(response + "▌")
                else:
                    # Direct response without thinking
                    response_placeholder.markdown(full_response + "▌")
        
        # Final update without cursor
        final_response = get_response_after_thinking(full_response)
        response_placeholder.markdown(final_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})