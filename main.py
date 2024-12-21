import telebot
from googletrans import Translator, LANGUAGES
from config_data import config


bot = telebot.TeleBot(token=config.BOT_TOKEN)
translator = Translator()


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    text_to_translate = message.text
    if translator.detect(text_to_translate).lang == "lt" and translator.detect(text_to_translate).confidence >= 0.80:
        translated_text = translator.translate(text_to_translate, dest="be").text
    elif translator.detect(text_to_translate).lang == "be" and translator.detect(text_to_translate).confidence >= 0.80:
        translated_text = translator.translate(text_to_translate, dest="lt").text
    else:
        translated_text = "something weird"
    bot.reply_to(message, translated_text)

# text_to_translate = "добрай раніцы"
# if translator.detect(text_to_translate).lang == "lt" and translator.detect(text_to_translate).confidence >= 0.80:
#     print(translator.translate(text_to_translate, dest="be").text)
# elif translator.detect(text_to_translate).lang == "be" and translator.detect(text_to_translate).confidence >= 0.80:
#     print(translator.translate(text_to_translate, dest="lt").text)


# print(translator.detect('이 문장은 한글로 쓰여졌습니다.'))
# detected = translator.detect('이 문장은 한글로 쓰여졌습니다.').lang
# print(detected)
# translated = translator.translate('안녕하세요')
# print(translated)
# print(translated.text)
# print(LANGUAGES)

if __name__ == "__main__":
    bot.polling(none_stop=True)
