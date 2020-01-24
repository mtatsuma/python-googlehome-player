import socket
import pychromecast
from gtts import gTTS

def get_speaker(ip=None, name=None):
    if ip:
        return pychromecast.Chromecast(str(ip))
    else:
        speakers = pychromecast.get_chromecasts()
        if name:
            return next(s for s in speakers if s.device.friendly_name == name)
        else:
            return next(speakers)

def speak(text, speaker, lang='en'):
    try:
        tts = gTTS(text=text, lang=lang)
        urls = tts.get_urls()
        if not speaker.is_idle:
            print("Killing current running app")
            speaker.quit_app()
            time.sleep(5)
        speaker.wait()
        speaker.media_controller.play_media(urls[0], 'audit/mp3')
        speaker.media_controller.block_until_active()
    except Exception as e:
        print(str(e))
        raise Exception

def check_speaker(speaker, lang):
    try:
        speak(text='OK', speaker=speaker, lang=lang)
        print('You are ready to speak!')
        return True
    except Exception as e:
        print('Try an another ip or name: %s' % (str(e)))
        return False

def prepare_speaker():
    print('Enter language (English: en or Japanese: ja): ', end="")
    lang = input()
    print('Enter Google Home name or IP: ', end="")
    name_or_ip = input()
    try:
        socket.inet_aton(name_or_ip)
        speaker = get_speaker(ip=name_or_ip)
    except socket.error:
        speaker = get_speaker(name=name_or_ip)
    except Exception as e:
        print('Error: %s' % (str(e)))
        raise Exception
    return speaker, lang

def main():
    while True:
        try:
            speaker, lang = prepare_speaker()
        except Exception:
            continue
        if check_speaker(speaker, lang):
            break
        print('Failed to setup. Try again!')

    print('Start typing ...')
    text = ''
    while text != 'bye':
        print('>> ', end="")
        text = input()
        if text:
            speak(text, speaker, lang)

if __name__ == "__main__":
    main()
