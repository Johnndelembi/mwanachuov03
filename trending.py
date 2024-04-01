import streamlit as st
from firebase_admin import auth

def app():
    #st.header(' MWANACHUO PLATFORM!! ')
    header1, header2 = st.columns([2,3])
    header1.image('logo.png', width=150)
    #header2.subheader(':green[MWANACHUO PLATFORM] ')
    st.header(' Getting Started with :green[MWANACHUO]')
    col1, col2 = st.columns([2,3])
    col1.video('simu.mp4')  
    col2.markdown(' **A platform for all short-term University/college/Class news and updates. Spreading the word quick and fast across the community** ')
    col2.markdown('''Mwanachuo makes it easier to translate information to students by making sure that students get these information
    on time and that the information is authentic and legit. ''')
    col2.markdown('''After signing up, user will be able to receive latest updates pertaining the univeristy from
    CRs and etc, It is our policy to make sure Mwanachuo facilitate the spread of authentic information and up-to-date information.''')
    col2.markdown('''Mwanachuo will be self-updating itself with every begining of a new week automously therefore minimizing compression of old
    information and making sure user stay updated with the latest news and updates.
    ''')
    col2.write('[Learn More](https://wa.link/p7ke9l)')

    with col2:
        col5, col6 = st.columns(2)
        col5.button(' :green[**Sign Up**]', use_container_width=True)
        col6.button(' :blue[**Contact us**]', use_container_width=True)
        
    st.info(' Page still under construction..')

    st.write(' ### ')
    col1, col2, col3, col4 = st.columns([2,6,2,2])
    col1.caption('mwanachuo.app')
    col3.caption(' [Privacy Policy]()')
    col4.caption( ' [Terms of Use]() ')
    