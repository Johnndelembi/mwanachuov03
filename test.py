import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth


cred = credentials.Certificate("mwanachuo2-7faec-firebase-adminsdk-ddavb-0b8a737a43.json")
try:
    firebase_admin.get_app()
except ValueError as e:
    initialize_app(cred)
    
def app():
# Usernm = []
    col3, col4 = st.columns([4,2])
    col3.image('logo.png', width=100)
    

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''
    if 'regnumber' not in st.session_state:
        st.session_state.regnumber = ''
    if 'college' not in st.session_state:
        st.session_state.college = ''        



    def f(): 
        try:
            user = auth.get_user_by_email(email)
            print(user.uid)
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            st.session_state.regnumber = user.display_name
            
            global Usernm
            Usernm=(user.uid)
            
            st.session_state.signedout = True
            st.session_state.signout = True    
  
            
        except: 
            st.warning('Login Failed')

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''


        
    
        
    if "signedout"  not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False    
        
    student_type = ('Student', 'Leader', )
        
    
    if  not st.session_state["signedout"]: # only show if the state is False, hence the button has never been clicked
        col4.header(' :green[To Get Access] ')
        choice = st.selectbox('Login/Signup',['Login','Sign up'])
        email = st.text_input('Email Address')
        regnumber = st.text_input('Registration number', help='Write your registration number as it shows in your Stident ID')
        password = st.text_input('Password',type='password', help='write a strong password make it so that its easy to remember')

        

        
        if choice == 'Sign up':
            st.subheader('PROFILE INFORMATION')
            username = st.text_input("Enter  your unique username", help='please include your position if you are a leader i.e Jackson Temba: BAEST CR, Janet John: DARUSO VP, James June: MT114 Seminar Leader')
            college = st.text_input('College/School', help='Write your respective college i.e COSS, CoNAS, UDSE')
            category = st.selectbox('Category', student_type, help='Tell us what you identify as, normal student or Leader')
            
            if st.button(' :green[**Create my account**]', use_container_width=True):
                user = auth.create_user(email = email, password = password,uid=username, display_name=regnumber)
                
                st.success('Account created successfully!')
                st.info('Please Login using your email and password')
                st.balloons()
        else:
            # st.button('Login', on_click=f)          
            st.button(' :green[**Login**]', on_click=f, use_container_width=True)
            
            
    if st.session_state.signout:
                container = st.container(border=True)
                container.info(' Successfully signed in as '+st.session_state.username )
                #st.header(' Why Choose MWANACHUO!! ')
                #st.text('Name '+st.session_state.username)
                container.text('Email ID: '+st.session_state.useremail)
                container.text('Reg :'+st.session_state.regnumber )
                
                st.write(' ### ')
 
                st.subheader(':green[+ NEWS FEED] ')
                container1 = st.container(border=True)
                container1.subheader('Welcome to the AIESEC Career Fair 2024')
                container1.markdown(' ***Where talent meets opportunity*** 💯 ')
                container1.image('WhatsApp Image 2024-03-30 at 08.01.26_48cc1211.jpg')
                container1.markdown(''' Join us for a two-day extravaganza hosted by AIESEC in Tanzania on 6th & 7th April at the UDSM New Library Auditorium!🌟 filled with networking🫂, 
                interviews👨🏼‍🏫, skills workshops🧑🏽‍💻, and recruitment🤝🏽 opportunities👨‍💼 with top local and multinational🛩 organizations.🔥💯
                [Register to attend here](https://b.link/CareerFair2024). Don't miss out on an opportunity to reach your dream career! ''')

                st.write(' ### ')

                container2 = st.container(border=True)
                container2.image('resultss.jpg')
                container2.write('First semester results on display!! Visit your aris accounts to view your reults')




                st.button('Sign out', on_click=t)
            
                
    

                            
    def ap():
        st.write('Posts')
