import streamlit as st
import random
import os

base_dir = os.path.dirname(__file__)
pdf_dis_dir = os.path.join(base_dir, "dis_pdfs")
pdf_tech_dir = os.path.join(base_dir, "tech_pdfs")
status_dir = os.path.join(base_dir, "status")

disease_options = ['Depression',
                   'Epilepsy',
                   'Obsessive-Compulsive Disorder (OCD)',
                   'Parkinson\'s Disease',
                   'Tremor',
                   'Chronic Pain']

disease_dict = {
    'Depression': 'Depression',
    'Epilepsy': 'Epilepsy',
    'Obsessive-Compulsive Disorder (OCD)': 'OCD',
    'Parkinson\'s Disease': 'PD',
    'Tremor': 'Tremor',
    'Chronic Pain': 'Pain'
}

technology_dict = {
    'Deep Brain Stimulation (DBS)': 'DBS',
    'Focused Ultrasound (FUS)': 'FUS',
    'Spinal Cord Stimulation (SCS)': 'SCS',
    'Transcranial Magnetic Stimulation (TMS)': 'TMS',
    'Vagus Nerve Stimulation (VNS)': 'VNS',
    'Magnetic Seizure Therapy (MST)': 'MST',
    'Transcranial Direct Current Stimulation (tDCS)': 'TDCS',
    'Transcutaneous Electrical Nerve Stimulation (TENS)': 'TENS'
}

if 'disease' not in st.session_state:
    st.session_state['disease'] = random.choice(disease_options)

if 'disease_index' not in st.session_state:
    st.session_state['disease_index'] = 0  # start with first image

if 'tech_index' not in st.session_state:
    st.session_state['tech_index'] = 0  # start with first image

if 'selected_tech_list' not in st.session_state:
    st.session_state['selected_tech_list'] = []

if 'player_considerations' not in st.session_state:
    st.session_state['player_considerations'] = ""

def handle_tech_change():
    '''
    Reset the image index when the technology selection changes.
    '''
    st.session_state['tech_index'] = 0

def update_selected_tech_list():
    st.session_state.selected_tech_list = st.session_state.select_tech

def update_player_considerations():
    st.session_state.player_considerations = st.session_state.considerations

select_page = st.sidebar.radio("Contents",
                               ["Introduction",
                                "Brain Disease information", 
                                "Choose Neurotechnology", 
                                "Survey"])

if select_page == "Introduction":

    st.title("Welcome to NeuroGame!")

    st.markdown("""
    ### Learning Objectives:""")
    
    st.markdown("- Learn about brain diseases, their symptoms, demographics, and any identified neuroscientific basis behind the diseases.")
    st.markdown("- Learn about the various neurotechnologies available for the treatment of a disease.")
    st.markdown("- Assess various features of a neurotechnology towards making an informed decision on the best possible neurotechnological treatment for a disease.")
    st.markdown("- Share your thoughts and considerations with others behind your choice of neurotechnology for treatment of a disease.")
    st.markdown('''
        <style>
        [data-testid="stMarkdownContainer"] ul{
            padding-left:40px;
        }
        </style>
        ''', unsafe_allow_html=True)

    st.markdown(""" ### Gameplay Instructions: """)
    st.markdown("""
                1. You will be working in small groups of 3-4. Each group is randomly assigned a brain disease from a list of 6 diseases.
                2. You can view information about the assigned disease such as symptoms, demographics, and any identified neuroscientific basis behind the disease.
                3. You can then view details about various neurotechnologies from a list of 8 neurotechnologies and choose a neurotechnology that you think is best suited for treatment of the assigned disease.
                4. As you view the neurotechnologies, identify which ones have potential applications towards the treatment of the disease assigned to your group.
                5. Once you have filtered out the neurotechnologies that you think are relevant for treatment of the assigned disease, 
                   you can weigh in the various aspects of these neurotechnologies to select one or more neurotechnologies that you think is/are 
                   the best suited.
                6. There are a bunch of guiding questions that you can consider towards making your decision. As you do so, note down
                   your thoughts and considerations, for discussions later.
                7. At the end of this game, you can also share your feedback and reflections about the game or about the use of neurotechnologies 
                   in a clinical context through a survey.
                """)

elif select_page == "Brain Disease information":

    disease_assigned = st.session_state['disease']

    st.title(f"You have been assigned the disease: **{disease_assigned}**")

    pdf_files = [
        os.path.join(pdf_dis_dir, f"{disease_dict[disease_assigned]}_1.pdf"),
        os.path.join(pdf_dis_dir, f"{disease_dict[disease_assigned]}_2.pdf")
    ]
    
    max_index = len(pdf_files) - 1
    min_index = 0

    col1, col2 = st.columns([1.6, 1])
    with col1:
        if st.session_state['disease_index'] > min_index:
            if st.button("Front"):
                st.session_state['disease_index'] -= 1
                st.rerun()

    with col2:
        if st.session_state['disease_index'] < max_index:
            if st.button("Back"):
                st.session_state['disease_index'] += 1
                st.rerun()
        

    current_disease_index = st.session_state.disease_index
    st.pdf(pdf_files[current_disease_index], height=600)
    
    if st.button("Choose another disease"):
        st.session_state['disease'] = random.choice(disease_options)
        st.session_state['disease_index'] = 0
        current_disease_index = st.session_state.disease_index
        st.rerun()

