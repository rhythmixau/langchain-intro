import os
# from langchain_core.prompts import PromptTemplate
# from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

"""
Groq Model Switching Exercise - LangChain Integration

Instructions:
1. This exercise simulates langchain-groq integration patterns
2. You'll implement functions to switch between Groq models
3. Complete the functions below to demonstrate proper model switching
4. Use valid model names from the Groq website (console.groq.com)

Learning Objectives:
- Learn LangChain-Groq integration patterns
- Practice switching between different LLM models with full model names
- Understand proper class instantiation and method calls
- Master function composition and data structures

Note: This uses mock objects to simulate the langchain-groq package behavior!
Model names should match exactly what's available on console.groq.com
"""


def implement_set_api_key(api_key):
    """
    IMPLEMENT: Set the GROQ_API_KEY environment variable.
    
    Args:
        api_key (str): Your Groq API key
    """
    # TODO: Your implementation here
    os.environ["GROQ_API_KEY"] = api_key


def check_api_key():
    """
    Check if GROQ_API_KEY is set in environment variables.
    Raise an exception if the API key is not set.
    (This function is provided for you)
    """
    if "GROQ_API_KEY" not in os.environ:
        raise Exception("GROQ_API_KEY environment variable is required")
    else:
        print(f"GROQ_API_KEY: {os.environ["GROQ_API_KEY"]}")


def implement_llama_4_model():
    """
    IMPLEMENT: Create and return a ChatGroq instance for Llama 4.
    Use the exact model name from console.groq.com
    Set temperature=0 for consistent responses
    """
    print("Creating an instance of ChatGroq for Llama 4")
    return ChatGroq(model="meta-llama/llama-4-maverick-17b-128e-instruct", temperature=0, max_retries=2)
    


def implement_llama_3_3_model():
    """
    IMPLEMENT: Create and return a ChatGroq instance for Llama 3.3.
    Use the exact model name from console.groq.com
    Set for slightly more creative responses
    """
    return ChatGroq(model="llama-3.3-70b-versatile", temperature=0.2, max_retries=2)

def implement_gpt_oss():
    return ChatGroq(model="openai/gpt-oss-120b", temperature=0)


def implement_query_model(model: ChatGroq, prompt: str):
    """
    IMPLEMENT: Send a query to the model and return the response content.
    
    Args:
        model: The ChatGroq model instance
        prompt: The text prompt to send
        
    Returns:
        str: The response content
    """
    job_description = """
    you are a primary STEM teacher that can answer questions about science, technology, engineering, and math.
    """
    # messages = [
    #     {"role": "system", "content": job_description},
    #     {"role": "human", "content": prompt }
    #     ]
    
    messages = [("system", job_description), ("human", prompt)]

    result = model.invoke(messages)

    return result.content


def implement_compare_models(prompt):
    """
    IMPLEMENT: Query both models and return a dictionary with both responses.
    
    Args:
        prompt: The text prompt to send to both models
        
    Returns:
        dict: Dictionary with responses from both models
    """
    model4 = implement_llama_4_model()
    model3 = implement_llama_3_3_model()

    result4 = implement_query_model(model4, prompt)
    result3 = implement_query_model(model3, prompt)

    print("model4: ", result4)
    print("model3: ", result3)

    return {
        "model4": result4,
        "model3": result3
    }

def main():
    """
    Main function to test your implementations.
    """
    print("🚀 Groq Model Switching Exercise (LangChain Integration)")
    print("=" * 55)
    print("📝 This exercise simulates langchain-groq package behavior!")
    print("🌐 Model names should match console.groq.com exactly")
    print()
    
    try:
        # Test your set_api_key implementation
        print("🔑 Setting API key...")
        # implement_set_api_key("mock_api_key_for_testing")
        
        # Check if API key was set correctly
        check_api_key()
        print("✓ API key validation working!")
        
        # Test prompt
        test_prompt = "Explain the concept of machine learning in one sentence."
        
        # Test your model implementations
        print(f"\n🤖 Testing your Llama 4 implementation:")
        llama4 = implement_llama_4_model()
        response4 = implement_query_model(llama4, test_prompt)
        print(f"Llama 4: {response4}\n")
        
        print(f"🤖 Testing your Llama 3.3 implementation:")
        llama33 = implement_llama_3_3_model()
        response33 = implement_query_model(llama33, test_prompt)
        print(f"Llama 3.3: {response33}\n")
        
        # # Test your comparison implementation
        print("🔄 Testing your model comparison:")
        comparison = implement_compare_models(test_prompt)
        print("Comparison results:")
        for model, response in comparison.items():
            print(f"  {model}: {response}")
        
        # print("\n🎉 All implementations working!")
        # print("✅ Great job implementing the LangChain-Groq patterns!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        if "GROQ_API_KEY" in str(e):
            print("\n💡 Check your implement_set_api_key() function!")
        else:
            print("📝 Check your function implementations!")
            print("🌐 Verify model names match console.groq.com exactly")

if __name__ == "__main__":
    main()
