import numpy as np
from music_generator import MusicGenerator
from data_preprocessing import load_midi, prepare_sequences

def train_model(midi_file):
    notes = load_midi(midi_file)
    input_sequences, output_notes, note_to_int = prepare_sequences(notes)

    # Convert to numpy arrays
    input_sequences = np.array(input_sequences)
    output_notes = np.array(output_notes)

    # Create and train the model
    music_gen = MusicGenerator()
    music_gen.train(input_sequences, epochs=50)

if __name__ == "__main__":
    train_model("path_to_your_midi_file.mid")  # Update with your MIDI file path
