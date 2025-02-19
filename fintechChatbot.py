import google.generativeai as genai
import streamlit as st


genai.configure(api_key='AIzaSyBoeGZNtUdSH_fCGPoZ7hARvNa_v2N9LBU')

knowledge_base = {
    "loans": "A loan is a sum of money that is borrowed and is expected to be paid back with interest. Loans can be secured or unsecured.",
    "interest rates": "An interest rate is the percentage of the loan amount that the borrower pays as interest to the lender over a specified period.",
    "credit reports": "A credit report is a detailed report of an individual's credit history, prepared by a credit bureau. It includes information like credit accounts, loans, and payment history.",
    "credit bureau": "A credit bureau is an agency that collects and researches individual credit information and sells it to creditors for a fee.",
    "cibil": "CIBIL stands for Credit Information Bureau (India) Limited. It is one of the leading credit bureaus in India, providing credit information on individuals and businesses.",
    "loan": "A loan is a sum of money that is borrowed and is expected to be paid back with interest. Loans can be secured or unsecured.",
    "interest rate": "An interest rate is the percentage of the loan amount that the borrower pays as interest to the lender over a specified period.",
    "credit report":"A credit report is a detailed report of an individual's credit history, prepared by a credit bureau. It includes information like credit accounts, loans, and payment history.",
    "hi": "This is FinTech Assistant How can i help you",
    "fintech":"Financial technology (better known as fintech) is used to describe new technology that seeks to improve and automate the delivery and use of financial services",
    "who are you" : "This is FinTech Assistant Here to assist you",
    "about you" : "This is FinTech Assistant Here to assist you",
    #"you" : "This is FinTech Assistant Here to assist you",
}

def get_chatbot_response(user_input):

    for key in knowledge_base:
        if key in user_input.lower():
            return knowledge_base[key]


    try:

        model = genai.GenerativeModel('gemini-pro')

        response = model.generate_content(user_input)
        return response.text.strip()
    except Exception as e:
        return f"Sorry, something went wrong: {e}"


def main():
    st.title("FinTech Chatbot")
    st.write("Welcome to the FinTech Chatbot! How can I assist you today?")

    user_input = st.text_input("You:")

    if user_input:
        #  chatbot's response
        response = get_chatbot_response(user_input)
        st.write(f"Chatbot: {response}")

    #quit button
    if st.button("Quit"):
        st.write("Chatbot: Goodbye! Have a great day!")
        st.stop()


if __name__ == "__main__":
    main()