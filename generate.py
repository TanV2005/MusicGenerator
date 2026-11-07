# -----------------------CHANGE NO 1-----------------------------------

# import numpy as np
# from music21 import stream, note, chord

# def sample(preds, temperature=1.0):
#     preds = np.asarray(preds).astype('float64')
#     preds = np.log(preds + 1e-8) / temperature
#     exp_preds = np.exp(preds)
#     preds = exp_preds / np.sum(exp_preds)
#     return np.random.choice(len(preds), p=preds)


# def generate_notes(model, network_input, int_to_note, temperature=0.8):
#     start = np.random.randint(0, len(network_input)-1)
#     pattern = network_input[start]

#     output = []

#     for _ in range(200):
#         prediction = model.predict(pattern.reshape(1, len(pattern), 1), verbose=0)
#         index = sample(prediction[0], temperature)

#         result = int_to_note[index]
#         output.append(result)

#         pattern = np.append(pattern, index)
#         pattern = pattern[1:]

#     return output


# def create_midi(notes, filename="output/output.mid"):
#     output_notes = []

#     for n in notes:
#         if '.' in n:
#             chord_notes = [note.Note(int(x)) for x in n.split('.')]
#             output_notes.append(chord.Chord(chord_notes))
#         else:
#             output_notes.append(note.Note(n))

#     midi_stream = stream.Stream(output_notes)
#     midi_stream.write('midi', fp=filename)

# -----------------------CHANGE NO 2-----------------------------------

# import numpy as np
# from music21 import stream, note, chord

# def sample(preds, temperature=1.0):
#     preds = np.asarray(preds).astype('float64')
#     preds = np.log(preds + 1e-8) / temperature
#     exp_preds = np.exp(preds)
#     preds = exp_preds / np.sum(exp_preds)
#     return np.random.choice(len(preds), p=preds)

# def generate_notes(model, network_input, int_to_note, temperature=0.8):
#     start = np.random.randint(0, len(network_input)-1)
#     pattern = network_input[start]
#     output = []

#     for _ in range(200):  # reduced for speed
#         prediction_input = np.reshape(pattern, (1, len(pattern), 1))
#         prediction = model.predict(prediction_input, verbose=0)
#         index = sample(prediction[0], temperature)
#         result = int_to_note[index]
#         output.append(result)
#         pattern = np.append(pattern, index)
#         pattern = pattern[1:]

#     return output

# def create_midi(prediction_output):
#     offset = 0
#     output_notes = []

#     for pattern in prediction_output:
#         if '.' in pattern or pattern.isdigit():
#             notes = pattern.split('.')
#             notes = [note.Note(int(n)) for n in notes]
#             chord_obj = chord.Chord(notes)
#             chord_obj.offset = offset
#             output_notes.append(chord_obj)
#         else:
#             new_note = note.Note(pattern)
#             new_note.offset = offset
#             output_notes.append(new_note)

#         offset += 0.5

#     midi_stream = stream.Stream(output_notes)
#     midi_stream.write('midi', fp="output/output.mid")


# -----------------------CHANGE NO 3-----------------------------------

# import numpy as np
# import pretty_midi

# def sample(preds, temperature=1.0):
#     preds = np.asarray(preds).astype('float64')
#     preds = np.log(preds + 1e-8) / temperature
#     exp_preds = np.exp(preds)
#     preds = exp_preds / np.sum(exp_preds)
#     return np.random.choice(len(preds), p=preds)

# def generate_notes(model, network_input, int_to_note, temperature=0.8):
#     start = np.random.randint(0, len(network_input)-1)
#     pattern = network_input[start]
#     output = []

#     for _ in range(80):   # FAST generation
#         prediction_input = pattern.reshape(1, len(pattern), 1)
#         prediction = model.predict(prediction_input, verbose=0)

#         index = sample(prediction[0], temperature)
#         result = int_to_note[index]

#         output.append(result)
#         pattern = np.append(pattern, index)
#         pattern = pattern[1:]

#     return output


# def create_audio(prediction_output):
#     pm = pretty_midi.PrettyMIDI()
#     instrument = pretty_midi.Instrument(program=0)

#     start = 0
#     for pattern in prediction_output:
#         try:
#             pitch = int(pattern.split('.')[0]) if '.' in pattern else pretty_midi.note_name_to_number(pattern)
#         except:
#             pitch = 60  # fallback

#         note_obj = pretty_midi.Note(
#             velocity=100,
#             pitch=pitch,
#             start=start,
#             end=start + 0.5
#         )
#         instrument.notes.append(note_obj)
#         start += 0.5

#     pm.instruments.append(instrument)

#     audio_path = "output/output.wav"
#     pm.write(audio_path)

#     return audio_path


# -----------------------CHANGE NO 4-----------------------------------


