import discord, os
from time import sleep
import random


Token = os.environ['Token'] # here you can do Token = "your token"

# normal list to send random messages from
list = ["استغفرالله", "لا اله الا الله", "الحمدلله", "لا حول ولا قوة الا بالله", "اللهم لك الحمد حتى ترضى ولك الحمد اذا رضيت ولك الحمد حتى الرضى", "اللهم صلي وسلم على محمد", "لا اله الا الله وحده لا شريك له له الملك وله الحمد وهو على كل شيء قدير", "الله واكبر", "سبحان الله وبحمده سبحان الله العظيم", "قُلْ هُوَ اللَّهُ أَحَدٌ اللَّهُ الصَّمَدُ لَمْ يَلِدْ وَلَمْ يُولَدْ وَلَمْ يَكُنْ لَهُ كُفُوًا أَحَدٌ ", "اللَّهُ لَا إِلَٰهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ ۚ لَا تَأْخُذُهُ سِنَةٌ وَلَا نَوْمٌ ۚ لَّهُ مَا فِي السَّمَاوَاتِ وَمَا فِي الْأَرْضِ ۗ مَن ذَا الَّذِي يَشْفَعُ عِندَهُ إِلَّا بِإِذْنِهِ ۚ يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ ۖ وَلَا يُحِيطُونَ بِشَيْءٍ مِّنْ عِلْمِهِ إِلَّا بِمَا شَاءَ ۚ وَسِعَ كُرْسِيُّهُ السَّمَاوَاتِ وَالْأَرْضَ ۖ وَلَا يَئُودُهُ حِفْظُهُمَا ۚ وَهُوَ الْعَلِيُّ الْعَظِيمُ", "قُلْ أَعُوذُ بِرَبِّ النَّاسِ مَلِكِ النَّاسِ إِلَهِ النَّاسِ مِنْ شَرِّ الْوَسْوَاسِ الْخَنَّاسِ الَّذِي يُوَسْوِسُ فِي صُدُورِ النَّاسِ مِنَ الْجِنَّةِ وَالنَّاسِ", "قُلْ أَعُوذُ بِرَبِّ الْفَلَقِ مِنْ شَرِّ مَا خَلَقَ وَمِنْ شَرِّ غَاسِقٍ إِذَا وَقَبَ وَمِنْ شَرِّ النَّفَّاثَاتِ فِي الْعُقَدِ وَمِنْ شَرِّ حَاسِدٍ إِذَا حَسَدَ", "الحمدلله حمدا كثيرا طيبا مباركا فيه", "سبحان الله والحمدلله ولا اله الا الله والله اكبر", "الله اكبر كبيرا والحمدلله كثيرا وسبحان الله بكرة واصيلا", "استغفرالله", "الحمدلله", "اللهم صلي على محمد وعلى ال محمد كما صليت على ابراهيم وعلى ال ابراهيم انك حميد مجيد"]


class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as', self.user)

  async def on_message(self, message):
    if message.author == self.user:
      return
      
    while True:
      sleep(900) # send message every 15 minutes
      await message.channel.send(random.choice(list))

client = MyClient()
client.run(Token)
