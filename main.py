import streamlit as st
from streamlit_option_menu import option_menu
import os
import replicate
import requests
from streamlit_image_select import image_select
from htbuilder import HTML
from pathlib import Path

#Set the REPLICATE_API_TOKEN environment variable
os.environ["REPLICATE_API_TOKEN"] = "YOUR_REPLICATE_API_TOKEN"

if 'button' not in st.session_state:
    st.session_state.button = False

def button_clicked():
    st.session_state.button = True
    return st.session_state.button

def home():
    st.subheader("HOME")

    uploaded_img = st.file_uploader("Choose an Image file", type=["jpeg", "jpg", "png"])

    pref_container = st.container(border=True)

    new_image = None
    new_image2 = None
    button_pressed = False

    with pref_container:
    
        col1, col2 = st.columns(2)
        with col1:
            style = st.selectbox(
                'Choose Style',
                ('Modern', 'Vintage', 'Minimalist', 'Maximalistic', 'Professional', 'Contemprory', 'Indian', 'Japanese Zen', 'Gaming')
            )

            lighting_type =  st.selectbox(
                'Choose Lighting Type',
                ('Natural Lights', 'Dim Lights', 'Warm Lights', 'Cool Lights', 'LED Lights', 'Lamp Lights')
            )

            color = st.selectbox(
                'Choose Color',
                ('Red', 'Red-Orange', 'Red-Violet', 'Green', 'Green-Yellow', 'Blue', 'Blue-Violet', 'Blue-Green', 'Light-Blue', 'Pink', 'Magenta', 'Indigo', 'Violet', 'Purple', 'Yellow', 'Yellow-Orange', 'Yellow-Violet', 'Orange', 'Grey', 'White', 'Black')
            )           
                            
        with col2:
            room_type = st.selectbox(
                'Choose Room Type',
                ('Bed Room', 'Living Room', 'Dining Room', 'Bath Room', 'Gaming Room')
            )

            furniture =  st.selectbox(
                'Choose Furniture',
                ('Sofa Set', 'Table & Chairs', 'Recliner Chair', 'Bed Frame', 'Book-Shelf', 'Study Table')
            )

            texture = st.selectbox(
                'Choose Wall Texture',
                ('Brick', 'Granite', 'Marble', 'Wood', 'Orange Peel', 'Popcorn', 'Tile', 'Smooth')
            )
        
        button_col1, button_col2, button_col3, button_col4, button_col5 = st.columns(5)
        model = "jagilley/controlnet-hough:854e8727697a057c525cdb45ab037f64ecca770a1769cc52287c2e56472a247b"

        with button_col5:
            if uploaded_img is not None:
                st.button("Design", type="primary", use_container_width=True, on_click=button_clicked)                    
            else:
                new_image = None

    img_col1, img_col2 = st.columns(2)

    with img_col1:
        st.subheader("Uploaded Image:")
        img_container = st.container(border=True)
        if uploaded_img is not None:
            img_container.image(uploaded_img)
        else:
            img_container.image('images/no_image.jpg')
    
    with img_col2:
        st.subheader("AI Generated Output:")
        img_container2 = st.container(border=True)
        if st.session_state.button is True:
            output_image = replicate.run(
                model,
                input = {
                    "image": uploaded_img,
                    "prompt": f"A detailed {style} style {room_type}, with color as {color} and with {furniture} placed in the room with {texture} wall texture and with {lighting_type} lighting type.",
                    "a_prompt": "best quality, extremely detailed, interior, cinematic photo, ultra-detailed, ultra-realistic, award-winning, high-definition",
                    "n_prompt": "worst quality, distorted, low quality, low definition, bad qaulity, the absolute worst quality, distorted features, distorted generation"
                }
            )
            new_image = output_image[1]
            img_container2.image(new_image)
        else:
            img_container2.image('images/no_image.jpg')