# import numpy as np
# import pretty_midi
# import numpy as np
# from scipy.io.wavfile import write
# import os

# # Sampling function
# def sample(preds, temperature=1.0):
#     preds = np.asarray(preds).astype('float64')
#     preds = np.log(preds + 1e-8) / temperature
#     exp_preds = np.exp(preds)
#     preds = exp_preds / np.sum(exp_preds)
#     return np.random.choice(len(preds), p=preds)

# # Generate notes
# def generate_notes(model, network_input, int_to_note, temperature=0.8):
#     start = np.random.randint(0, len(network_input)-1)
#     pattern = network_input[start]
#     output = []

#     for _ in range(80):  # FAST
#         prediction_input = pattern.reshape(1, len(pattern), 1)
#         prediction = model.predict(prediction_input, verbose=0)

#         index = sample(prediction[0], temperature)
#         result = int_to_note[index]

#         output.append(result)
#         pattern = np.append(pattern, index)
#         pattern = pattern[1:]

#     return output


# # # Create audio (FIXED PITCH ERROR)
# # def create_audio(prediction_output):
# #     pm = pretty_midi.PrettyMIDI()
# #     instrument = pretty_midi.Instrument(program=0)

# #     start = 0

# #     for pattern in prediction_output:
# #         try:
# #             if '.' in pattern:
# #                 pitch = int(pattern.split('.')[0])
# #             else:
# #                 pitch = pretty_midi.note_name_to_number(pattern)
# #         except:
# #             pitch = 60  # fallback

# #         # 🔥 FIX: Clamp pitch to valid MIDI range
# #         pitch = max(0, min(127, pitch))

# #         note_obj = pretty_midi.Note(
# #             velocity=100,
# #             pitch=pitch,
# #             start=start,
# #             end=start + 0.5
# #         )

# #         instrument.notes.append(note_obj)
# #         start += 0.5

# #     pm.instruments.append(instrument)

# #     audio_path = "output/output.wav"
# #     pm.write(audio_path)

# #     return audio_path


# # import numpy as np
# # from scipy.io.wavfile import write
# # import os

# def create_audio(prediction_output):
#     sample_rate = 44100
#     duration = 0.3

#     audio = []

#     for pattern in prediction_output:
#         try:
#             if '.' in pattern:
#                 pitch = int(pattern.split('.')[0])
#             else:
#                 pitch = 60
#         except:
#             pitch = 60

#         pitch = max(0, min(127, pitch))

#         freq = 440 * (2 ** ((pitch - 69) / 12))

#         t = np.linspace(0, duration, int(sample_rate * duration), False)
#         wave = np.sin(2 * np.pi * freq * t)

#         audio.extend(wave)

#     audio = np.array(audio)

#     # 🔥 VERY IMPORTANT FIX
#     if len(audio) == 0:
#         audio = np.zeros(sample_rate)

#     audio = audio / np.max(np.abs(audio))  # normalize
#     audio = (audio * 32767).astype(np.int16)

#     # ensure folder exists
#     os.makedirs("output", exist_ok=True)

#     audio_path = "output/output.wav"
#     write(audio_path, sample_rate, audio)

#     print("Audio saved at:", audio_path)  # DEBUG

#     return audio_path




# -----------------------CHANGE NO 5-----------------------------------

# import numpy as np
# from scipy.io.wavfile import write

# # 🎯 Sampling
# def sample(preds, temperature=1.0):
#     preds = np.asarray(preds).astype('float64')
#     preds = np.log(preds + 1e-8) / temperature
#     exp_preds = np.exp(preds)
#     preds = exp_preds / np.sum(exp_preds)
#     return np.random.choice(len(preds), p=preds)


# # 🎯 Generate Notes (with pitch control)
# def generate_notes(model, network_input, int_to_note, temperature=0.8, pitch_range=(40, 90)):
#     start = np.random.randint(0, len(network_input)-1)
#     pattern = network_input[start]
#     output = []

#     min_pitch, max_pitch = pitch_range

#     for _ in range(80):
#         prediction_input = pattern.reshape(1, len(pattern), 1)
#         prediction = model.predict(prediction_input, verbose=0)

#         index = sample(prediction[0], temperature)
#         result = int_to_note[index]

#         # 🎯 Pitch filtering
#         try:
#             pitch = int(result.split('.')[0]) if '.' in result else 60
#             if pitch < min_pitch or pitch > max_pitch:
#                 continue
#         except:
#             pass

#         output.append(result)
#         pattern = np.append(pattern, index)
#         pattern = pattern[1:]

#     return output


# # 🎯 Create Audio (with speed control)
# def create_audio(prediction_output, duration=0.4):
#     sample_rate = 44100
#     audio = []

