# from preprocess import extract_notes
# from utils import prepare_sequences
# from train import create_model, train_model
# from generate import generate_notes, create_midi
# from prompt_engine import apply_prompt_settings

# notes = extract_notes("dataset/midi_files")

# X, y, note_to_int, int_to_note, pitchnames = prepare_sequences(notes)

# model = create_model((X.shape[1], X.shape[2]), len(pitchnames))

# model = train_model(model, X, y)

# prompt = input("Enter mood: ")
# settings = apply_prompt_settings(prompt)

# generated_notes = generate_notes(model, X, int_to_note, settings["temperature"])

# create_midi(generated_notes)

# print("Music Generated 🎵")



import os
from preprocess import get_notes
from utils import prepare_sequences
from train import create_model
from tensorflow.keras.utils import to_categorical

# STEP 1: Count dataset files
midi_path = "dataset/midi_files"
files = [f for f in os.listdir(midi_path) if f.endswith('.mid')]
file_count = len(files)

print("Total MIDI files:", file_count)

# STEP 2: Dynamic parameters
if file_count <= 20:
    epochs = 10
    seq_len = 40
elif file_count <= 50:
    epochs = 7
    seq_len = 50
else:
    epochs = 5
    seq_len = 60

print(f"Using epochs={epochs}, seq_len={seq_len}")

# STEP 3: Load notes
notes = get_notes(midi_path)

# STEP 4: Prepare sequences
network_input, network_output, note_to_int, int_to_note, pitchnames = prepare_sequences(notes, seq_len)

# STEP 5: Normalize input
n_vocab = len(pitchnames)
network_input = network_input / float(n_vocab)

# STEP 6: One-hot encode output
network_output = to_categorical(network_output)

# STEP 7: Create model
model = create_model((network_input.shape[1], network_input.shape[2]), n_vocab)

# STEP 8: Train model
model.fit(network_input, network_output, epochs=epochs, batch_size=64, verbose=1)

# STEP 9: Save model
model.save("models/model.h5")
print("Model saved ✅")