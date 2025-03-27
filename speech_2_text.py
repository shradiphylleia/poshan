# import torch
# from transformers import Speech2TextProcessor, Speech2TextForConditionalGeneration
# import soundfile as sf
# import io
# import torchaudio

# model = Speech2TextForConditionalGeneration.from_pretrained("facebook/s2t-medium-librispeech-asr")
# processor = Speech2TextProcessor.from_pretrained("facebook/s2t-medium-librispeech-asr")

# def speech_text(audio_file) -> str:
#     """
#     Converts speech to text.

#     Args:
#         audio_file: 

#     Returns:
#         str: text.
#     """
#     try:
#         audio_data, sampling_rate = sf.read(io.BytesIO(audio_file.getvalue()), dtype="float32")

#         target_sampling_rate = 16000
#         if sampling_rate != target_sampling_rate:
#             audio_data = torch.tensor(audio_data, dtype=torch.float32)
#             audio_data = torchaudio.functional.resample(
#                 audio_data, orig_freq=sampling_rate, new_freq=target_sampling_rate
#             ).numpy()

#         input_features = processor(audio_data, sampling_rate=target_sampling_rate, return_tensors="pt").input_features

#         with torch.no_grad():
#             generated_ids = model.generate(input_features=input_features)

#         transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)
#         return transcription[0] if transcription else "Sorry, couldn't transcribe the audio."

#     except Exception as e:
#         return f"Error processing audio: {e}"

