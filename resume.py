import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="JobFinder | Jobs & Careers",
    page_icon="💼",
    layout="wide"
)

# =========================================================
# DARK PROFESSIONAL THEME
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #080b12;
    color: #ffffff;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Headings */

h1 {
    color: #ffffff !important;
    font-size: 40px !important;
    font-weight: 750 !important;
}

h2 {
    color: #ffffff !important;
    font-weight: 700 !important;
}

h3 {
    color: #e5e7eb !important;
}

/* Text */

p {
    color: #b8c1d1 !important;
}

/* Inputs */

.stTextInput input,
.stTextArea textarea {
    background-color: #10151f !important;
    color: #ffffff !important;
    border: 1px solid #293344 !important;
    border-radius: 9px !important;
}

/* Select boxes */

div[data-baseweb="select"] {
    background-color: #10151f !important;
    border-radius: 9px !important;
}

div[data-baseweb="select"] * {
    color: #ffffff !important;
}

/* Buttons */

.stButton > button {
    width: 100%;
    min-height: 44px;
    border-radius: 9px;
    border: none;
    background: linear-gradient(
        90deg,
        #2563eb,
        #4f46e5
    );
    color: white;
    font-weight: 650;
    font-size: 15px;
}

.stButton > button:hover {
    background: linear-gradient(
        90deg,
        #1d4ed8,
        #4338ca
    );
}

/* Resume uploader */

section[data-testid="stFileUploaderDropzone"] {
    background-color: #10151f;
    border: 1px dashed #3b82f6;
    border-radius: 12px;
}

/* Divider */

hr {
    border-color: #273244;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "resume_uploaded" not in st.session_state:
    st.session_state.resume_uploaded = False

if "applications" not in st.session_state:
    st.session_state.applications = []


# =========================================================
# JOB DATA
# =========================================================

jobs = [
    {
        "title": "AI / ML Intern",
        "company": "TechNova Solutions",
        "location": "Hyderabad",
        "type": "Internship",
        "salary": "₹15,000 - ₹25,000 / month",
        "experience": "Fresher",
        "skills": [
            "Python",
            "Machine Learning",
            "AI"
        ]
    },
    {
        "title": "Software Engineer",
        "company": "InnovateTech",
        "location": "Bangalore",
        "type": "Full Time",
        "salary": "₹6 - ₹10 LPA",
        "experience": "0–2 Years",
        "skills": [
            "Java",
            "Python",
            "SQL"
        ]
    },
    {
        "title": "Frontend Developer",
        "company": "DigitalWorks",
        "location": "Hyderabad",
        "type": "Full Time",
        "salary": "₹5 - ₹8 LPA",
        "experience": "0–2 Years",
        "skills": [
            "React",
            "JavaScript",
            "HTML"
        ]
    },
    {
        "title": "Data Analyst Intern",
        "company": "DataSphere",
        "location": "Remote",
        "type": "Internship",
        "salary": "₹12,000 - ₹20,000 / month",
        "experience": "Fresher",
        "skills": [
            "Python",
            "SQL",
            "Power BI"
        ]
    }
]


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("💼 JobFinder")

    st.caption("Jobs • Careers • Opportunities")

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "🏠 Find Jobs",
            "📄 My Resume",
            "📋 My Applications",
            "👤 My Profile"
        ]
    )

    st.divider()

    st.caption(
        "Find opportunities. Build your career."
    )


# =========================================================
# FIND JOBS
# =========================================================

