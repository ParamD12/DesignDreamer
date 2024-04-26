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

def get_color_palette(style):
    if style == "Modern":
        cp =  ["ColorPalette/Modern 1.jpg", "ColorPalette/Modern 2.jpg", "ColorPalette/Modern 3.jpg"]
        cpc = ["Modern 1", "Modern 2", "Modern 3"]
    elif style == "Vintage":
        cp = ["ColorPalette/Vintage 1.jpg", "ColorPalette/Vintage 2.jpg", "ColorPalette/Vintage 3.jpg"]
        cpc = ["Vintage 1", "Vintage 2", "Vintage 3"]
    elif style == "Minimalist":
        cp = ["ColorPalette/Minimalist 1.jpg", "ColorPalette/Minimalist 2.jpg", "ColorPalette/Minimalist 3.jpg"]
        cpc = ["Minimalist 1", "Minimalist 2", "Minimalist 3"]
    elif style == "Professional":
        cp = ["ColorPalette/Professional 1.jpg", "ColorPalette/Professional 2.jpg", "ColorPalette/Professional 3.jpg"]
        cpc = ["Professional 1", "Professional 2", "Professional 3"]
    elif style == "Contemprory":
        cp = ["ColorPalette/Contemprory 1.jpg", "ColorPalette/Contemprory 2.jpg", "ColorPalette/Contemprory 3.jpg"]
        cpc = ["Contemprory 1", "Contemprory 2", "Contemprory 3"]
    elif style == "Maximalistic":
        cp = ["ColorPalette/Maximalistic 1.jpg", "ColorPalette/Maximalistic 2.jpg", "ColorPalette/Maximalistic 3.jpg"]
        cpc = ["Maximalistic 1", "Maximalistic 2", "Maximalistic 3"]
    elif style == "Indian":
        cp = ["ColorPalette/Indian 1.jpg", "ColorPalette/Indian 2.jpg", "ColorPalette/Indian 3.jpg"]
        cpc = ["Indian 1", "Indian 2", "Indian 3"]
    elif style == "Japanese Zen":
        cp = ["ColorPalette/Japanese Zen 1.jpg", "ColorPalette/Japanese Zen 2.jpg", "ColorPalette/Japanese Zen 3.jpg"]
        cpc = ["Japanese Zen 1", "Japanese Zen 2", "Japanese Zen 3"]
    elif style == "Gaming":
        cp = ["ColorPalette/Gaming 1.jpg", "ColorPalette/Gaming 2.jpg", "ColorPalette/Gaming 3.jpg"]
        cpc = ["Gaming 1", "Gaming 2", "Gaming 3"]    
    else:
        cp = ["ColorPalette/Modern 1.jpg", "ColorPalette/Modern 2.jpg", "ColorPalette/Modern 3.jpg"]
        cpc = ["Modern 1", "Modern 2", "Modern 3"]

    return cp, cpc

