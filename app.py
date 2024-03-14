import streamlit as st
import os
import replicate
import base64
import requests

#Set the REPLICATE_API_TOKEN environment variable
os.environ["REPLICATE_API_TOKEN"] = "r8_T6DZZrt40fWjdtOxtrYyOp74T8eXS9f47r1ng"

def get_color_palette(style):
    if style == "Modern":
        return ["ColorPalette/Modern 1.jpg", "ColorPalette/Modern 2.jpg", "ColorPalette/Modern 3.jpg"]
    elif style == "Vintage":
        return ["ColorPalette/Vintage 1.jpg", "ColorPalette/Vintage 2.jpg", "ColorPalette/Vintage 3.jpg"]
    elif style == "Minimalist":
        return ["ColorPalette/Minimalist 1.jpg", "ColorPalette/Minimalist 2.jpg", "ColorPalette/Minimalist 3.jpg"]
    elif style == "Professional":
        return ["ColorPalette/Professional 1.jpg", "ColorPalette/Professional 2.jpg", "ColorPalette/Professional 3.jpg"]
    elif style == "Contemprory":
        return ["ColorPalette/Contemprory 1.jpg", "ColorPalette/Contemprory 2.jpg", "ColorPalette/Contemprory 3.jpg"]
    elif style == "Maximalistic":
        return ["ColorPalette/Maximalistic 1.jpg", "ColorPalette/Maximalistic 2.jpg", "ColorPalette/Maximalistic 3.jpg"]
    else:
        return ["ColorPalette/Modern 1.jpg", "ColorPalette/Modern 2.jpg", "ColorPalette/Modern 3.jpg"]

def get_color_palette_name(style):
    if style == "Modern":
        return ["Modern 1", "Modern 2", "Modern 3"]
    elif style == "Vintage":
        return ["Vintage 1", "Vintage 2", "Vintage 3"]
    elif style == "Minimalist":
        return ["Minimalist 1", "Minimalist 2", "Minimalist 3"]
    elif style == "Professional":
        return ["Professional 1", "Professional 2", "Professional 3"]
    elif style == "Contemprory":
        return ["Contemprory 1", "Contemprory 2", "Contemprory 3"]
    elif style == "Maximalistic":
        return ["Maximalistic 1", "Maximalistic 2", "Maximalistic 3"]
    else:
        return ["Modern 1", "Modern 2", "Modern 3"]

def texture_image(texture):
    if texture == "Brick":
        return "WallTexture/Brick.jpg"
    elif texture == "Marble":
        return "WallTexture/Marble.jpg"
    elif texture == "Granite":
        return "WallTexture/Granite.jpg"
    elif texture == "Orange Peel":
        return "WallTexture/OrangePeel.jpg"
    elif texture == "Popcorn":
        return "WallTexture/Popcorn.jpg"
    elif texture == "Tile":
        return "WallTexture/Tile.jpg"
    else:
        return "WallTexture/Bick.jpg"

def generate_image(uploaded_image, style, room_type):
    model = "jagilley/controlnet-hough:854e8727697a057c525cdb45ab037f64ecca770a1769cc52287c2e56472a247b"
    output_image = replicate.run(
        model,
        input = {
            "image": uploaded_image,
            "prompt": f"A detailed {style} design, for a {room_type}.",
            "a_prompt": "best quality, extremely detailed, , interior, cinematic photo, ultra-detailed, ultra-realistic, award-winning"
        }
    )
    return output_image[1]

def download_output(new_image):
    try:
        # Send a GET request to the URL
        response = requests.get(new_image)
        current_directory = os.path.dirname(os.path.realpath(__file__))
        save_path = os.path.join(current_directory, "output" + '.png')
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Open the file in binary write mode and write the image content to it
            with open(save_path, 'wb') as f:
                f.write(response.content)
            res = "Image downloaded successfully and saved as '{save_path}'"
            return res
        else:
            res = "Failed to download image from '{new_image}'. Status code: {response.status_code}"
            return res
    except Exception as e:
        res = "An error occurred: {str(e)}"
        return res