if page == "🏠 Find Jobs":

    st.title("💼 Find Your Next Opportunity")

    st.write(
        "Search jobs, discover opportunities, upload your resume, "
        "and apply directly from one professional platform."
    )

    st.divider()

    # -----------------------------------------------------
    # SEARCH
    # -----------------------------------------------------

    st.subheader("🔎 Search Jobs")

    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:

        search = st.text_input(
            "Job title or keyword",
            placeholder="e.g. Python Developer, AI Engineer"
        )

    with col2:

        location_filter = st.selectbox(
            "Location",
            [
                "Any Location",
                "Hyderabad",
                "Bangalore",
                "Remote"
            ]
        )

    with col3:

        job_type_filter = st.selectbox(
            "Job Type",
            [
                "All Types",
                "Full Time",
                "Internship"
            ]
        )

    st.divider()

    # -----------------------------------------------------
    # FILTER JOBS
    # -----------------------------------------------------

    filtered_jobs = []

    for job in jobs:

        matches_search = (
            not search
            or search.lower() in job["title"].lower()
            or search.lower() in job["company"].lower()
            or any(
                search.lower() in skill.lower()
                for skill in job["skills"]
            )
        )

        matches_location = (
            location_filter == "Any Location"
            or job["location"] == location_filter
        )

        matches_type = (
            job_type_filter == "All Types"
            or job["type"] == job_type_filter
        )

        if (
            matches_search
            and matches_location
            and matches_type
        ):
            filtered_jobs.append(job)

    # -----------------------------------------------------
    # JOB RESULTS
    # -----------------------------------------------------

    st.subheader(
        f"💼 Available Jobs ({len(filtered_jobs)})"
    )

    if not filtered_jobs:

        st.info(
            "No jobs found. Try another keyword, "
            "location or job type."
        )

    # -----------------------------------------------------
    # JOB CARDS
    # -----------------------------------------------------

    for index, job in enumerate(filtered_jobs):

        st.markdown(
            f"### 💼 {job['title']}"
        )

        st.write(
            f"**{job['company']}**"
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(
                f"📍 **Location**\n\n"
                f"{job['location']}"
            )

        with col2:
            st.write(
                f"💼 **Job Type**\n\n"
                f"{job['type']}"
            )

        with col3:
            st.write(
                f"💰 **Salary**\n\n"
                f"{job['salary']}"
            )

        st.write(
            f"🎓 **Experience:** "
            f"{job['experience']}"
        )

        st.write("🛠️ **Required Skills**")

        st.info(
            "  •  ".join(job["skills"])
        )

        apply_col, save_col = st.columns(2)

        with apply_col:

            if st.button(
                "🚀 Apply Now",
                key=f"apply_{index}"
            ):

                if not st.session_state.resume_uploaded:

                    st.warning(
                        "Please upload your resume "
                        "before applying."
                    )

                    st.info(
                        "Go to **📄 My Resume** "
                        "and upload your resume."
                    )

                else:

                    application = {
                        "job": job["title"],
                        "company": job["company"],
                        "status": "Application Submitted"
                    }

                    if application not in st.session_state.applications:

                        st.session_state.applications.append(
                            application
                        )

                    st.success(
                        f"Application submitted for "
                        f"{job['title']}!"
                    )

        with save_col:

            st.button(
                "♡ Save Job",
                key=f"save_{index}"
            )

        st.divider()


# =========================================================
# MY RESUME
# =========================================================

elif page == "📄 My Resume":

    st.title("📄 My Resume")

    st.write(
        "Create your professional profile and keep "
        "your resume ready for job applications."
    )

    st.divider()

    # -----------------------------------------------------
    # RESUME UPLOAD
    # -----------------------------------------------------

    st.subheader("📤 Upload Resume")

    resume = st.file_uploader(
        "Upload your latest resume",
        type=[
            "pdf",
            "doc",
            "docx"
        ],
        help="Supported formats: PDF, DOC and DOCX"
    )

    if resume:

        st.session_state.resume_uploaded = True

        st.success(
            f"✓ Resume uploaded successfully: "
            f"{resume.name}"
        )

    elif st.session_state.resume_uploaded:

        st.success(
            "✓ Your resume is ready for job applications."
        )

    st.divider()

    # -----------------------------------------------------
    # PERSONAL DETAILS
    # -----------------------------------------------------

    st.subheader("👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:

        full_name = st.text_input(
            "Full Name",
            placeholder="Enter your full name"
        )

        email = st.text_input(
            "Email Address",
            placeholder="example@gmail.com"
        )

        phone = st.text_input(
            "Phone Number",
            placeholder="+91 XXXXX XXXXX"
        )

    with col2:

        location = st.text_input(
            "Current Location",
            placeholder="Hyderabad, Telangana"
        )

        education = st.text_input(
            "Highest Qualification",
            placeholder="B.Tech CSE"
        )

        experience = st.selectbox(
            "Experience Level",
            [
                "Fresher",
                "0–1 Years",
                "1–3 Years",
                "3–5 Years",
                "5+ Years"
            ]
        )

    # -----------------------------------------------------
    # SKILLS
    # -----------------------------------------------------

    st.subheader("💻 Skills")

    skills = st.multiselect(
        "Select your skills",
        [
            "Python",
            "Java",
            "C",
            "C++",
            "JavaScript",
            "React.js",
            "Node.js",
            "SQL",
            "MongoDB",
            "Machine Learning",
            "Artificial Intelligence",
            "Data Science",
            "Cloud Computing",
            "Git & GitHub"
        ]
    )

    # -----------------------------------------------------
    # SUMMARY
    # -----------------------------------------------------

    st.subheader("📝 Professional Summary")

    summary = st.text_area(
        "About You",
        placeholder=(
            "Write a short professional summary about "
            "your skills, projects and career goals..."
        ),
        height=130
    )

    # -----------------------------------------------------
    # PROJECTS
    # -----------------------------------------------------

    st.subheader("🚀 Projects")

    projects = st.text_area(
        "Project Details",
        placeholder=(
            "Mention your important academic, "
            "personal or professional projects..."
        ),
        height=120
    )

    # -----------------------------------------------------
    # SAVE
    # -----------------------------------------------------

    if st.button("💾 Save Resume Profile"):

        if not full_name:

            st.error(
                "Please enter your full name."
            )

        elif not email:

            st.error(
                "Please enter your email address."
            )

        elif not st.session_state.resume_uploaded:

            st.error(
                "Please upload your resume."
            )

        else:

            st.success(
                "✓ Your resume profile has been saved "
                "successfully."
            )


# =========================================================
# MY APPLICATIONS
# =========================================================

elif page == "📋 My Applications":

    st.title("📋 My Applications")

    st.write(
        "Track the jobs you have applied for."
    )

    st.divider()

    if not st.session_state.applications:

        st.info(
            "You haven't applied to any jobs yet."
        )

        st.write(
            "Go to **🏠 Find Jobs** to discover "
            "available opportunities."
        )

    else:

        st.subheader(
            f"Applications ({len(st.session_state.applications)})"
        )

        for application in st.session_state.applications:

            st.markdown(
                f"### 💼 {application['job']}"
            )

            st.write(
                f"**Company:** {application['company']}"
            )

            st.success(
                f"Status: {application['status']}"
            )

            st.divider()


# =========================================================
# MY PROFILE
# =========================================================

elif page == "👤 My Profile":

    st.title("👤 My Profile")

    st.write(
        "Manage your professional profile and career preferences."
    )

    st.divider()

    # -----------------------------------------------------
    # PROFILE STATS
    # -----------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Available Jobs",
            len(jobs)
        )

    with col2:

        st.metric(
            "Applications",
            len(st.session_state.applications)
        )

    with col3:

        resume_status = (
            "Ready"
            if st.session_state.resume_uploaded
            else "Pending"
        )

        st.metric(
            "Resume",
            resume_status
        )

    st.divider()

    # -----------------------------------------------------
    # CAREER PREFERENCES
    # -----------------------------------------------------

    st.subheader("🎯 Career Preferences")

    preferred_role = st.text_input(
        "Preferred Job Role",
        placeholder="e.g. AI Engineer"
    )

    preferred_location = st.selectbox(
        "Preferred Location",
        [
            "Hyderabad",
            "Bangalore",
            "Chennai",
            "Pune",
            "Delhi",
            "Remote"
        ]
    )

    preferred_type = st.selectbox(
        "Preferred Employment Type",
        [
            "Full Time",
            "Internship",
            "Part Time",
            "Remote"
        ]
    )

    if st.button(
        "💾 Save Career Preferences"
    ):

        st.success(
            "✓ Career preferences saved successfully."
        )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "💼 JobFinder | Discover Jobs • Upload Resume • "
    "Apply • Track Applications"
)