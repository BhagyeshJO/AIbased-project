import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain_huggingface import HuggingFaceEndpoint
import os


st.set_page_config(page_title="Generate Blogs",page_icon='🔥',layout='centered',initial_sidebar_state='collapsed')
os.environ["HugginFaceHub"]= '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'

repo_id= "meta-llama/Meta-Llama-3.1-8B-Instruct"

#Function to get response fromm my Llama 2 model
def getLLamaresponse(input_text, no_words, blog_style):
    ###Llama2 model
    llm=HuggingFaceEndpoint(repo_id=repo_id, max_length=128, temperature=0.7)


    ###Prompt template

    template="""
        Write a blog for {blog_style}  job profile for a topic {input_text}
        withing {no_words} words.
    """
    prompt= PromptTemplate(input_variables= ["blog_style", "input_text", "no_words"], template=template)

    ## Generate the response from the llama 2 model
    response=llm.invoke(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response)
    return response

st.header("Generate Blogs 🔥")

input_text=st.text_input("Enter the Blog Topic")

## creating two more columns for additional 2 fields
col1,col2 = st.columns([5,5])

with col1:
    no_words=st.text_input('No of words to generate')

with col2:
    blog_style= st.selectbox('Writing the blog for: ', ('Researchers','Data Scientists', 'Common People'), index=0)

submit=st.button("Generate")

##Final response
if submit:
    st.write(getLLamaresponse(input_text, no_words, blog_style))
