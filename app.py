
import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------
st.set_page_config(
    page_title="Computational Science and Molecular Modeling Laboratory",
    page_icon="⚛️",
    layout="wide"
)

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.title("Computational Science and Molecular Modeling Laboratory")
st.subheader("Research Team, Scientific Activities and Projects")

st.success("Laboratory dashboard is running successfully!")

st.markdown("""
An interdisciplinary research laboratory integrating computational
science, molecular modeling, simulation, bioinformatics and artificial
intelligence.
""")

st.divider()

# -------------------------------------------------
# KEY INDICATORS
# -------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Research Groups", "3")
col2.metric("Research Projects", "6")
col3.metric("Core Research Areas", "3")
col4.metric("Shared Resources", "4")

st.divider()

# -------------------------------------------------
# RESEARCH GROUPS
# -------------------------------------------------
st.header("1. Research Groups")

group1, group2, group3 = st.columns(3)

with group1:
    with st.container(border=True):
        st.subheader("⚛️ Quantum Chemistry")
        st.markdown("**Focus areas:**")
        st.markdown("""
        - Density Functional Theory (DFT)
        - Ab initio calculations
        - Molecular orbitals
        - Noncovalent interactions
        - QTAIM and NCI analysis
        """)
        st.markdown("**Software:**")
        st.caption("ORCA, Gaussian, Psi4, Multiwfn")

with group2:
    with st.container(border=True):
        st.subheader("🔬 Molecular Dynamics")
        st.markdown("**Focus areas:**")
        st.markdown("""
        - Molecular dynamics
        - Molecular mechanics
        - Monte Carlo simulations
        - Adsorption and diffusion
        - Materials and water modeling
        """)
        st.markdown("**Software:**")
        st.caption("GROMACS, LAMMPS, AMBER, VMD")

with group3:
    with st.container(border=True):
        st.subheader("🧬 Bioinformatics")
        st.markdown("**Focus areas:**")
        st.markdown("""
        - Protein structure analysis
        - Molecular docking
        - Drug discovery
        - Sequence analysis
        - AI-assisted bioinformatics
        """)
        st.markdown("**Software:**")
        st.caption("AutoDock Vina, PyMOL, Biopython")

st.divider()

# -------------------------------------------------
# STAFF STRUCTURE
# -------------------------------------------------
st.header("2. Laboratory Staff Structure")

st.markdown("""
The laboratory operates through three specialized research groups
supported by shared computational and technical services.
""")

staff = pd.DataFrame({
    "Position": [
        "Laboratory Director",
        "Quantum Chemistry Group Leader",
        "Molecular Dynamics Group Leader",
        "Bioinformatics Group Leader",
        "HPC and System Administrator",
        "Research Scientists",
        "Research Assistants",
        "Graduate Students"
    ],
    "Research Unit": [
        "Laboratory Management",
        "Quantum Chemistry",
        "Molecular Dynamics",
        "Bioinformatics",
        "Shared Technical Support",
        "Research Groups",
        "Research Groups",
        "Research Groups"
    ],
    "Assigned Staff Member": [
        "To be assigned",
        "To be assigned",
        "To be assigned",
        "To be assigned",
        "To be assigned",
        "To be assigned",
        "To be assigned",
        "To be assigned"
    ]
})

st.dataframe(
    staff,
    width="stretch",
    hide_index=True
)

st.divider()


# -------------------------------------------------
# STAFF PROFILES
# -------------------------------------------------

st.header("3. Research Team Members")

st.markdown("""
Academic and technical personnel working across the
three specialized research groups.
""")

staff_data = pd.DataFrame({
    "Name": [
        "Laboratory Director",
        "Quantum Chemistry Leader",
        "Molecular Dynamics Leader",
        "Bioinformatics Leader",
        "HPC Administrator"
    ],
    "Academic Position": [
        "Assistant Professor",
        "Faculty Member",
        "Faculty Member",
        "Faculty Member",
        "Technical Specialist"
    ],
    "Research Group": [
        "Laboratory Management",
        "Quantum Chemistry",
        "Molecular Dynamics",
        "Bioinformatics",
        "Shared Technical Support"
    ],
    "Specialization": [
        "Computational Science and Molecular Modeling",
        "DFT, SAPT and Molecular Interactions",
        "Molecular Dynamics and Materials Simulation",
        "Bioinformatics and Molecular Docking",
        "HPC, Linux and Slurm"
    ],
    "Email": [
        "To be added",
        "To be added",
        "To be added",
        "To be added",
        "To be added"
    ],
    "Publications": [
        "To be added",
        "To be added",
        "To be added",
        "To be added",
        "To be added"
    ]
})

st.dataframe(
    staff_data,
    width="stretch",
    hide_index=True
)

st.divider()

# -------------------------------------------------
# RESEARCH PROJECTS
# -------------------------------------------------
st.header("2. Research Projects")

projects = pd.DataFrame({
    "Research Group": [
        "Quantum Chemistry",
        "Quantum Chemistry",
        "Molecular Dynamics",
        "Molecular Dynamics",
        "Bioinformatics",
        "Bioinformatics"
    ],
    "Research Project": [
        "Noncovalent Interactions in Molecular Systems",
        "Computational Design of Advanced Materials",
        "Molecular Modeling of Water Purification",
        "Adsorption of Pollutants on Nanomaterials",
        "Protein-Ligand Interaction Studies",
        "AI-Assisted Drug Discovery"
    ],
    "Research Area": [
        "Molecular interactions",
        "Materials science",
        "Water treatment",
        "Environmental modeling",
        "Computational biology",
        "Artificial intelligence"
    ],
    "Status": [
        "Proposed", "Proposed", "Proposed",
        "Proposed", "Proposed", "Proposed"
    ]
})

st.dataframe(
    projects,
    use_container_width=True,
    hide_index=True
)

st.divider()

# -------------------------------------------------
# PROJECT DISTRIBUTION
# -------------------------------------------------
st.header("3. Research Project Distribution")

project_counts = (
    projects["Research Group"]
    .value_counts()
    .rename_axis("Research Group")
    .reset_index(name="Number of Projects")
)

fig = px.pie(
    project_counts,
    names="Research Group",
    values="Number of Projects",
    hole=0.45,
    title="Projects Across Research Groups"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# -------------------------------------------------
# SHARED COMPUTATIONAL RESOURCES
# -------------------------------------------------
st.header("4. Shared Computational Resources")

resources = [
    "High-Performance Computing (HPC)",
    "Artificial Intelligence and Machine Learning",
    "Python Programming and Scientific Data Analysis",
    "Scientific Visualization and Research Data Management"
]

for resource in resources:
    st.markdown(f"• {resource}")

st.divider()

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown(
    "**Computational Science and Molecular Modeling Laboratory**"
)
st.caption("Research, Innovation and Interdisciplinary Collaboration")
