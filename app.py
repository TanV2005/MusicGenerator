# import streamlit as st
# import os
# from preprocess import extract_notes
# from utils import prepare_sequences
# from train import create_model, train_model
# from generate import generate_notes, create_midi
# from prompt_engine import apply_prompt_settings

# st.title("🎵 AI Music Generator")

# prompt = st.text_input("Enter mood (happy/sad/energetic/calm):")
# length = st.slider("Music Length", 100, 500, 200)

# if st.button("Generate Music"):
#     notes = extract_notes("dataset/midi_files")
    
#     X, y, note_to_int, int_to_note, pitchnames = prepare_sequences(notes)

#     model = create_model((X.shape[1], X.shape[2]), len(pitchnames))
#     model = train_model(model, X, y, epochs=20)

#     settings = apply_prompt_settings(prompt)

#     output_notes = generate_notes(model, X, int_to_note, settings["temperature"])

#     if not os.path.exists("output"):
#         os.makedirs("output")

#     create_midi(output_notes)

#     st.success("Music Generated 🎉")
#     st.audio("output/output.mid")



# import streamlit as st
# from tensorflow.keras.models import load_model
# from preprocess import get_notes
# from utils import prepare_sequences
# from generate import generate_notes, create_midi

# st.title("🎵 AI Music Generator")

# if st.button("Generate Music"):
#     st.write("Generating music...")

#     # Load model
#     model = load_model("models/model.h5")

#     # Load notes
#     notes = get_notes("dataset/midi_files")

#     # Prepare sequences
#     network_input, _, note_to_int, int_to_note, pitchnames = prepare_sequences(notes, 50)

#     # Generate music
#     prediction_output = generate_notes(model, network_input, int_to_note)

#     # Save MIDI
#     create_midi(prediction_output)

#     st.success("Music Generated 🎵")
#     st.audio("output/output.mid")


# ------------chane no 1----------------------------------------------------------------


# import streamlit as st
# from tensorflow.keras.models import load_model
# from preprocess import get_notes
# from utils import prepare_sequences
# # from generate import generate_notes, create_audio
# from generate import generate_music # new function that uses pretrained model for faster generation---as per--change no 6--

# st.set_page_config(page_title="AI Music Generator", layout="centered")

# st.title("🎵 AI Text-to-Music Generator")

# # LOAD MODEL ONLY ONCE
# @st.cache_resource
# def load_my_model():
#     return load_model("models/model.h5")

# model = load_my_model()

# # LOAD DATA ONLY ONCE
# @st.cache_data
# def load_data():
#     notes = get_notes("dataset/midi_files")
#     network_input, _, note_to_int, int_to_note, pitchnames = prepare_sequences(notes, 50)
#     return network_input, int_to_note

# network_input, int_to_note = load_data()

# # PROMPT INPUT
# prompt = st.text_input("Enter prompt (e.g., energetic dance music)")

# # TEMPERATURE LOGIC
# # def get_temperature(prompt):
# #     prompt = prompt.lower()

# #     if "happy" in prompt:
# #         return 0.9
# #     elif "sad" in prompt:
# #         return 0.5
# #     elif "energetic" in prompt or "dance" in prompt:
# #         return 1.1
# #     elif "calm" in prompt:
# #         return 0.6
# #     else:
# #         return 0.8
    
# # def get_params(prompt):
# #     prompt = prompt.lower()

# #     # default
# #     temp = 0.8
# #     duration = 0.4

# #     if "happy" in prompt:
# #         temp = 0.9
# #         duration = 0.3

# #     elif "sad" in prompt:
# #         temp = 0.5
# #         duration = 0.6

# #     elif "energetic" in prompt or "dance" in prompt:
# #         temp = 1.2
# #         duration = 0.2

# #     elif "calm" in prompt or "relax" in prompt:
# #         temp = 0.6
# #         duration = 0.7

# #     return temp, duration  

# # 🎯 PROMPT CONTROL FUNCTION
# def get_params(prompt):
#     prompt = prompt.lower()

#     # default
#     temp = 0.8
#     duration = 0.4
#     pitch_range = (40, 90)

#     if "happy" in prompt:
#         temp = 0.9
#         duration = 0.3
#         pitch_range = (60, 100)

#     elif "sad" in prompt:
#         temp = 0.5
#         duration = 0.6
#         pitch_range = (40, 70)

#     elif "energetic" in prompt or "dance" in prompt:
#         temp = 1.2
#         duration = 0.2
#         pitch_range = (70, 110)

#     elif "calm" in prompt or "relax" in prompt:
#         temp = 0.6
#         duration = 0.7
#         pitch_range = (50, 75)

#     return temp, duration, pitch_range  

