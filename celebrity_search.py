import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
import streamlit as st

os.environ['OPENAI_API_KEY']=openai_key

#Streamlit framework

st.title('Celebrity Search Application')
input_text=st.text_input("Search")

#Prompt Template
first_prompt=PromptTemplate(input_variables=['name'],template="Tell me about celebrity {name}")

person_memory=ConversationBufferMemory(input_key='name', memory_key='chat_history')
dob_memory=ConversationBufferMemory(input_key='person', memory_key='chat_history')
event_memory=ConversationBufferMemory(input_key='dob', memory_key='event_history')


#OPENAI LLM
llm=OpenAI(temperature=0.8)
chain1=LLMChain(
    llm=llm, prompt=first_prompt, verbose=True, output_key='person')

second_prompt=PromptTemplate(input_variables=['person'],template="when was {person} born")


chain2=LLMChain(
    llm=llm, prompt=second_prompt, verbose=True, output_key='dob')

third_prompt=PromptTemplate(input_variables=['dob'],template="Mention 5 events that happened on {dob} around the world")

chain3=LLMChain(
    llm=llm, prompt=second_prompt, verbose=True, output_key='events')

parent_chain=SequentialChain(
    chains=[chain1, chain2, chain3], input_variables=['name'], output_variables=['person', 'dob', 'events'], verbose=True)

if input_text:
    st.write(parent_chain({'name':input_text}))

    with st.expander('Person'):
        st.info(person_memory.buffer)

    with st.expander('Events'):
        st.info(event_memory.buffer)

    