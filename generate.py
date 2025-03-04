import numpy as np
from music_generator import MusicGenerator

def generate_music(seed, num_notes=100):
    music_gen = MusicGenerator()
    generated_notes = music_gen.generate(seed, num_notes)
    return generated_notes

if __name__ == "__main__":
    seed = [0] * 100  # Example seed, replace with actual seed data
    generated = generate_music(seed)
    print(generated)
