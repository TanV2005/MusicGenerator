# import numpy as np

# def prepare_sequences(notes, seq_len=100):
#     pitchnames = sorted(set(notes))
    
#     note_to_int = {n: i for i, n in enumerate(pitchnames)}
#     int_to_note = {i: n for i, n in enumerate(pitchnames)}

#     network_input = []
#     network_output = []

#     for i in range(len(notes) - seq_len):
#         seq_in = notes[i:i+seq_len]
#         seq_out = notes[i+seq_len]

#         network_input.append([note_to_int[n] for n in seq_in])
#         network_output.append(note_to_int[seq_out])

#     network_input = np.reshape(network_input, (len(network_input), seq_len, 1))
#     network_input = network_input / float(len(pitchnames))

#     return network_input, network_output, note_to_int, int_to_note, pitchnames



import numpy as np

def prepare_sequences(notes, seq_len=50):
    pitchnames = sorted(set(notes))
    note_to_int = {n: i for i, n in enumerate(pitchnames)}
    int_to_note = {i: n for i, n in enumerate(pitchnames)}

    network_input = []
    network_output = []

    for i in range(len(notes) - seq_len):
        seq_in = notes[i:i+seq_len]
        seq_out = notes[i+seq_len]

        network_input.append([note_to_int[n] for n in seq_in])
        network_output.append(note_to_int[seq_out])

    network_input = np.reshape(network_input, (len(network_input), seq_len, 1))
    return network_input, network_output, note_to_int, int_to_note, pitchnames