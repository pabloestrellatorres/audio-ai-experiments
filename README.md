# Audio Analysis

Python-based audio analysis workflow developed as part of my exploration of audio engineering and creative technology.

The project analyzes an original music composition and extracts basic musical and audio characteristics, including:

- Audio duration
- Sample rate
- Estimated tempo (BPM)
- Beat positions
- RMS energy
- Spectral information

## Technologies

- Python
- Librosa
- NumPy
- Matplotlib
- SoundFile

## Example

The analysis was performed on an original composition:

**CHILDREN INSTRU.wav**

Results:

- Duration: 224.64 seconds
- Sample rate: 48 kHz
- Estimated tempo: 125 BPM
- Detected beats: 376

The script generates:

- `audio_energy.png` — visualization of the RMS energy over time
- `spectrogram.png` — frequency analysis over time
- `beats.txt` — detected beat positions in seconds

## Purpose

This project explores practical applications of Python-based audio analysis within professional audio production workflows, as part of my broader interest in AI, generative audio and creative technology.
