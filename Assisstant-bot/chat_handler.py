from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import os
from dotenv import load_dotenv

class ChatHandler:
    def __init__(self, document_processor):
        load_dotenv()
        self.document_processor = document_processor
        api_key = os.getenv("OPENAI_API_KEY", "")
        self.llm = init_chat_model("gpt-4o-mini", model_provider="openai")  # Use an appropriate model
        self.company_info = {
            "name": "AutoMotive Support",
            "phone": "+1-800-555-AUTO",
            "email": "support@automotivesupport.com",
            "website": "https://automotivesupport.com"
        }
        self.conversation_history = []
        
    def get_context_from_documents(self, query):
        """Retrieve relevant document chunks for the query"""
        results = self.document_processor.search_documents(query)
        
        if not results:
            return ""
        
        # Format context with source information for citations
        context = ""
        for doc, score in results:
            if score < 0.7:  # Optional: Filter by relevance score
                continue
                
            source = doc.metadata.get('source', 'Unknown')
            page = doc.metadata.get('page_number', 'N/A')
            context += f"\nCONTENT: {doc.page_content}\nSOURCE: {source}, Page: {page}\n\n"
            
        return context
    
    def format_system_prompt(self):
        """Create system prompt with company information"""
        return f"""You are a helpful customer support assistant for {self.company_info['name']}.
You answer questions based on the provided document context.
If you don't know the answer or can't find it in the context, suggest creating a support ticket.
Always cite your sources when answering questions, mentioning the document name and page number.
Company contact information:
- Phone: {self.company_info['phone']}
- Email: {self.company_info['email']}
- Website: {self.company_info['website']}

If the user wants to create a support ticket, ask for their name and email if not already provided.
"""
    
    def process_message(self, user_message):
        """Process user message and generate a response"""
        # Add user message to history
        self.conversation_history.append(HumanMessage(content=user_message))
        
        # Get context from documents
        context = self.get_context_from_documents(user_message)
        
        # Create messages for the LLM
        messages = [
            SystemMessage(content=self.format_system_prompt()),
            SystemMessage(content=f"Use the following context to answer the user's question: {context}")
        ]
        
        # Add conversation history (limited to last few exchanges to manage context window)
        messages.extend(self.conversation_history[-10:])  # Last 5 exchanges (10 messages)
        
        # Get response from LLM
        response = self.llm.invoke(messages)
        
        # Add response to history
        self.conversation_history.append(AIMessage(content=response.content))
        
        return response.content
        
    def check_ticket_intent(self, message):
        """Check if user intends to create a ticket"""
        ticket_phrases = [
            "create a ticket",
            "open a ticket",
            "submit a ticket",
            "raise a ticket",
            "support ticket",
            "help ticket",
            "new ticket"
        ]
        
        message_lower = message.lower()
        return any(phrase in message_lower for phrase in ticket_phrases)