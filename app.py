from transformers import AutoModel, AutoTokenizer
import streamlit as st
from PIL import Image
import tempfile



def perform_ocr(image):
    tokenizer = AutoTokenizer.from_pretrained('srimanth-d/GOT_CPU', trust_remote_code=True)
    model = AutoModel.from_pretrained('srimanth-d/GOT_CPU', trust_remote_code=True, low_cpu_mem_usage=True, use_safetensors=True, pad_token_id=tokenizer.eos_token_id)
    model = model.eval()
    res = model.chat(tokenizer, image, ocr_type='ocr')
    return res


# Title and instructions
st.title(' OCR and Document Search Web Application Prototype')
st.write('Upload an image and extract text in Hindi and English. You can also search for keywords within the extracted text.')

# Upload the image
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])

# If an image is uploaded
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        temp_file_path = temp_file.name

    # Perform OCR on the uploaded image
    st.write("Extracting text...")
    extracted_text = perform_ocr(temp_file_path)
    st.write("Extracted Text:")
    st.text_area("OCR Output", extracted_text, height=200)