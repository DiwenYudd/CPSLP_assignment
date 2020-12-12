from pathlib import Path
import glob

all_diphone_wav_files = (str(item) for item in Path("./diphones").glob('*.wav') if item.is_file())
print(all_diphone_wav_files)
all_diphone_wav = glob.glob('.diphones/*.wav')
print(all_diphone_wav)