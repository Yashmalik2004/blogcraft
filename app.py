import streamlit as st
from google import genai
from apikey import google_gemini_api_key

def generate_blog_post(blog_title, keyword_ip, number_words, img_consent, img_count):
    client = genai.Client(api_key=google_gemini_api_key)

    keywords_str = ', '.join(
      [kw.strip() for kw in keyword_ip.split(',')]
    ) #formatting the keywords for the prompt
    
    if img_consent == "Yes":
      img_instruction = f""" Suggest exactly {img_count} relevant images throughout the article. Format them clearly as placeholders. For example: [IMAGE 1 PLACEHOLDER: A brief description of what the image should show, e.g., A futuristic robot painting on a canvas]"
      """
    else:
      img_instruction = "Do not include any image suggestions in the article."
    
    # Creating the prompt for the AI model
    prompt = f""" 
    You are an expert content writer and SEO specialist.  
    Write a comprehensive, engaging blog post with the following specifications:
    
    - Title: "{blog_title}"
    - Keywords to include: {keywords_str}
    - Approximate length: {number_words} words
    
    {img_instruction}

    Ensure the content is original, informative, maintains a consistent and engaging tone, and flows naturally between paragraphs.
    """
    
    # generating the blog post using the Google Gemini API
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":

  st.set_page_config(layout="wide") #set layout to wide

  st.title("blogcraft - AI powered blogging platform") #title for web app
  st.subheader("Generate blog posts with AI") #subheader for web app

  with st.sidebar:
    st.header("Input your blog details below:") #header for sidebar
    st.subheader("Enter your blog title and description") #subheader for sidebar
    blog_title = st.text_input("Blog Title") #text input for blog title
    keyword_ip = st.text_input("Enter your blog keywords (comma separated)") #text input for blog keywords

    number_words = st.slider("select number of words in your blog post", 250, 1000, 250) #slider for number of words in blog post
    img_consent = st.radio("Do you want to generate images for your blog post?", ("Yes", "No")) #radio button for image generation consent
    img_count = 0
    
if img_consent == "Yes":
  img_count = st.slider("How many images do you want in your blog?", 1,5,1) #slider for number of images in blog post

submit_btn = st.button("Generate blog") #button to generate blog post

if submit_btn:
    if not blog_title:
        st.warning("Please enter a blog title.")
    elif not keyword_ip:
        st.warning("Please enter at least one keyword.")
    else:
        with st.spinner("Generating blog..."):
            blog_post = generate_blog_post(
                blog_title,
                keyword_ip,
                number_words,
                img_consent,
                img_count
            )
        st.markdown(blog_post)