# # BUTTON
# # if st.button("Generate Music"):
# #     if prompt.strip() == "":
# #         st.warning("Please enter a prompt!")
# #     else:
# #         # temperature = get_temperature(prompt)
# #         temperature, note_duration = get_params(prompt)

# #         with st.spinner("Generating music... 🎵"):
# #             prediction_output = generate_notes(
# #                 model, network_input, int_to_note, temperature
# #             )
# #             audio_path = create_audio(prediction_output)

# #         st.success("Music Generated 🎶")
# #         # st.audio(audio_path)
# #         st.audio(audio_path, format="audio/wav")

# if st.button("Generate Music"):
#     if prompt.strip() == "":
#         st.warning("Please enter a prompt!")
#     else:
#         temp, duration, pitch_range = get_params(prompt)

#         # with st.spinner("Generating music... 🎵"):
#         #     prediction_output = generate_notes(
#         #         model,
#         #         network_input,
#         #         int_to_note,
#         #         temp,
#         #         pitch_range
#         #     )

#         #     audio_path = create_audio(prediction_output, duration)

#         # using pretrained model for much faster generation and better quality--as per----change no 6----
#         with st.spinner("Generating music with pretrained model... 🎵"):    
#             audio_path = generate_music(prompt)

#         st.success("Music Generated 🎶")
#         st.audio(audio_path, format="audio/wav")        





# -----------------------change no 2----------------------------------------------------------------

# import streamlit as st
# from generate import generate_music

# st.set_page_config(page_title="AI Music Generator", layout="centered")

# st.title("🎵 AI Text-to-Music Generator (MusicGen)")

# # PROMPT INPUT
# prompt = st.text_input("Enter prompt (e.g., energetic dance music)")

# # BUTTON
# if st.button("Generate Music"):
#     if prompt.strip() == "":
#         st.warning("Please enter a prompt!")
#     else:
#         with st.spinner("Generating music... 🎵"):
#             audio_path = generate_music(prompt)

#         st.success("Music Generated 🎶")
#         st.audio(audio_path, format="audio/wav")

# ----------change no 3----------------------------------------------------------------
# adding more features





# import streamlit as st
# from generate import generate_musicgen, generate_lstm, create_audio_lstm
# from tensorflow.keras.models import load_model
# from preprocess import get_notes
# from utils import prepare_sequences

# st.set_page_config(page_title="AI Music Generator", layout="centered")

# st.title("🎵 AI Music Generator (Premium Version)")

# # ================= LOAD LSTM ================= #

# @st.cache_resource
# def load_lstm_model():
#     return load_model("models/model.h5")

# @st.cache_data
# def load_data():
#     notes = get_notes("dataset/midi_files")
#     network_input, _, note_to_int, int_to_note, _ = prepare_sequences(notes, 50)
#     return network_input, int_to_note

# lstm_model = load_lstm_model()
# network_input, int_to_note = load_data()

# # ================= UI ================= #

# prompt = st.text_input("Enter your music prompt")

# # 🎛️ Style Presets
# style = st.selectbox(
#     "Select Style",
#     ["None", "Lo-fi", "Jazz", "EDM", "Classical"]
# )

# # 🎵 Duration Control
# duration = st.radio(
#     "Select Duration",
#     ["Short", "Medium", "Long"]
# )

# # 🔄 Model Selection
# model_choice = st.radio(
#     "Select Model",
#     ["MusicGen (AI)", "LSTM (Old Model)"]
# )

# # ================= STYLE PROMPT ENHANCEMENT ================= #

# def apply_style(prompt, style):
#     if style == "Lo-fi":
#         return prompt + " lofi chill beats"
#     elif style == "Jazz":
#         return prompt + " smooth jazz music"
#     elif style == "EDM":
#         return prompt + " electronic dance music"
#     elif style == "Classical":
#         return prompt + " classical orchestral music"
#     return prompt

# # ================= GENERATE ================= #

# if st.button("Generate Music"):
#     if prompt.strip() == "":
#         st.warning("Please enter a prompt!")
#     else:
#         final_prompt = apply_style(prompt, style)

#         progress = st.progress(0)

#         with st.spinner("Generating music... 🎵"):

#             progress.progress(20)

#             if model_choice == "MusicGen (AI)":
#                 audio_path = generate_musicgen(final_prompt, duration)

#             else:
#                 notes = generate_lstm(lstm_model, network_input, int_to_note)
#                 audio_path = create_audio_lstm(notes)

#             progress.progress(100)

#         st.success("Music Generated 🎶")

#         st.audio(audio_path)

#         # 🎧 Download Button
#         with open(audio_path, "rb") as f:
#             st.download_button(
#                 label="Download Music",
#                 data=f,
#                 file_name="generated_music.wav",
#                 mime="audio/wav"
#             )