def about():
    st.subheader("ABOUT")

    container = st.container(border=True)
    container.markdown("""
            <h4>Welcome to DesignDreamer, your gateway to personalized and visually stunning living spaces. Our app utilizes cutting-edge Generative AI to transform interior design into a seamless and interactive experience.</h4>
            <hr>
            <h3>How It Works?</h3>

            <h5> 1. <u>Upload & Specify</u>: Easily upload room images, specify design preferences, and room types.</h5>
            <h5> 2. <u>AI Reimagining</u>: Our advanced Generative AI processes your input, providing a tailored, visually stunning reimagining of your space.</h5>
            <h5> 3. <u>Futuristic Vision</u>: DesignDreamer represents a futuristic vision, making interior design personalized and effortless.</h5>
                       
            <hr>
            <p><h6>Join us in shaping the future of interior design. DesignDreamer – where your dream space becomes a reality with the click of a button.</h6></p>
            """, unsafe_allow_html=True
        )    

def gallery():
    st.subheader("GALLERY")
    col1, col2 = st.columns(2)
    with col1:
        container1 = st.container(border=True)
        
        with container1:
            c1c1, c1c2, c1c3 = st.columns(3)
            with c1c1:
                st.image("Input Image Samples/input2.png")
            with c1c2:
                st.image("Output Image Samples/output_1.png")
                st.markdown("""<style> .vertical-divider { border-left: 1px solid #ccc; height: 100%; } </style>""", unsafe_allow_html=True)
            with c1c3:
                st.markdown("""
                    ###### **Style** - Vintage

                    ###### **Room Type** - Bedroom

                    ###### **Color** - Red-Violet

                    ###### **Furniture** - Bed Frame

                    ###### **Wall Texture** - Smooth

                    ###### **Lighting Type** - Warm Lights
                    """, unsafe_allow_html=True)
    
        container3 = st.container(border=True)
        
        with container3:
            c3c1, c3c2, c3c3 = st.columns(3)
            with c3c1:
                st.image("Input Image Samples/input.jpg")
            with c3c2:
                st.image("Output Image Samples/output_2.png")
                st.markdown("""<style> .vertical-divider { border-left: 1px solid #ccc; height: 100%; } </style>""", unsafe_allow_html=True)
            with c3c3:
                st.markdown("""
                    ###### **Style** - Minimalist

                    ###### **Room Type** - Living Room

                    ###### **Color** - Grey

                    ###### **Furniture** - Sofa Set

                    ###### **Wall Texture** - Wood

                    ###### **Lighting Type** - LED Lights
                    """, unsafe_allow_html=True)
                
    with col2:
        container2 = st.container(border=True)
        
        with container2:
            c2c1, c2c2, c2c3 = st.columns(3)
            with c2c1:
                st.image("Input Image Samples/input2.jpeg")
            with c2c2:
                st.image("Output Image Samples/output_3.png")
                st.markdown("""<style> .vertical-divider { border-left: 1px solid #ccc; height: 100%; } </style>""", unsafe_allow_html=True)
            with c2c3:
                st.markdown("""
                    ###### **Style** - Japanese Zen

                    ###### **Room Type** - Living Room

                    ###### **Color** - Pink

                    ###### **Furniture** - Table & Chair

                    ###### **Wall Texture** - Marble

                    ###### **Lighting Type** - Dim Lights
                    """, unsafe_allow_html=True)

        container4 = st.container(border=True)        
        with container4:
            c4c1, c4c2, c4c3 = st.columns(3)
            with c4c1:
                st.image("Input Image Samples/input.png")
            with c4c2:
                st.image("Output Image Samples/output_4.png")
                st.markdown("""<style> .vertical-divider { border-left: 1px solid #ccc; height: 100%; } </style>""", unsafe_allow_html=True)
            with c4c3:
                st.markdown("""
                    ###### **Style** - Contemprory

                    ###### **Room Type** - Bed Room

                    ###### **Color** - Yellow-Orange

                    ###### **Furniture** - Bed Frame

                    ###### **Wall Texture** - Orange Peel

                    ###### **Lighting Type** - Natural Lights
                    """, unsafe_allow_html=True)
        
