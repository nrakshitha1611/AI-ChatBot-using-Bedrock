import streamlit as st
from langchain_aws import ChatBedrock
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
import boto3
import os

# Page config
st.set_page_config(
    page_title="ChatBot using AWS Bedrock",
    page_icon="🤖",
    layout="wide"
)

# AWS Configuration
os.environ["AWS_PROFILE"] = "your_profile_name"

@st.cache_resource
def initialize_bedrock():
    """Initialize Bedrock client and model (cached for performance)"""
    try:
        bedrock_client = boto3.client(
            service_name="bedrock-runtime",
            region_name="us-east-1"
        )
        
        llm = ChatBedrock(
            model_id="anthropic.claude-3-haiku-20240307-v1:0",
            client=bedrock_client,
            model_kwargs={
                "max_tokens": 900,
                "temperature": 0.9
            }
        )
        return llm
    except Exception as e:
        st.error(f"Failed to initialize Bedrock: {str(e)}")
        return None

def get_response(language, freeform_text):
    """Get response from Bedrock"""
    llm = initialize_bedrock()
    if not llm:
        return "Error: Could not initialize Bedrock client"
    
    try:
        prompt = PromptTemplate(
            input_variables=["language", "freeform_text"],
            template="You are a helpful chatbot. Respond in {language}.\n\nQuestion: {freeform_text}"
        )
        
        chain = prompt | llm | StrOutputParser()
        response = chain.invoke({
            "language": language,
            "freeform_text": freeform_text
        })
        
        return response
    except Exception as e:
        return f"Error generating response: {str(e)}"

def streaming_response(language, freeform_text):
    """Streaming response for Streamlit (yields chunks for real-time display)"""
    llm = initialize_bedrock()
    if not llm:
        yield "Error: Could not initialize Bedrock client"
        return
    
    try:
        prompt = PromptTemplate(
            input_variables=["language", "freeform_text"],
            template="You are a helpful chatbot. Respond in {language}.\n\nQuestion: {freeform_text}"
        )
        
        chain = prompt | llm | StrOutputParser()
        
        for chunk in chain.stream({
            "language": language,
            "freeform_text": freeform_text
        }):
            yield chunk
    except Exception as e:
        yield f"Error: {str(e)}"

# Main Streamlit App
def main():
    st.title("🤖 ChatBot using AWS Bedrock")
    
    # Sidebar for inputs
    st.sidebar.header("Chat Configuration")
    
    language = st.sidebar.selectbox(
        "Language",
        ["English", "Spanish", "French", "German", "Italian"],
        index=0
    )
    
    freeform_text = st.sidebar.text_area(
        label="What is your question?",
        max_chars=500,
        height=100,
        placeholder="Type your question here..."
    )
    
    # Submit button for better UX
    submit_button = st.sidebar.button("Ask Question", type="primary")
    
    # Response area
    if submit_button and freeform_text.strip():
        st.subheader("Response:")
        
        # Simple response (all at once)
        if st.sidebar.checkbox("Use streaming", value=True):
            # Streaming response
            response_container = st.empty()
            full_response = ""
            
            for chunk in streaming_response(language, freeform_text):
                full_response += chunk
                response_container.markdown(full_response + "▌")  # Cursor effect
            
            response_container.markdown(full_response)  # Final response without cursor
            
        else:
            # Non-streaming response
            with st.spinner("Generating response..."):
                response = get_response(language, freeform_text)
                st.markdown(response)
    
    elif submit_button and not freeform_text.strip():
        st.warning("Please enter a question before submitting.")
    
    # Instructions
    with st.expander("ℹ️ How to use this chatbot"):
        st.markdown("""
        1. **Select Language**: Choose your preferred language from the dropdown
        2. **Enter Question**: Type your question in the text area
        3. **Ask Question**: Click the button to get a response
        4. **Streaming**: Toggle streaming for real-time response display
        
        **Note**: Make sure your AWS credentials are properly configured and you have access to Amazon Bedrock.
        """)
    
    # Status information
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Status**")
    
    # Check if Bedrock is accessible
    llm = initialize_bedrock()
    if llm:
        st.sidebar.success("✅ Bedrock Connected")
    else:
        st.sidebar.error("❌ Bedrock Connection Failed")

if __name__ == "__main__":
    main()
