import music21

def load_midi(file_path):
    """Load a MIDI file and convert it to a sequence of notes."""
    midi = music21.converter.parse(file_path)
    notes = []
    for element in midi.flat.notes:
        if isinstance(element, music21.note.Note):
            notes.append(str(element.pitch))
        elif isinstance(element, music21.chord.Chord):
            notes.append('.'.join(str(n) for n in element.normalOrder))
    return notes

def prepare_sequences(notes, sequence_length=100):
    """Prepare input and output sequences for the model."""
    unique_notes = sorted(set(notes))
    note_to_int = {note: number for number, note in enumerate(unique_notes)}
    
    input_sequences = []
    output_notes = []
    
    for i in range(len(notes) - sequence_length):
        input_seq = notes[i:i + sequence_length]
        output_seq = notes[i + sequence_length]
        input_sequences.append([note_to_int[note] for note in input_seq])
        output_notes.append(note_to_int[output_seq])
    
    return input_sequences, output_notes, note_to_int