# -------------------------change no 4----------------------------------------------------------------
# adding download button for generated music--as per---google colab--


# import streamlit as st
# import requests

# st.set_page_config(page_title="AI Music Generator", layout="centered")

# st.title("🎵 AI Music Generator (GPU Powered 🚀)")

# # ================= INPUT ================= #

# prompt = st.text_input("Enter your music prompt")

# # 🎨 Style presets
# style = st.selectbox(
#     "Select Style",
#     ["None", "Lo-fi", "Jazz", "EDM", "Classical"]
# )

# # 🎵 Duration
# duration = st.radio(
#     "Select Duration",
#     ["Short", "Medium", "Long"]
# )

# # ================= STYLE LOGIC ================= #

# def apply_style(prompt, style):
#     if style == "Lo-fi":
#         return prompt + " lofi chill beats"
#     elif style == "Jazz":
#         return prompt + " smooth jazz music"
#     elif style == "EDM":
#         return prompt + " electronic dance music"
#     elif style == "Classical":
#         return prompt + " classical orchestral music"
#     return prompt

# # ================= GENERATE ================= #

# if st.button("Generate Music"):
#     if prompt.strip() == "":
#         st.warning("Please enter a prompt!")
#     else:
#         final_prompt = apply_style(prompt, style)

#         progress = st.progress(0)

#         with st.spinner("Generating music on GPU... 🎵"):

#             progress.progress(20)

#             # 🔥 YOUR NGROK URL HERE
#             API_URL = "https://cardinal-congrats-peroxide.ngrok-free.dev/generate"

#             response = requests.post(
#                 API_URL,
#                 json={
#                     "text": final_prompt,
#                     "duration": duration
#                 }
#             )

#             progress.progress(70)

#             # Save audio
#             with open("output.wav", "wb") as f:
#                 f.write(response.content)

#             progress.progress(100)

#         st.success("Music Generated 🎶")

#         st.audio("output.wav")

#         # 🎧 Download button
#         with open("output.wav", "rb") as f:
#             st.download_button(
#                 label="Download Music",
#                 data=f,
#                 file_name="generated_music.wav",
#                 mime="audio/wav"
#             )

# -------------------------change no 5----------------------------------------------------------------

import streamlit as st
from generate import generate_musicgen, generate_lstm, create_audio_lstm, load_musicgen
from tensorflow.keras.models import load_model
from preprocess import get_notes
from utils import prepare_sequences

st.set_page_config(page_title="AI Music Generator", layout="centered")

st.title("🎵 AI Music Generator (Premium Version)")

# ================= PRELOAD MUSICGEN ================= #

@st.cache_resource
def preload_musicgen():
    return load_musicgen()

with st.spinner("Loading MusicGen AI Model... First time only"):
    preload_musicgen()

# ================= LOAD LSTM ================= #

@st.cache_resource
def load_lstm_model():
    return load_model("models/model.h5")

@st.cache_data
def load_data():
    notes = get_notes("dataset/midi_files")
    network_input, _, note_to_int, int_to_note, _ = prepare_sequences(notes, 50)
    return network_input, int_to_note

lstm_model = load_lstm_model()
network_input, int_to_note = load_data()

# ================= UI ================= #

prompt = st.text_input("Enter your music prompt")

style = st.selectbox(
    "Select Style",
    ["None", "Lo-fi", "Jazz", "EDM", "Classical"]
)

duration = st.radio(
    "Select Duration",
    ["Short", "Medium", "Long"]
)

model_choice = st.radio(
    "Select Model",
    ["MusicGen (AI)", "LSTM (Old Model)"]
)

# ================= STYLE ================= #

def apply_style(prompt, style):
    if style == "Lo-fi":
        return prompt + " chill lofi beats"
    elif style == "Jazz":
        return prompt + " smooth jazz music"
    elif style == "EDM":
        return prompt + " energetic electronic dance music"
    elif style == "Classical":
        return prompt + " classical orchestra piano"
    return prompt

# ================= GENERATE ================= #

if st.button("Generate Music"):

    if prompt.strip() == "":
        st.warning("Please enter a prompt!")

    else:
        final_prompt = apply_style(prompt, style)

        progress = st.progress(0)

        with st.spinner("Generating music... 🎵"):

            progress.progress(20)

            if model_choice == "MusicGen (AI)":
                audio_path = generate_musicgen(final_prompt, duration)

            else:
                notes = generate_lstm(
                    lstm_model,
                    network_input,
                    int_to_note
                )

                audio_path = create_audio_lstm(notes)

            progress.progress(100)

        st.success("Music Generated 🎶")

        st.audio(audio_path)

        with open(audio_path, "rb") as f:
            st.download_button(
                label="Download Music",
                data=f,
                file_name="generated_music.wav",
                mime="audio/wav"
            )