elif select_page == "Choose Neurotechnology":

    st.title(f"Choose a Neurotechnology that you think is best suited for treatment of {st.session_state['disease']}")

    col_left, col_right = st.columns([1, 3])

    with col_left:
        view_technology = st.radio("View the details of a Neurotechnology by selecting from the list below:",
                                ['Deep Brain Stimulation (DBS)',
                                    'Focused Ultrasound (FUS)',
                                    'Spinal Cord Stimulation (SCS)',
                                    'Transcranial Magnetic Stimulation (TMS)',
                                    'Vagus Nerve Stimulation (VNS)',
                                    'Magnetic Seizure Therapy (MST)',
                                    'Transcranial Direct Current Stimulation (tDCS)',
                                    'Transcutaneous Electrical Nerve Stimulation (TENS)'],
                                    on_change=handle_tech_change)

    with col_right:
        if view_technology:

            pdf_files = [
                os.path.join(pdf_tech_dir, f"{technology_dict[view_technology]}_1.pdf"),
                os.path.join(pdf_tech_dir, f"{technology_dict[view_technology]}_2.pdf")
            ]

            max_index = len(pdf_files) - 1
            min_index = 0

            col1, col2 = st.columns([6, 1])
            with col1:
                if st.session_state.tech_index > min_index:
                    if st.button("Front"):
                        st.session_state['tech_index'] -= 1
                        st.rerun()

            with col2:
                if st.session_state.tech_index < max_index:
                    if st.button("Back"):
                        st.session_state['tech_index'] += 1
                        st.rerun()
                

            current_tech_index = st.session_state['tech_index']
            st.pdf(pdf_files[current_tech_index], height=600)
    
    st.header(f"Select the Neurotechnology you think is best suited for treatment of {st.session_state['disease']} (you can select multiple)")
    
    with st.expander("Guiding questions"):
        st.text("Consider the following guiding questions while making your choice(s):")
        st.markdown("- Which neurotechnology(ies) have potential applications towards the treatment of the assigned disease?")
        st.markdown("""- Among the neurotechnologies that have potential applications, which one(s) do you think is/are the 
                    most beneficial for the treatment of the assigned disease?""")
        st.markdown("- Reflect upon the invasiveness/intrusiveness of the technologies? Does that influence your decision?")
        st.markdown("""- Is safety more important or is the effectiveness of the technology more important? Hypothetically, if 
                    you find yourself or a loved one in a situation seeking technological intervention, would you choose a 
                    technology that has higher effectiveness but also higher risks over one which is safer but less effective?""")
        st.markdown("- Additionally, are there technologies that you perceive " \
        "as requiring more regular visits to a clinic as they may not be easily administrable at home? If yes, how do you think " \
        "it affects the day-to-day routine of a patient and their caretakers? And does that influence your decision?")
        st.markdown("-  Reflect upon the affordability of the technologies and the implications of the same towards an " \
        "equitable access to treatment.")
        st.markdown("- Does the regulatory status of the technology influence your decision? ")
        
        status = os.path.join(status_dir, "regulatory.pdf")
        st.pdf(status, height=600)
    

    st.multiselect('options',['Deep Brain Stimulation (DBS)',
                    'Focused Ultrasound (FUS)',
                    'Spinal Cord Stimulation (SCS)',
                    'Transcranial Magnetic Stimulation (TMS)',
                    'Vagus Nerve Stimulation (VNS)',
                    'Magnetic Seizure Therapy (MST)',
                    'Transcranial Direct Current Stimulation (tDCS)',
                    'Transcutaneous Electrical Nerve Stimulation (TENS)'],
                    default=st.session_state.selected_tech_list,
                    key='select_tech',
                    on_change=update_selected_tech_list,
                    label_visibility="hidden")
    
    if len(st.session_state['selected_tech_list']) >= 1:

        st.markdown("### Please note any considerations/thoughts behind your choice(s) for sharing with the other participants. You can refer " \
        "to the guiding questions above while noting down your thoughts.")
        
        user_thoughts = st.text_area("",
                                     height=200,
                                     value=st.session_state.player_considerations,
                                     key='considerations',
                                     on_change=update_player_considerations)
    
else:
    # link to survey app
    st.markdown("## Proceed to the Survey to share your feedback about the game and any reflections on what you learnt")
    st.markdown("Thank you for participating in this activity! We hope it helped you appreciate the complex " \
    "considerations behind brain health and care, and helped reflect upon the various aspects of technological interventions " \
    "that influence a person's (and/or their caretakers) choice in making a well-informed decision.")
    st.markdown("We would love to hear " \
    "from you what you thought about this activity, any feedback you have or any personal reflections that you would like " \
    "to share about the use of neurotechnologies in a clinical context. ") 
    
    st.markdown("Please click the link below to proceed to a survey where you can share the same with us:")
    st.markdown("[Survey Link](https://forms.office.com/r/cjZ3H3k9Xf)")