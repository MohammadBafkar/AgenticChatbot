import streamlit as st
import os
from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}
    
    def load_streamlit_ui(self):
        page_title = "🤖 " + self.config.get_page_title()
        st.set_page_config(page_title= page_title, layout="wide")
        st.header(page_title)
        
        with st.sidebar:
            self.user_controls['selected_llm'] = st.selectbox("Select LLM", self.config.get_llm_options())
            if self.user_controls['selected_llm'] == 'Groq':
                self.user_controls['selected_groq_model'] = st.selectbox("Select Model", self.config.get_groq_model_options())
                self.user_controls['GROQ_API_KEY'] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key", type="password")
                
                if not self.user_controls['GROQ_API_KEY']:
                    st.warning("Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys")
            self.user_controls['selected_usecase'] = st.selectbox("Select Use Case", self.config.get_usecase_options())
            if self.user_controls['selected_usecase'] == 'Chatbot with Web':
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("Tavily API Key", type="password")

                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("Please enter your Tavily API key to proceed. Don't have? refer : https://app.tavily.com/home")

        return self.user_controls