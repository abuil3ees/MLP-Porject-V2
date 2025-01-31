import streamlit as st

# Apply custom CSS for green sliders and radio buttons
st.markdown("""
    <style>
        /* Make sliders green */
        .stSlider > div[role="slider"] {
            background-color: #008000 !important; /* Green */
        }

        /* Make radio buttons green */
        div[role="radiogroup"] label div {
            color: #008000 !important; /* Green text */
        }

        /* Make radio button selection dots green */
        div[role="radiogroup"] input:checked + div {
            background-color: #008000 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Display the logo at the top
st.image("logo.png", width=150)  # Smaller logo

# Title of the app
st.title("Leadership Readiness Tool")

# Define behaviors and their 5 questions each
behaviors = {
    "1. We Trust and Respect One Another": [
        {"question": "Do team members demonstrate mutual trust and respect?", "type": "Yes/No"},
        {"question": "Are there regular opportunities for open and honest communication?", "type": "Yes/No"},
        {"question": "How confident are employees that leadership values their input?", "type": "Scale"},
        {"question": "Are actions taken by leadership perceived as fair and equitable?", "type": "Scale"},
        {"question": "Do employees feel they can rely on their colleagues for support?", "type": "Yes/No"}
    ],
    "2. We Are Inclusive and Take Care of Each Other": [
        {"question": "Is inclusivity considered when making decisions that impact employees?", "type": "Yes/No"},
        {"question": "Are employee well-being programs actively promoted?", "type": "Yes/No"},
        {"question": "How supported do employees feel by their managers?", "type": "Scale"},
        {"question": "Are team members encouraged to share diverse perspectives?", "type": "Yes/No"},
        {"question": "Is there a culture of teamwork and collaboration?", "type": "Scale"}
    ],
    "3. We Listen and Communicate Transparently": [
        {"question": "Are mechanisms in place to collect feedback during transitions?", "type": "Yes/No"},
        {"question": "How effectively does leadership communicate changes?", "type": "Scale"},
        {"question": "Are employees confident in leadership’s transparency?", "type": "Scale"},
        {"question": "Is feedback from employees or customers addressed in a timely manner?", "type": "Yes/No"},
        {"question": "Are regular town halls or Q&A sessions conducted?", "type": "Yes/No"}
    ],
    "4. We Embrace Change and Learn Continuously": [
        {"question": "Are employees provided with resources to adapt to new roles?", "type": "Yes/No"},
        {"question": "How willing are employees to embrace change and learn?", "type": "Scale"},
        {"question": "Are lessons learned during transitions documented and used?", "type": "Yes/No"},
        {"question": "Is leadership promoting a culture of continuous learning?", "type": "Scale"},
        {"question": "Are knowledge-sharing sessions encouraged?", "type": "Yes/No"}
    ],
    "5. We Strive to Improve and Innovate Courageously": [
        {"question": "Are innovative ideas encouraged and implemented?", "type": "Yes/No"},
        {"question": "How frequently are process improvements identified?", "type": "Scale"},
        {"question": "Are employees empowered to take risks and innovate?", "type": "Yes/No"},
        {"question": "How confident is leadership in fostering innovation?", "type": "Scale"},
        {"question": "Are there structured programs to support innovation?", "type": "Yes/No"}
    ],
    "6. We Keep Sustainability Top of Mind in Everything We Do": [
        {"question": "Are sustainability goals integrated into transformation processes?", "type": "Yes/No"},
        {"question": "How frequently are sustainability metrics reviewed?", "type": "Scale"},
        {"question": "Are employees and stakeholders aligned on sustainability priorities?", "type": "Scale"},
        {"question": "Are actions being taken to reduce environmental/social impact?", "type": "Yes/No"},
        {"question": "Are suppliers and partners evaluated for sustainability?", "type": "Yes/No"}
    ],
    "7. We Create Value for Customers": [
        {"question": "Are mechanisms in place to minimize customer disruptions?", "type": "Yes/No"},
        {"question": "Is there a process to identify and address customer gaps?", "type": "Yes/No"},
        {"question": "Do employees and leadership collaborate to balance customer needs?", "type": "Scale"},
        {"question": "Are customer satisfaction metrics tracked and improving?", "type": "Yes/No"},
        {"question": "Is customer feedback actively used for decision-making?", "type": "Scale"}
    ],
    "8. We Drive Performance, Celebrate Successes, and Win Together": [
        {"question": "Are performance goals clearly defined and aligned?", "type": "Yes/No"},
        {"question": "How frequently are milestones and achievements recognized?", "type": "Scale"},
        {"question": "Is there a formal process to document lessons learned?", "type": "Yes/No"},
        {"question": "Do employees feel leadership fosters collaboration and motivation?", "type": "Scale"},
        {"question": "Are incentives and recognition programs aligned with contributions?", "type": "Yes/No"}
    ]
}

# Dictionary to store responses
responses = {}

# Display the questions
for behavior, questions in behaviors.items():
    st.subheader(behavior)
    for i, q in enumerate(questions):
        if q["type"] == "Yes/No":
            responses[f"{behavior}_{i}"] = st.radio(q["question"], ["Yes", "No"], index=1)
        elif q["type"] == "Scale":
            responses[f"{behavior}_{i}"] = st.slider(q["question"], min_value=1, max_value=10, value=5)