def get_colors(selected_palette):
    if selected_palette == "Modern 1":
        colors = ['Soapstone', 'Laurel', 'Russian Green', 'Envy']
        hex_codes = ['#E9E3D7', '#6B946C', '#6D8C6C', '#86A48C']
    elif selected_palette == "Modern 2":
        colors = ['Porsche', 'Provincial Pink', 'Shilo', 'Champagne']
        hex_codes = ['#E19061', '#F4E1D0', '#E4AFA1', '#ECD7B8']
    elif selected_palette == "Modern 3":
        colors = ['Wild Sand', 'Turkish Rose', 'Persian Red', 'Dark Salmon']
        hex_codes = ['#E9E5E4', '#AD797D', '#C92D2E', '#EC8C7C']
    elif selected_palette == "Vintage 1":
        colors = ['Desert Storm', 'Granite Green', 'Bronco', 'Pale Oyster']
        hex_codes = ['#ECE8DD', '#8C7D60', '#AE9C84', '#9C9078']
    elif selected_palette == "Vintage 2":
        colors = ['Grey', 'White Smoke', 'Jon', 'Heavy Metal']
        hex_codes = ['#7B7B7B', '#ECECEC', '#443B3C', '#44443C']
    elif selected_palette == "Vintage 3":
        colors = ['White Smoke', 'Grey Suit', 'Mamba', 'Grey']
        hex_codes = ['#F2F2F2', '#988EA7', '#7D6D8A', '#7C7C7C']
    elif selected_palette == "Minimalist 1":
        colors = ['Light Grey', 'Suva Grey', 'Grey', 'Dim Gray']
        hex_codes = ['#D7D7D7', '#8C8C8C', '#848484', '#6C6C6C']
    elif selected_palette == "Minimalist 2":
        colors = ['Cloud', 'Dune', 'Ironside Grey', 'Makara']
        hex_codes = ['#C7BFB4', '#535250', '#70716C', '#615D52']
    elif selected_palette == "Minimalist 3":
        colors = ['Cashmere', 'Sand Dune', 'Camelot', 'Tobacco Brown']
        hex_codes = ['#CFB294', '#807063', '#7A3844', '#765C43']
    elif selected_palette == "Professional 1":
        colors = ['Sandrift', 'Black Squeeze', 'Saddle', 'Masala']
        hex_codes = ['#B39C7A', '#F3F3F1', '#5B4C47', '#5C534C']
    elif selected_palette == "Professional 2":
        colors = ['Sapphire', 'Bombay', 'Curious Blue', 'Gamboge']
        hex_codes = ['#0B3C5C', '#ABAAA8', '#338CC4', '#DB8315']
    elif selected_palette == "Professional 3":
        colors = ['Paris White', 'Scarlet', 'Grey', 'Empress']
        hex_codes = ['#C0C7BF', '#E82B05', '#7C7C7C', '#747474']
    elif selected_palette == "Contemprory 1":
        colors = ['Snow Drift', 'Cloudy', 'Heathered Grey', 'Suva Grey']
        hex_codes = ['#E5E4E0', '#B0A9A1', '#908C83', '#8C8384']
    elif selected_palette == "Contemprory 2":
        colors = ['Quill Grey', 'Matterhorn', 'Scorpion', 'Makara']
        hex_codes = ['#C6C6C4', '#504B48', '#6B6768', '#6C614F']
    elif selected_palette == "Contemprory 3":
        colors = ['Dawn Pink', 'Sea Buckthorn', 'Cascade', 'Rose Taupe']
        hex_codes = ['#E4D7CE', '#F09657', '#8BA69D', '#895C56']
    elif selected_palette == "Maximalistic 1":
        colors = ['Tumbleweed', 'Sepia', 'Bali Hai', 'Mantle']
        hex_codes = ['#D8A570', '#9B6247', '#8291A4', '#A1B2A0']
    elif selected_palette == "Maximalistic 2":
        colors = ['Petite Orchid', 'Granite Green', 'Monte Carlo', 'Pelorous']
        hex_codes = ['#DDA49D', '#948669', '#7EBDB5', '#3294C1']
    elif selected_palette == "Maximalistic 3":
        colors = ['Rose', 'Ochre', 'Half Colonial White', 'Stromboli']
        hex_codes = ['#D09897', '#C56E27', '#F2E3C6', '#456E5E']
    elif selected_palette == "Indian 1":
        colors = ['Black Squeeze', 'Hot Toddy', 'Winter Hazel', 'Shingle Fawn']
        hex_codes = ['#F3F4EF', '#A6872C', '#D3BE85', '#6C5533']
    elif selected_palette == "Indian 2":
        colors = ['Pumpkin', 'Concrete', 'Burnt Orange', 'Waikawa Grey']
        hex_codes = ['#F46B23', '#D7D7D5', '#F5743B', '#5C6493']
    elif selected_palette == "Indian 3":
        colors = ['Whisper', 'Dolly', 'Free Speech Magenta', 'Polo Blue']
        hex_codes = ['#F4EBEC', '#F3E06A', '#E166B6', '#96B4D6']
    elif selected_palette == "Japanese Zen 1":
        colors = ['Soya Bean', 'Desert Storm', 'Tasman', 'Cerulean Blue']
        hex_codes = ['#78624B', '#EFECE5', '#B5BDAE', '#A9ACA5']
    elif selected_palette == "Japanese Zen 2":
        colors = ['Whisper', 'Brandy Rose', 'Brink Pink', 'Suva Grey']
        hex_codes = ['#F2EEED', '#B67C7B', '#FB7083', '#949494']
    elif selected_palette == "Japanese Zen 3":
        colors = ['Prim', 'Mountbatten Pink', 'Casper', 'Logan']
        hex_codes = ['#DDCED5', '#9B7989', '#ACB5BA', '#A29AAF']
    elif selected_palette == "Gaming 1":
        colors = ['Porcelain', 'Bay Leaf', 'Mantis', 'Chicago']
        hex_codes = ['#DBDBD9', '#6EB589', '#96B857', '#60615C']
    elif selected_palette == "Gaming 2":
        colors = ['Black White', 'Flamingo', 'Emerald', 'Olivine']
        hex_codes = ['#E4E4D8', '#DE5245', '#4EC08F', '#94B27C']
    elif selected_palette == "Gaming 3":
        colors = ['Perano', 'Slate Blue', 'Topaz', 'Suva Grey']
        hex_codes = ['#CCA2EE', '#804BCF', '#81718C', '#949494']    
    else:
        colors = ['Soapstone', 'Laurel', 'Russian Green', 'Envy']
        hex_codes = ['#E9E3D7', '#6B946C', '#6D8C6C', '#86A48C']

    return colors, hex_codes

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
                            
        with col2:
            room_type = st.selectbox(
                'Choose Room Type',
                ('Bedroom', 'Living Room', 'Dining Room', 'Bathroom', 'Gaming Room')
            )

            furniture =  st.selectbox(
                'Choose Furniture',
                ('Sofa Set', 'Table & Chairs', 'Recliner Chair', 'Bed Frame', 'Book-Shelf', 'Study Table')
            )

        cp, cpc = get_color_palette(style)
        color_palette = image_select(label = "Select Color Palette", 
                                    images = cp,
                                    captions = cpc,
                                    use_container_width = False)

        cpf = Path(color_palette).name
        cpn = os.path.splitext(cpf)[0]
        color1, color2, color3, color4 = get_colors(cpn)[0]
        hex_code1, hex_code2, hex_code3, hex_code4 = get_colors(cpn)[1]
        st.write(f"Colors in Color Palette: {color1}, {color2}, {color3}, {color4}")
        st.write(f"Colors[Hex-Codes] in Color  Palette: {hex_code1}, {hex_code2}, {hex_code3}, {hex_code4}")
        
        texture = ['WallTexture/Brick.jpg',
                   'WallTexture/Granite.jpg',
                   'WallTexture/Marble.jpg',
                   'WallTexture/Wood.jpg',
                   'WallTexture/OrangePeel.jpg',
                   'WallTexture/Popcorn.jpg',
                   'WallTexture/Tile.jpg',
                   'WallTexture/Smooth.jpg']
        
        wall_texture = image_select(
            label="Select Wall Texture",
            images = texture,
            captions = ['Brick', 'Granite', 'Marble', 'Wood', 'Orange Peel', 'Popcorn', 'Tile', 'Smooth'],
            use_container_width = True
        )
        walltf = Path(wall_texture).name
        walltn = os.path.splitext(walltf)[0]

        button_col1, button_col2, button_col3, button_col4, button_col5 = st.columns(5)
        model = "jagilley/controlnet-hough:854e8727697a057c525cdb45ab037f64ecca770a1769cc52287c2e56472a247b"

        with button_col5:
            if uploaded_img is not None:
                st.button("Design", type="primary", use_container_width=True, on_click=button_clicked)                    
            else:
                new_image = None

    img_col1, img_col2 = st.columns(2)

    with img_col1:
        st.header("Uploaded Image:")
        img_container = st.container(border=True)
        if uploaded_img is not None:
            img_container.image(uploaded_img)
        else:
            img_container.image('images/no_image.jpg')
    
    with img_col2:
        st.header("AI Generated Output:")
        img_container2 = st.container(border=True)
        if st.session_state.button is True:
            output_image = replicate.run(
                model,
                input = {
                    "image": uploaded_img,
                    "prompt": f"A detailed multi colored {style} {room_type}, with wall color as {color1}, and other colors inlcuding {color2}, {color3}, {color4}, with {furniture} placed in the room with {walltn} wall texture and with {lighting_type} lighting type.",
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
                st.image("Output Image Samples/output.png")
                st.markdown("""<style> .vertical-divider { border-left: 1px solid #ccc; height: 100%; } </style>""", unsafe_allow_html=True)
            with c1c3:
                st.markdown("""
                    ###### **Style** - Vintage

                    ###### **Room Type** - Bedroom

                    ###### **Color Palette** - Vintage 2

                    ###### **Furniture** - Bed Frame

                    ###### **Wall Texture** - Smooth

                    ###### **Lighting Type** - Warm
                    """, unsafe_allow_html=True)
    
        container3 = st.container(border=True)
        
        with container3:
            c3c1, c3c2, c3c3 = st.columns(3)
            with c3c1:
                st.image("Input Image Samples/input.jpg")
            with c3c2:
                st.image("Output Image Samples/output2.png")
                st.markdown("""<style> .vertical-divider { border-left: 1px solid #ccc; height: 100%; } </style>""", unsafe_allow_html=True)
            with c3c3:
                st.markdown("""
                    ###### **Style** - Minimalist

                    ###### **Room Type** - Living Room

                    ###### **Color Palette** - Minimalist 3

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
                st.image("Output Image Samples/output3.png")
                st.markdown("""<style> .vertical-divider { border-left: 1px solid #ccc; height: 100%; } </style>""", unsafe_allow_html=True)
            with c2c3:
                st.markdown("""
                    ###### **Style** - Professional

                    ###### **Room Type** - Living Room

                    ###### **Color Palette** - Professional 1

                    ###### **Furniture** - Recliner Chair

                    ###### **Wall Texture** - Marble

                    ###### **Lighting Type** - Cool
                    """, unsafe_allow_html=True)

        container4 = st.container(border=True)        
        with container4:
            c4c1, c4c2, c4c3 = st.columns(3)
            with c4c1:
                st.image("Input Image Samples/input.png")
            with c4c2:
                st.image("Output Image Samples/output4.png")
                st.markdown("""<style> .vertical-divider { border-left: 1px solid #ccc; height: 100%; } </style>""", unsafe_allow_html=True)
            with c4c3:
                st.markdown("""
                    ###### **Style** - Contemprory

                    ###### **Room Type** - Bed Room

                    ###### **Color Palette** - Contemprory 3

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