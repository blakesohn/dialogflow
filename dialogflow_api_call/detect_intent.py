#!/usr/bin/env python

# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Detects intent and returns a synthesized Text-to-Speech (TTS) response

# [START dialogflow_cx_v3_detect_intent_synthesize_tts_response_async]
import uuid
import os
from dotenv import load_dotenv

from google.cloud.dialogflowcx_v3.services.sessions import SessionsClient
from google.cloud.dialogflowcx_v3.types import audio_config
from google.cloud.dialogflowcx_v3.types import session
from google.cloud import texttospeech

def run_sample():
    load_dotenv()
    # TODO(developer): Update these values when running the function
    project_id = os.getenv("PROJECT_ID")
    location = os.getenv("LOCATION")
    agent_id = os.getenv("AGENT_ID")
    text = "반품정책 안내 해주실래요?"
    audio_encoding = "OUTPUT_AUDIO_ENCODING_LINEAR_16"
    language_code = "ko"
    output_file = "output.wav"

    detect_intent_synthesize_tts_response(
        project_id,
        location,
        agent_id,
        text,
        audio_encoding,
        language_code,
        output_file,
    )

def synthesize_gemini_tts(prompt: str, text: str, model_name: str, output_filepath: str = "output.mp3"):
   """Synthesizes speech from the input text and saves it to an MP3 file.

   Args:
       prompt: Stylisting instructions on how to synthesize the content in
         the text field.
       text: The text to synthesize.
       model_name: Gemini model to use. Currently, the available models are
         gemini-2.5-flash-preview-tts and gemini-2.5-pro-preview-tts
       output_filepath: The path to save the generated audio file.
         Defaults to "output.mp3".
   """
   client = texttospeech.TextToSpeechClient()

   synthesis_input = texttospeech.SynthesisInput(text=text, prompt=prompt)

   # Select the voice you want to use.
   voice = texttospeech.VoiceSelectionParams(
       language_code="en-US",
       name="Charon",  # Example voice, adjust as needed
       model_name=model_name
   )

   audio_config = texttospeech.AudioConfig(
       audio_encoding=texttospeech.AudioEncoding.MP3
   )

   # Perform the text-to-speech request on the text input with the selected
   # voice parameters and audio file type.
   response = client.synthesize_speech(
       input=synthesis_input, voice=voice, audio_config=audio_config
   )

   # The response's audio_content is binary.
   with open(output_filepath, "wb") as out:
       out.write(response.audio_content)
       print(f"Audio content written to file: {output_filepath}")

def detect_intent_synthesize_tts_response(
    project_id,
    location,
    agent_id,
    text,
    audio_encoding,
    language_code,
    output_file,
):
    """Returns the result of detect intent with synthesized response."""
    client_options = None
    if location != "global":
        api_endpoint = f"{location}-dialogflow.googleapis.com:443"
        print(f"API Endpoint: {api_endpoint}\n")
        client_options = {"api_endpoint": api_endpoint}
    session_client = SessionsClient(client_options=client_options)
    session_id = str(uuid.uuid4())

    # Constructs the audio query request
    session_path = session_client.session_path(
        project=project_id,
        location=location,
        agent=agent_id,
        session=session_id,
    )
    text_input = session.TextInput(text=text)

    query_input = session.QueryInput(text=text_input, language_code=language_code)
#    synthesize_speech_config = audio_config.SynthesizeSpeechConfig(
#        speaking_rate=1,
#        pitch=1,
#    )
#    output_audio_config = audio_config.OutputAudioConfig(
#        synthesize_speech_config=synthesize_speech_config,
#        audio_encoding=audio_config.OutputAudioEncoding[audio_encoding]
#    )
    request = session.DetectIntentRequest(
        session=session_path,
        query_input=query_input,
        #output_audio_config=output_audio_config,
    )

    response = session_client.detect_intent(request=request)

    print("=" * 20)
    print(f"Query text: {response.query_result.text}")
    response_messages = [
        " ".join(msg.text.text) for msg in response.query_result.response_messages
    ]
    print(f"Response text: {response_messages[0]}")

    synthesize_gemini_tts(
        prompt="Say the following, kindly and friendly, still be intelligible",
        text=response_messages[0],
        model_name="gemini-2.5-flash-preview-tts"
    )
    
#    print("Pitch: " f"{response.output_audio_config.synthesize_speech_config.pitch}")
#    with open(output_file, "wb") as fout:
#        fout.write(response.output_audio)
#    print(f"Audio content written to file: {output_file}")


# [END dialogflow_cx_v3_detect_intent_synthesize_tts_response_async]


if __name__ == "__main__":
    run_sample()