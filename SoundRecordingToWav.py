import pandas as pd
from scipy.io.wavfile import write

# Load the CSV file
csv_file_path = 'C:\Users\franze1\Desktop\APL\Programming Training\Personal GitHub\SoundLogtoWav\base1.csv'  # Change this to your file path
data = pd.read_csv(csv_file_path)

# Third column contains the signal data
signal = data.iloc[:, 3].values

# Assuming you have a sample rate defined in your CSV or set it manually
sample_rate = 8000  # Change this if your sample rate is different

# Normalize the signal to the range of int16
signal_normalized = (signal / max(abs(signal)) * 32767).astype('int16')

# Save as WAV file
output_wav_file = 'output_signal.wav'  # Change this to your desired output file name
write(output_wav_file, sample_rate, signal_normalized)

print(f'Successfully converted {csv_file_path} to {output_wav_file}')