# Design Dreamer

DesignDreamer represents a futuristic vision in the realm of Generative AI, harnessing advanced technologies to elevate interior design into a personalized and visually stunning experience. This project delves into the intricate fusion of user-uploaded room images, cutting-edge image generation and recreation models, and design preferences to create tailored and aesthetically pleasing spaces. 

By seamlessly integrating style preferences and room types, DesignDreamer empowers users to effortlessly visualize and co-create their dream environments.

This README will guide you through the setup and usage of the Design Dreamer: AI Interior Designer.

## Table of Contents

- [Introduction](#design-dreamer)
- [Table of Contents](#table-of-contents)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [License](#license)

## Prerequisites

Before you can start using the Design Dreamer: AI Interior Designer, make sure you have the following prerequisites installed on your system:

- Python 3.6 or higher
- Replicate API
- Required Python packages (you can install them using pip):
  -  streamlit
  - streamlit_option_menu 
  - os
  - replicate
  - requests
  - streamlit_image_select
  - htbuilder
  - pathlib

## Installation

1. Clone this repository to your local machine.

    ```bash
    git clone https://github.com/ParamD12/DesignDreamer.git
    cd DesignDreamer
    ```

2. Create a Python virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Make sure to have your Replicate API key ready.

## Getting Started

To get started with Design Dreamer, you need to:

1. Set up your environment and install the required packages as described in the Installation section.

2. Set the Replicate API Token value in the code given below.

```python
REPLICATE_API_KEY = "your-replicate-api-key"
```

3. Start the Design Dreamer: AI Interior Designer by running the provided Python script or by running the command given below.

```bash
streamlit run app.py #or
streamlit run main.py
```

## Usage

The Design Dreamer can be used for designing your living spaces. To use the application, you can follow these steps:

1. Start the application by running the given command or using the provided Python script.

2. Upload a picture of the room to be designed.

3. Choose a variety of Design Preferences for your room.

4. The application then takes the input parameters and comes up with a unique design everytime you run the application.

## Technologies Used

1. **Python**: Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. It supports multiple programming paradigms, including structured, object-oriented and functional programming.

2. **Streamlit**: Streamlit is an open-source Python GUI framework for machine learning and data science teams.

3. **Replicate**: Replicate is a scalable deployment tool facilitating the integration of custom AI models into a production environment through API calls. Users can also fine tune open source models, and deploy custom models at scale.

4. **Controlnet-Hough**: This model is ControlNet adapting Stable Diffusion to use M-LSD detected edges in an input image in addition to a text input to generate an output image. The training data is generated using a learning-based deep Hough transform to detect straight lines from Places2 and then use BLIP to generate captions.

## License

This project is licensed under the MIT License.

---

For more information on how to use, configure, and extend the Design Dreamer: AI Interior Designer, please refer to the documentation or contact the project maintainers.