# ---------------------------change no 6----------------------------------------------------------------


# import streamlit as st
# from generate import generate_musicgen, generate_lstm, create_audio_lstm, load_musicgen
# from tensorflow.keras.models import load_model
# from preprocess import get_notes
# from utils import prepare_sequences

# st.set_page_config(page_title="AI Music Generator", layout="centered")

# st.title("🎵 AI Music Generator (Premium Version)")

# # ================= PRELOAD MUSICGEN ================= #

# @st.cache_resource
# def preload_musicgen():
#     return load_musicgen()

# with st.spinner("Loading MusicGen AI Model... First time only"):
#     preload_musicgen()

# # ================= LOAD LSTM ================= #

# @st.cache_resource
# def load_lstm_model():
#     return load_model("models/model.h5", compile=False)

# @st.cache_data
# def load_data():
#     notes = get_notes("dataset/midi_files")

#     # MUST match training sequence length
#     network_input, _, note_to_int, int_to_note, _ = prepare_sequences(notes, 100)

#     return network_input, int_to_note

# lstm_model = load_lstm_model()
# network_input, int_to_note = load_data()

# # ================= LSTM ================= #

# def generate_lstm(model, network_input, int_to_note):
#     start = np.random.randint(0, len(network_input)-1)
#     pattern = network_input[start]

#     output = []

#     for _ in range(100):   # longer melody

#         prediction_input = pattern.reshape(1, len(pattern), 1)

#         prediction = model.predict(
#             prediction_input,
#             verbose=0
#         )

#         # top prediction
#         index = np.argmax(prediction)

#         result = int_to_note[index]

#         output.append(result)

#         pattern = np.append(pattern, index)
#         pattern = pattern[1:]

#     return output


# def create_audio_lstm(prediction_output, duration=0.32):
#     sample_rate = 44100
#     audio = []

#     for pattern in prediction_output:

#         try:
#             pitch = int(pattern.split('.')[0]) if '.' in pattern else 60
#         except:
#             pitch = 60

#         freq = 440 * (2 ** ((pitch - 69) / 12))

#         t = np.linspace(
#             0,
#             duration,
#             int(sample_rate * duration),
#             False
#         )

#         wave = np.sin(2 * np.pi * freq * t)

#         # smoother sound
#         envelope = np.linspace(1, 0.2, len(wave))
#         wave = wave * envelope

#         audio.extend(wave)

#     audio = np.array(audio)

#     if len(audio) == 0:
#         audio = np.zeros(sample_rate)

#     audio = audio / np.max(np.abs(audio))
#     audio = (audio * 32767).astype(np.int16)

#     os.makedirs("output", exist_ok=True)

#     path = "output/output.wav"

#     wavfile.write(path, sample_rate, audio)

#     return path

# # ================= UI ================= #

# prompt = st.text_input("Enter your music prompt")

# style = st.selectbox(
#     "Select Style",
#     ["None", "Lo-fi", "Jazz", "EDM", "Classical"]
# )

# duration = st.radio(
#     "Select Duration",
#     ["Short", "Medium", "Long"]
# )

# model_choice = st.radio(
#     "Select Model",
#     ["MusicGen (AI)", "LSTM (Custom Trained AI)"]
# )

# # ================= STYLE ================= #

# def apply_style(prompt, style):
#     if style == "Lo-fi":
#         return prompt + " chill lofi beats"
#     elif style == "Jazz":
#         return prompt + " smooth jazz music"
#     elif style == "EDM":
#         return prompt + " energetic electronic dance music"
#     elif style == "Classical":
#         return prompt + " classical orchestra piano"
#     return prompt

# # ================= GENERATE ================= #

# if st.button("Generate Music"):

#     if prompt.strip() == "":
#         st.warning("Please enter a prompt!")

#     else:
#         final_prompt = apply_style(prompt, style)

#         progress = st.progress(0)

#         with st.spinner("Generating music... 🎵"):

#             progress.progress(20)

#             if model_choice == "MusicGen (AI)":
#                 audio_path = generate_musicgen(final_prompt, duration)

#             else:
#                 notes = generate_lstm(
#                     lstm_model,
#                     network_input,
#                     int_to_note
#                 )

#                 audio_path = create_audio_lstm(
#                     notes,
#                     duration=0.32
#                 )

#             progress.progress(100)

#         st.success("Music Generated 🎶")

#         st.audio(audio_path)

#         with open(audio_path, "rb") as f:
#             st.download_button(
#                 label="Download Music",
#                 data=f,
#                 file_name="generated_music.wav",
#                 mime="audio/wav"
#             )