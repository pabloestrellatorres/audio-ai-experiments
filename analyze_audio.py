import sys
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


def analyze_audio(file_path):
    print(f"\nAnalyzing: {file_path}\n")

    # Load audio
    y, sr = librosa.load(file_path, sr=None, mono=True)

    duration = librosa.get_duration(y=y, sr=sr)

    # Tempo and beats
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    # Energy
    rms = librosa.feature.rms(y=y)[0]
    rms_times = librosa.times_like(rms, sr=sr)

    # Print basic information
    print(f"Sample rate: {sr} Hz")
    print(f"Duration: {duration:.2f} seconds")
    print(f"Estimated BPM: {float(np.asarray(tempo).flat[0]):.2f}")
    print(f"Detected beats: {len(beat_times)}")

    # Energy plot
    plt.figure(figsize=(12, 5))
    plt.plot(rms_times, rms)
    plt.title("Audio Energy")
    plt.xlabel("Time (seconds)")
    plt.ylabel("RMS Energy")
    plt.tight_layout()
    plt.savefig("audio_energy.png", dpi=150)
    plt.close()

    # Spectrogram
    D = librosa.amplitude_to_db(
        np.abs(librosa.stft(y)),
        ref=np.max
    )

    plt.figure(figsize=(12, 6))
    librosa.display.specshow(
        D,
        sr=sr,
        x_axis="time",
        y_axis="log"
    )
    plt.colorbar(format="%+2.0f dB")
    plt.title("Spectrogram")
    plt.tight_layout()
    plt.savefig("spectrogram.png", dpi=150)
    plt.close()

    # Save beat positions
    np.savetxt(
        "beats.txt",
        beat_times,
        fmt="%.3f",
        header="Beat positions in seconds"
    )

    print("\nAnalysis complete.")
    print("Generated:")
    print("- audio_energy.png")
    print("- spectrogram.png")
    print("- beats.txt")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_audio.py <audio_file>")
        sys.exit(1)

    analyze_audio(sys.argv[1])
