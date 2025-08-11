import streamlit as st
 
# Title of the app
st.title("🎯 FitLens - Job Role Fit Analyzer")
 
# Job Role Description
jobrole = (
    "We are hiring for a **Data Engineer** with experience in **Python, AWS, Glue, Terraform**, and **ETL workflows**. \n"
    "- Minimum **2 years** of experience required.\n"
    "- Strong understanding of **data pipelines** is a plus."
)
st.subheader("📄 Job Description:")
st.write(jobrole)
 
# Text input from user
st.markdown("---")
st.subheader("📝 Paste your resume or skill summary below:")
user_input = st.text_area("Enter your skills and experience here:")
 
# Experience input
experience = st.number_input("👤 Enter your years of experience(in years):", min_value=0, max_value=10, step=1)
 
# Required skills for this role:
required_skills = ["python", "aws", "glue", "terraform", "etl"]
 
# Check fit on button click
if st.button("✅ Check Fit"):
    # Convert input to lowercase and count how many required skills are matched
    matched_skills=[]
    for skill in required_skills:
        if skill in user_input.lower():
            matched_skills.append(skill)
 
    # Check both experience and skill match
    if experience >= 2 and len(matched_skills) >= 2:
        st.success(f"✅ You seem to be a good fit for this role!\n\nMatched skills: {', '.join(matched_skills)}")
    elif experience < 2:
        st.warning("⚠️ You need at least **2 years** of experience for this role.")
    else:
        st.warning("❌ Your skills do not match the minimum job requirements yet.")
 
