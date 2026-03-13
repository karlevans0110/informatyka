import streamlit as st
from random import randint
from time import sleep

st.set_page_config(
    page_title='Zgaduj liczbę!',
    page_icon='❓',
    layout='centered'
)

st.title('❓Czy uda ci się zgadnąć liczbę?')

#PODSTAWA DZIAŁANIA
if 'szukana' not in st.session_state:
    st.session_state.szukana = randint(1, 100)
if 'proby' not in st.session_state:
    st.session_state.proby = 0

st.subheader(f'Zgaduj liczbę w przedziale od 1 do 100')

#PROGRAM
zgadywana_inp = st.text_input('Zgaduj liczbę!', placeholder='Tu wpisz twój guess')
if zgadywana_inp:
    try:
        zgadywana = int(zgadywana_inp)
    except ValueError:
        st.error('Można zgadywać tylko liczby całkowite!')
    else:
        with st.spinner('Sprawdzam...'):
            sleep(1)
        if zgadywana == st.session_state.szukana:
            st.success('Udało ci się zgadnąć liczbę!')
            st.write(f'Liczba prób: {st.session_state.proby}')
        elif zgadywana < st.session_state.szukana:
            st.warning('Za mało!')
            st.session_state.proby += 1
        elif zgadywana > st.session_state.szukana:
            st.info('Za dużo!')
            st.session_state.proby += 1
st.divider()