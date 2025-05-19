import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Simulate Gemini API key (not actually used here due to API key limit)
GEMINI_API_KEY = "AIzA-SAMPLE-RANDOM-KEY-123456"

# Config
st.set_page_config(page_title="TripMate - Smart Travel Planner", layout="centered")
st.title("🌴 TripMate: Plan Your Dream Trip with AI")

# Load model
MODEL_NAME = "google/flan-t5-small"  # lighter and faster
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
    return pipe

generator = load_model()

# Form input
with st.form("trip_form"):
    st.subheader("✈️ Tell us about your trip")
    destination = st.text_input("Where are you going?", value="Galle")
    days = st.number_input("Number of days", min_value=1, max_value=30, value=5)
    interests = st.multiselect("What are you interested in?", ["Culture", "Adventure", "Relaxation", "Nature", "Food", "History", "Nightlife"], default=["Relaxation", "Nature"])
    budget = st.selectbox("Budget", ["Economy", "Mid-range", "Luxury"])
    season = st.selectbox("Preferred Season", ["Spring", "Summer", "Autumn", "Winter"])
    submit = st.form_submit_button("🗺️ Generate Itinerary")

# Generate itinerary
if submit:
    with st.spinner("Planning your trip..."):
        interest_text = ", ".join(interests) if interests else "general tourism"
        prompt = (
            f"Create a detailed {days}-day travel itinerary to {destination} for someone interested in {interest_text}. "
            f"The budget is {budget} and the preferred season is {season}. "
            f"Include places to visit, activities, and food ideas. Format clearly day-by-day."
        )

        result = generator(prompt, max_new_tokens=512)[0]["generated_text"]

        st.success("Here's your AI-generated itinerary! Feel free to edit it as needed.")
        edited_text = st.text_area("✍️ Editable Itinerary", value=result, height=400)

        st.download_button(
            label="📥 Download Itinerary",
            data=edited_text,
            file_name=f"{destination.lower()}_itinerary.txt",
            mime="text/plain"
        )

st.markdown("---")
st.caption("🚀 Built with 🤗 Hugging Face Transformers and ❤️ Streamlit by Githmi Punchihewa")
