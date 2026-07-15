from brain.tools.pitch_detection import detect_pitch
from brain.tools.lufs_meter import detect
from brain.tools.spectrum_analysis import analyze_spectrum
from brain.tools.key_detection import detect_key
from brain.tools.bpm_detection import detect_bpm


def available_tools():

    return {
        "pitch_detection": detect_pitch,
        "lufs_meter": detect,
        "spectrum_analysis": analyze_spectrum,
        "key_detection": detect_key,
        "bpm_detection": detect_bpm,
    }