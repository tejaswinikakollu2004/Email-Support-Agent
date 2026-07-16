if st.button("Generate Reply"):
    if user_input.strip() == "":
        st.warning("Please enter a query")
    else:
        user_input = user_input.lower()

        if "delay" in user_input:
            response = "We apologize for the delay. Your order will arrive soon."
        elif "refund" in user_input:
            response = "Your refund has been initiated and will be processed soon."
        elif "cancel" in user_input:
            response = "Your order has been successfully cancelled."
        else:
            response = "Thank you for contacting support. We will get back to you shortly."

        st.success("Reply Generated ✅")
        st.write(response)