#     for pattern in prediction_output:
#         try:
#             if '.' in pattern:
#                 pitch = int(pattern.split('.')[0])
#             else:
#                 pitch = 60
#         except:
#             pitch = 60

#         pitch = max(0, min(127, pitch))

#         freq = 440 * (2 ** ((pitch - 69) / 12))

#         t = np.linspace(0, duration, int(sample_rate * duration), False)
#         wave = np.sin(2 * np.pi * freq * t)

#         audio.extend(wave)

#     audio = np.array(audio)

#     if len(audio) == 0:
#         audio = np.zeros(sample_rate)

#     audio = audio / np.max(np.abs(audio))
#     audio = (audio * 32767).astype(np.int16)

#     import os
#     os.makedirs("output", exist_ok=True)

#     audio_path = "output/output.wav"
#     write(audio_path, sample_rate, audio)

#     return audio_path



# --------------------------------------CHANGE NO 6-----------------------------------



# # using pretrained model from Hugging Face for music generation (much faster and better quality)
# # musicgen-small is a 60M parameter model that can generate 30s of music in under 5 seconds on CPU

# from transformers import AutoProcessor, MusicgenForConditionalGeneration
# import scipy.io.wavfile as wavfile
# import os

# # Load model once
# processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
# model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")

# def generate_music(prompt):
#     inputs = processor(
#         text=[prompt],
#         padding=True,
#         return_tensors="pt",
#     )

#     audio_values = model.generate(**inputs, max_new_tokens=256)

#     sampling_rate = model.config.audio_encoder.sampling_rate
#     # audio = audio_values[0].cpu().numpy()
#     import numpy as np

#     audio = audio_values[0].cpu().numpy()

#     # 🔥 FIX: Normalize audio
#     audio = audio / np.max(np.abs(audio))

#     # 🔥 Convert to int16 (required for WAV)
#     audio = (audio * 32767).astype(np.int16)

#     # Ensure output folder exists
#     os.makedirs("output", exist_ok=True)

#     output_path = "output/output.wav"
#     wavfile.write(output_path, sampling_rate, audio)

#     # output_path = "output/output.wav"
#     # wavfile.write(output_path, sampling_rate, audio)

#     # output_path = "output/output.wav"
#     # wavfile.write(output_path, sampling_rate, audio)

#     return output_path    


# --------------------------------------------------CHANGE NO 7-----------------------------------



# import os
# import numpy as np
# import torch
# import scipy.io.wavfile as wavfile
# from transformers import AutoProcessor, MusicgenForConditionalGeneration

# # 🔥 Load model only once (important for performance)
# processor = None
# model = None

# def load_musicgen():
#     global processor, model

#     if processor is None or model is None:
#         processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
#         model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")

#     return processor, model


# def generate_music(prompt):
#     processor, model = load_musicgen()

#     # Process input
#     inputs = processor(
#         text=[prompt],
#         padding=True,
#         return_tensors="pt",
#     )

#     # Generate audio
#     audio_values = model.generate(**inputs, max_new_tokens=256)

#     sampling_rate = model.config.audio_encoder.sampling_rate
#     audio = audio_values[0].cpu().numpy()

#     # 🔥 Fix audio shape
#     if len(audio.shape) > 1:
#         audio = audio.squeeze()

#     # 🔥 Remove invalid values
#     audio = np.nan_to_num(audio)

#     # 🔥 Normalize safely
#     max_val = np.max(np.abs(audio))
#     if max_val > 0:
#         audio = audio / max_val

#     # 🔥 Convert to int16 (WAV requirement)
#     audio = (audio * 32767).astype(np.int16)

#     # Ensure output folder exists
#     os.makedirs("output", exist_ok=True)

#     output_path = "output/output.wav"
#     wavfile.write(output_path, sampling_rate, audio)

#     return output_path


    # --------------------------------------------------CHANGE NO 8-----------------------------------

    # adding more features 




# import os
# import numpy as np
# import torch
# import scipy.io.wavfile as wavfile
# from transformers import AutoProcessor, MusicgenForConditionalGeneration

# # ================= MUSICGEN ================= #

# processor = None
# model = None

# def load_musicgen():
#     global processor, model
#     if processor is None or model is None:
#         processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
#         model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")
#     return processor, model


# def generate_musicgen(prompt, duration_type="Medium"):
#     processor, model = load_musicgen()

#     # 🎯 Duration control
#     if duration_type == "Short":
#         tokens = 256
#     elif duration_type == "Medium":
#         tokens = 700
#     else:
#         tokens = 1500  # Long

#     inputs = processor(text=[prompt], return_tensors="pt")

#     audio_values = model.generate(**inputs, max_new_tokens=tokens)

#     sampling_rate = model.config.audio_encoder.sampling_rate
#     audio = audio_values[0].cpu().numpy()

