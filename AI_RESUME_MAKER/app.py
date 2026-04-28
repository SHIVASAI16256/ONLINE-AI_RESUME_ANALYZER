import streamlit as st
import PyPDF2

# Skills database
required_skills = {
    "Java Developer": ["Java", "SQL", "Spring", "Git", "OOP"],
    "Python Developer": ["Python", "Django", "SQL", "Git", "API"],
    "Frontend Developer": ["HTML", "CSS", "JavaScript", "React", "Git"]
}

def extract_text_from_pdf(uploaded_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    for page in pdf_reader.pages:
        text += page.extract_text()

    return text

def analyze_resume(text, role):
    score = 0
    found_skills = []
    missing_skills = []

    skills = required_skills[role]

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)
            score += 20
        else:
            missing_skills.append(skill)

    return score, found_skills, missing_skills

st.title("AI Resume Analyzer")

role = st.selectbox(
    "Select Job Role",
    ["Java Developer", "Python Developer", "Frontend Developer"]
)

uploaded_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])

if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)

    score, found, missing = analyze_resume(text, role)

    st.subheader("Resume Analysis Result")

    st.write(f"Resume Score: {score}/100")

    st.write("### Found Skills")
    st.write(found)

    st.write("### Missing Skills")
    st.write(missing)

    if score >= 80:
        st.success("Excellent Resume!")
    elif score >= 50:
        st.warning("Good Resume, but needs improvement.")
    else:
        st.error("Resume needs major improvement.")