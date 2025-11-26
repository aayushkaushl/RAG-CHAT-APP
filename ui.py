import streamlit as st


def chat_header():
    st.markdown("""
        <h1 style='text-align:center; color:#4CAF50;'> Blog RAG Chat App</h1>
        <p style='text-align:center; font-size:18px;'>Ask anything from your uploaded blog</p>
    """, unsafe_allow_html=True)


def chat_box(message, role="user"):
    
    align = "right" if role == "user" else "left"

    st.markdown(
        f"""
        <div style=' padding:10px 15px; 
                    border-radius:10px; margin:5px; width:80%; float:{align};'>
            {message}
        </div>
        <div style='clear:both'></div>
        """,
        unsafe_allow_html=True
    )