#     # Fix audio
#     if len(audio.shape) > 1:
#         audio = audio.squeeze()

#     audio = np.nan_to_num(audio)

#     max_val = np.max(np.abs(audio))
#     if max_val > 0:
#         audio = audio / max_val

#     audio = (audio * 32767).astype(np.int16)

#     os.makedirs("output", exist_ok=True)
#     output_path = "output/output.wav"
#     wavfile.write(output_path, sampling_rate, audio)

#     return output_path


# # ================= LSTM (OLD SYSTEM) ================= #

# def generate_lstm(model, network_input, int_to_note, temperature=0.8):
#     import numpy as np

#     start = np.random.randint(0, len(network_input)-1)
#     pattern = network_input[start]
#     output = []

#     for _ in range(80):
#         prediction_input = pattern.reshape(1, len(pattern), 1)
#         prediction = model.predict(prediction_input, verbose=0)

#         index = np.argmax(prediction)
#         result = int_to_note[index]

#         output.append(result)
#         pattern = np.append(pattern, index)
#         pattern = pattern[1:]

#     return output


# def create_audio_lstm(prediction_output, duration=0.4):
#     sample_rate = 44100
#     audio = []

#     for pattern in prediction_output:
#         try:
#             pitch = int(pattern.split('.')[0]) if '.' in pattern else 60
#         except:
#             pitch = 60

#         freq = 440 * (2 ** ((pitch - 69) / 12))

#         t = np.linspace(0, duration, int(sample_rate * duration), False)
#         wave = np.sin(2 * np.pi * freq * t)

#         audio.extend(wave)

#     audio = np.array(audio)
#     audio = audio / np.max(np.abs(audio))
#     audio = (audio * 32767).astype(np.int16)

#     os.makedirs("output", exist_ok=True)
#     path = "output/output.wav"
#     wavfile.write(path, sample_rate, audio)

#     return path


#-----------change no 9-----------------------------------------------------------------------



import os
import numpy as np
import torch
import scipy.io.wavfile as wavfile
from transformers import AutoProcessor, MusicgenForConditionalGeneration

# ================= MUSICGEN ================= #

processor = None
music_model = None

def load_musicgen():
    global processor, music_model

    if processor is None:
        processor = AutoProcessor.from_pretrained("facebook/musicgen-small")

    if music_model is None:
        music_model = MusicgenForConditionalGeneration.from_pretrained(
            "facebook/musicgen-small"
        )

    return processor, music_model


def generate_musicgen(prompt, duration_type="Medium"):
    processor, music_model = load_musicgen()

    # Faster token settings
    if duration_type == "Short":
        tokens = 180
    elif duration_type == "Medium":
        tokens = 256
    else:
        tokens = 512

    inputs = processor(
        text=[prompt],
        return_tensors="pt"
    )

    audio_values = music_model.generate(
        **inputs,
        max_new_tokens=tokens
    )

    sampling_rate = music_model.config.audio_encoder.sampling_rate

    audio = audio_values[0].cpu().numpy()

    if len(audio.shape) > 1:
        audio = audio.squeeze()

    audio = np.nan_to_num(audio)

    max_val = np.max(np.abs(audio))
    if max_val > 0:
        audio = audio / max_val

    audio = (audio * 32767).astype(np.int16)

    os.makedirs("output", exist_ok=True)

    output_path = "output/output.wav"
    wavfile.write(output_path, sampling_rate, audio)

    return output_path


# ================= LSTM ================= #

def generate_lstm(model, network_input, int_to_note):
    start = np.random.randint(0, len(network_input)-1)
    pattern = network_input[start]
    output = []

    for _ in range(80):
        prediction_input = pattern.reshape(1, len(pattern), 1)
        prediction = model.predict(prediction_input, verbose=0)

        index = np.argmax(prediction)
        result = int_to_note[index]

        output.append(result)

        pattern = np.append(pattern, index)
        pattern = pattern[1:]

    return output


def create_audio_lstm(prediction_output, duration=0.4):
    sample_rate = 44100
    audio = []

    for pattern in prediction_output:
        try:
            pitch = int(pattern.split('.')[0]) if '.' in pattern else 60
        except:
            pitch = 60

        freq = 440 * (2 ** ((pitch - 69) / 12))

        t = np.linspace(0, duration, int(sample_rate * duration), False)
        wave = np.sin(2 * np.pi * freq * t)

        audio.extend(wave)

    audio = np.array(audio)

    if len(audio) == 0:
        audio = np.zeros(sample_rate)

    audio = audio / np.max(np.abs(audio))
    audio = (audio * 32767).astype(np.int16)

    os.makedirs("output", exist_ok=True)

    path = "output/output.wav"
    wavfile.write(path, sample_rate, audio)

    return path