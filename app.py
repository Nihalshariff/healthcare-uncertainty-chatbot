import streamlit as st

# Page settings
st.set_page_config(
    page_title="Healthcare Uncertainty Chatbot",
    page_icon="🩺",
    layout="wide"
)

# Title
st.markdown(
    """
    <h2 style="margin-bottom:10px;">
    🩺 Healthcare Uncertainty Chatbot
    </h2>
    """,
    unsafe_allow_html=True
)

# Input
symptom = st.text_input("Describe your symptom")

if symptom:

    symptom = symptom.lower()

    if "headache" in symptom:

        response = (
            "Possible causes include stress, dehydration or lack of sleep."
        )

        confidence = "Medium"

        reason = (
            "Several common explanations exist for this symptom."
        )

        advice = (
            "Monitor symptoms and seek medical advice if they worsen."
        )

    elif "chest pain" in symptom:

        response = (
            "Chest pain can have many possible causes and should be assessed by a healthcare professional."
        )

        confidence = "Low"

        reason = (
            "Multiple serious conditions may cause this symptom."
        )

        advice = (
            "Seek medical advice as soon as possible."
        )

    elif "fever" in symptom:

        response = (
            "Possible causes include a viral infection or another illness."
        )

        confidence = "Medium"

        reason = (
            "More than one possible explanation exists."
        )

        advice = (
            "Monitor symptoms and consider seeking medical advice."
        )

    elif "cough" in symptom:

        response = (
            "A cough may be associated with irritation, infection or other conditions."
        )

        confidence = "Low"

        reason = (
            "The symptom alone provides limited information."
        )

        advice = (
            "Seek advice if symptoms persist."
        )

    else:

        response = (
            "Insufficient information is available to provide a reliable response."
        )

        confidence = "Low"

        reason = (
            "This symptom is not recognised by the prototype."
        )

        advice = (
            "Provide more information or seek professional advice."
        )

    # Response
    st.markdown("### Response")
    st.write(response)

    # Confidence
    st.markdown("### Confidence")

    if confidence == "Medium":
        st.warning(f"Confidence Level: {confidence}")
    else:
        st.error(f"Confidence Level: {confidence}")

    # Reason
    st.write(f"Reason: {reason}")

    # Suggested Action
    st.markdown("### Suggested Action")

    if confidence == "Low":
        st.error(advice)
    else:
        st.warning(advice)

    # Uncertainty Message
    st.markdown("### Uncertainty")

    st.info(
        "This response is uncertain and should not replace professional medical advice."
    )