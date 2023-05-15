import json

def lambda_handler(event, context):
    # TODO implement
    polly = boto3.client('polly')
    
    intput_text = event['input_text']
    
    output_format = 'mp3'
    voice_id = "Joanna"
    
    response = polly.synthesize(Text = input.text, Output = output_format, VoiceId = voice_id)
    
    audio_data = response['AudioStream'].read()
    
    return {
        'statusCode': 200,
        'header': {
            'Content-Type': "audio/mp3",
        }
        'body': audio_data
    }
