from dotenv import load_dotenv # This function is used to load environment variables from a .env
from datetime import datetime # This class provides tools for working with dates and times
import os #provides access to operating system-specific functionality

# Import namespaces
import azure.cognitiveservices.speech as speech_sdk
from playsound import playsound

def main():
    try:
        global speech_config

        # Get Configuration Settings
        load_dotenv() # Load environment variables from a .env file
        ai_key = os.getenv('SPEECH_KEY')
        ai_region = os.getenv('SPEECH_REGION')

        # Configure speech service
        speech_config = speech_sdk.SpeechConfig(ai_key, ai_region)
        print('Ready to use speech service in:', speech_config.region)

        # Get spoken input
        # performs speech recognition and returns the transcribed text as a string
        command = TranscribeCommand()
        if command.lower() == 'what time is it?':
            TellTime()

    except Exception as ex:
        print(ex)

def TranscribeCommand():
    command = ''

    # Configure speech recognition
    current_dir = os.getcwd()
    audioFile = current_dir + '\\time.wav'
    playsound(audioFile)
    audio_config = speech_sdk.AudioConfig(filename=audioFile)
    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)

    # Process speech input
    speech = speech_recognizer.recognize_once_async().get()
    if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
        command = speech.text
        print(command)
    else:
        print(speech.reason)
        if speech.reason == speech_sdk.ResultReason.Canceled:
            cancellation = speech.cancellation_details
            print(cancellation.reason)
            print(cancellation.error_details)

    # Return the command
    return command

#function to synthesize speech
def TellTime():
    # get current time
    now = datetime.now()
    response_text = 'The time is {}:{:02d}'.format(now.hour,now.minute)


    # Configure speech synthesis
    #en-GE English (United Kingdom)
    # LibbyNeural (feminine)
    # ryanneural (male)
    # more voice https://speech.microsoft.com/portal/voicegallery
    speech_config.speech_synthesis_voice_name = "en-GB-LibbyNeural" 
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)
    
    # Synthesize spoken output
    speak = speech_synthesizer.speak_text_async(response_text).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)

    # Print the response
    print(response_text)


if __name__ == "__main__":
    main()