def main():

    st.set_page_config(page_title="Design Dreamer", page_icon="🛋️", layout="wide")

    st.title("Design Dreamer: Design your dream space with state-of-the-art Generative AI 🛋️🎨")
    st.image("DesignDreamer.png")

    tab1, tab2 = st.tabs(["Design Dreamer", "About the App"])
    
    with tab1:
        uploaded_img = st.file_uploader("Choose an Image file", type=["jpeg", "jpg", "png"])

        pref_container = st.container(border=True)

        col1, col2, col3 = pref_container.columns(3)

        with col1:
            style = st.selectbox(
                'Choose Style',
                ('Modern', 'Vintage', 'Minimalist', 'Professional', 'Contemprory', 'Maximalistic', 'Indian', 'Japanese Zen', 'Gaming')
            )            
                        
        with col2:
            room_type = st.selectbox(
                'Choose Room Type',
                ('Bedroom', 'Living Room', 'Dining Room', 'Bathroom')
            )   

        with col3:
           lighting_type = st.selectbox(
                'Choose Lighting Type',
                ('Natural Lights', 'Dim Lights', 'Warm Lights', 'Cool Lights', 'LED Lights', 'Lamp Lights')
            ) 
        
        image_paths = get_color_palette(style)
        
        with pref_container.expander("See Color Palette Preview"):

            cp_img1, cp_img2, cp_img3 = st.columns(3)

            with cp_img1:
                st.image(image_paths[0], use_column_width=True)

            with cp_img2:
                st.image(image_paths[1], use_column_width=True)

            with cp_img3:
                st.image(image_paths[2], use_column_width=True)

        color_palette_name = get_color_palette_name(style)

        selected_color_palette = pref_container.selectbox("Choose Color Palette", color_palette_name)

        wall_texture = ["Brick", "Wood", "Smooth", "Tile", "Popcorn", "Orange Peel", "Granite", "Marble"]

        selected_wall_texture = pref_container.selectbox("Choose Wall Texture", wall_texture)

        wall_texture_image = texture_image(selected_wall_texture)

        with pref_container.expander("See Texture Preview"):
            st.image(wall_texture_image)

        button_col1, button_col2, button_col3, button_col4 = pref_container.columns(4)

        global new_image
    
        with button_col4:
            if st.button("Design", type="primary", use_container_width=True):
                if uploaded_img is not None:
                    new_image = generate_image(uploaded_img, style, room_type)

            else:
                new_image = None
                  
        img_col1, img_col2 = st.columns(2)

        with img_col1:
            st.header("Uploaded Image:")
            img_container = st.container(border=True)
            if uploaded_img is not None:
                img_container.image(uploaded_img)
            else:
                img_container.image('no_image.jpg')

        with img_col2:
            st.header("AI Generated Output:")
            img_container2 = st.container(border=True)
            if new_image is not None:
                img_container2.image(new_image)
            else:
                img_container2.image('no_image.jpg')

        d_button_col1, d_button_col2, d_button_col3, d_button_col4, d_button_col5 = st.columns(5)

        with d_button_col5:
            if st.button(":arrow_double_down: Download Image", use_container_width = True):
                if new_image is not None:
                    res = download_output(new_image)
                    st.info(res)
                else:
                    st.error("Please Try Again!")
                        
                
    with tab2:
        container2 = st.container(border=True)
        container2.markdown("""
            <h4>About DesignDreamer</h4>                

            Welcome to DesignDreamer, your gateway to personalized and visually stunning living spaces. Our app utilizes cutting-edge Generative AI to transform interior design into a seamless and interactive experience.

            <h4>How It Works?</h4>

            1. **Upload & Specify**: Easily upload room images, specify design preferences, and room types.
            2. **AI Reimagining**: Our advanced Generative AI processes your input, providing a tailored, visually stunning reimagining of your space.
            3. **Futuristic Vision**: DesignDreamer represents a futuristic vision, making interior design personalized and effortless.

            Join us in shaping the future of interior design. DesignDreamer – where your dream space becomes a reality with the click of a button.
            """, unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()