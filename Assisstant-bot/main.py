import streamlit as st
import os
from document_processor import DocumentProcessor
from github_tool import GitHubIssueCreator
from chat_handler import ChatHandler
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up Streamlit page
st.set_page_config(
    page_title="Automotive Support Assistant",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar for company info
with st.sidebar:
    st.image("https://via.placeholder.com/150", width=150)
    st.title("🚗 AutoMotive Support")
    st.markdown("Providing intelligent support for your vehicle inquiries.")
    st.markdown("📞 **Phone:** +1-800-555-AUTO")
    st.markdown("📧 **Email:** support@automotivesupport.com")
    st.markdown("🌐 [Visit Website](https://automotivesupport.com)")

# Initialize session state variables
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
if "document_processor" not in st.session_state:
    st.session_state.document_processor = DocumentProcessor(data_dir="data")
    if not os.path.exists("faiss_index"):
        with st.spinner("Loading documents and creating embeddings..."):
            st.session_state.document_processor.load_documents()
            st.session_state.document_processor.create_embeddings()
    
if "chat_handler" not in st.session_state:
    st.session_state.chat_handler = ChatHandler(st.session_state.document_processor)
    
if "github_tool" not in st.session_state:
    st.session_state.github_tool = GitHubIssueCreator()
    
if "show_ticket_form" not in st.session_state:
    st.session_state.show_ticket_form = False
    
if "user_info" not in st.session_state:
    st.session_state.user_info = {"name": "", "email": ""}

# Helper functions
def process_user_message(user_message):
    if not user_message.strip():
        return
    
    if len(st.session_state.chat_history) > 0 and st.session_state.chat_history[-1]["content"] == user_message:
        st.session_state.chat_history.append({"role": "assistant", "content": "You've already asked this. Would you like me to clarify or provide additional details?"})
        return
    
    st.session_state.chat_history.append({"role": "user", "content": user_message})
    
    if st.session_state.chat_handler.check_ticket_intent(user_message):
        st.session_state.show_ticket_form = True
        response = "I'd be happy to help you create a support ticket. Please fill out the form on the right."
    else:
        response = st.session_state.chat_handler.process_message(user_message)
    
    if len(st.session_state.chat_history) == 0 or st.session_state.chat_history[-1]["content"] != response:
        st.session_state.chat_history.append({"role": "assistant", "content": response})

def create_ticket():
    name = st.session_state.user_info["name"]
    email = st.session_state.user_info["email"]
    summary = st.session_state.ticket_summary
    description = st.session_state.ticket_description
    
    if not name or not email or not summary or not description:
        st.error("All fields are required")
        return
    
    result = st.session_state.github_tool.create_issue(name, email, summary, description)
    
    if result["success"]:
        success_message = f"✅ Support ticket created successfully! [Track here]({result['issue_url']})"
        st.session_state.chat_history.append({"role": "assistant", "content": success_message})
        
        st.session_state.show_ticket_form = False
        st.session_state.ticket_summary = ""
        st.session_state.ticket_description = ""
    else:
        error_message = f"❌ Failed to create support ticket: {result['message']}"
        st.session_state.chat_history.append({"role": "assistant", "content": error_message})

# UI Layout
st.title("🚗 Automotive Support Assistant")

col1, col2 = st.columns([3, 1])

with col1:
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.chat_history:
            role = message["role"]
            content = message["content"]
            if role == "user":
                st.markdown(f"<div style='background-color:#cce5ff;padding:10px;border-radius:10px;margin:5px;'><b>You:</b> {content}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='background-color:#d4edda;padding:10px;border-radius:10px;margin:5px;'><b>Assistant:</b> {content}</div>", unsafe_allow_html=True)
    
    if "clear_input" in st.session_state and st.session_state["clear_input"]:
        user_input = st.text_input("Type your message here:", key="user_message", value="")
        del st.session_state["clear_input"]  # Reset flag
    else:
      user_input = st.text_input("Type your message here:", key="user_message")
    if st.button("Send") and user_input.strip():
        process_user_message(user_input)
    
    
        st.session_state["clear_input"] = True
        st.rerun()
with col2:
    if st.session_state.show_ticket_form:
        st.subheader("📩 Create Support Ticket")
        st.text_input("Your Name", key="user_name", on_change=lambda: st.session_state.update({"user_info": {"name": st.session_state.user_name, "email": st.session_state.user_email}}))
        st.text_input("Your Email", key="user_email", on_change=lambda: st.session_state.update({"user_info": {"name": st.session_state.user_name, "email": st.session_state.user_email}}))
        st.text_input("Ticket Summary (Title)", key="ticket_summary")
        st.text_area("Ticket Description", height=150, key="ticket_description")
        if st.button("Submit Ticket"):
            create_ticket()
            st.rerun()
    else:
        st.info("Ask questions about Ford F-150 vehicles using the chat. If you need additional support, you can create a support ticket.")