def contact():
    st.subheader("CONTACT")

    container = st.container()

    with container:
        col1, col2, col3 = st.columns(3)

        with col1:
            cont = st.container(border=True)
            with cont:
                st.image("images/Unknown_person.jpg")
                st.markdown('<p style="text-align: center; font-size: 24px; font-weight: bold;">Param Dhingana</p>', unsafe_allow_html=True)
                st.markdown('<p style="text-align: left; font-size: 20px;"><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/param-dhingana/" style="text-decoration: underline; color: light-blue;">@param-dhingana</a></p>', unsafe_allow_html=True)
                st.markdown('<p style="text-align: left; font-size: 20px;"><strong>GitHub:</strong> <a href="https://github.com/ParamD12" style="text-decoration: underline; color: light-blue;">@ParamD12</a></p>', unsafe_allow_html=True)
                st.markdown('<p style="text-align: left; font-size: 20px;"><strong>Mail:</strong> <a href="mailto:pdhingana@gmail.com" style="text-decoration: underline; color: light-blue;">pdhingana@gmail.com</a></p>', unsafe_allow_html=True)

        with col2:
            cont2 = st.container(border=True)
            with cont2:
                st.image("images/Unknown_person.jpg")
                st.markdown('<p style="text-align: center; font-size: 24px; font-weight: bold;">Vinamra Khandelwal</p>', unsafe_allow_html=True)
                st.markdown('<p style="text-align: left; font-size: 20px;"><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/vinamra-khandelwal-b92472246/" style="text-decoration: underline; color: light-blue;">@vinamra-khandelwal-b92472246</a></p>', unsafe_allow_html=True)
                st.markdown('<p style="text-align: left; font-size: 20px;"><strong>GitHub:</strong> <a href="https://github.com/Vinamra-Khandelwal" style="text-decoration: underline; color: light-blue;">@Vinamra-Khandelwal</a></p>', unsafe_allow_html=True)
                st.markdown('<p style="text-align: left; font-size: 20px;"><strong>Mail:</strong> <a href="mailto:vinamra1312@gmail.com" style="text-decoration: underline; color: light-blue;">vinamra1312@gmail.com</a></p>', unsafe_allow_html=True)
    
        with col3:
            cont3 = st.container(border=True)
            with cont3:
                st.image("images/Unknown_person.jpg")
                st.markdown('<p style="text-align: center; font-size: 24px; font-weight: bold;">Sudeep Ganguly</p>', unsafe_allow_html=True)
                st.markdown('<p style="text-align: left; font-size: 20px;"><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/sudeep-ganguly-a53b33205/" style="text-decoration: underline; color: light-blue;">@sudeep-ganguly-a53b33205</a></p>', unsafe_allow_html=True)
                st.markdown('<p style="text-align: left; font-size: 20px;"><strong>GitHub:</strong> <a href="https://github.com/2001sudeep" style="text-decoration: underline; color: light-blue;">@2001sudeep</a></p>', unsafe_allow_html=True)
                st.markdown('<p style="text-align: left; font-size: 20px;"><strong>Mail:</strong> <a href="mailto:Sudeep.ganguly99@gmail.com" style="text-decoration: underline; color: light-blue;">sudeep.ganguly99@gmail.com</a></p>', unsafe_allow_html=True)

def main():

    st.set_page_config(page_title="Design Dreamer", page_icon="🛋️", layout="wide")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<p style="text-align: left; font-size: 38px; font-family: Verdana; font-weight: bold;">Design Dreamer 🎨🛋️</p>', unsafe_allow_html=True)
        # st.title("Design Dreamer 🎨🛋️")

    with col2:
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Gallery", "About", "Contact"],  # required
            icons=["house", "image", "info-square", "person-rolodex"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal"
        )

    st.divider()

    if selected == "Home":
        home()
    elif selected == "Gallery":
        gallery()
    elif selected == "About":
        about()
    elif selected == "Contact":
        contact()
    else:
        home()
    
    footer_text = """

    <div style="text-align: center; font-size: 18px; font-weight: bold; background-color: #262730; padding: 10px; position: fixed; bottom: 0; left: 0; width: 100%;">
    © 2024 All Rights Reserved, Design Dreamer
    </div>

    """

    st.markdown(footer_text, unsafe_allow_html=True)

if __name__ == "__main__":
    main()