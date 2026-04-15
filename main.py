import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.types import FSInputFile

TOKEN = "8521316310:AAGZtU3d5Mkz7h8ExybkwNPK_1g5JiXhvWw"


dp = Dispatcher()




@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    txt = f"""
botda ushbu commandalar mavjud

/navoi
/toshkent
/jizzax
/surxandaryo
/qashqadaryo
/samarqand
/buxoro
"""



    await message.answer(txt)




@dp.message(Command("navoi"))
async def navoi_info(message: Message):
    image_url_file = FSInputFile("image/navoi.jpg")
    await message.answer_photo(photo=image_url_file, caption="Навои́ (узб. Navoiy / Навоий) — город в центральной части Республики Узбекистан, административный центр Навоийской области. Расположен на юго-западе пустыни Кызылкум, на берегу реки Заравшан. Один из крупнейших промышленных центров страны, важный транспортный узел и административно-экономическое ядро региона.")




@dp.message(Command("toshkent"))
async def navoi_info(message: Message):
    imag_url_file = FSInputFile("image/toshkent.jpg")
    await message.answer_photo(photo=imag_url_file, caption="Toshkent — Oʻzbekistonning poytaxti va eng yirik shahri, aholisi boʻyicha Markaziy Osiyodagi eng yirik qadimiy shaharlardan biri. Oʻzbekistonning shimoli-sharqiy qismida, Qozogʻiston bilan chegaraga yaqin qismda joylashgan boʻlib, maydoni 631.29 km2 ni tashkil etadi. 2024-yilning 1-iyulidagi maʼlumotlarga koʻra, Toshkent aholisi 3 075 000 nafar kishini (Oʻzbekiston aholisining qariyb 9 foizi) tashkil etadi[2]. 2024-yilning birinchi kvartal maʼlumotlarga koʻra, Toshkent shahrining YIMi $25 milliardni tashkil etadi va bu koʻrsatkich Oʻzbekistondagi eng katta YIMga ega shahar boʻlib kelmoqda.")






@dp.message(Command("jizzax"))
async def navoi_info(message: Message):
    imag_url_file = FSInputFile("image/jizzax.jpg")
    await message.answer_photo(photo=imag_url_file, caption="Jizzakh (/dʒɪzˈzæk/; Uzbek: Jizzax [dʒɪzˈzɑχ]) is a city and the center of Jizzakh Region in Uzbekistan, located in the northeast of Samarkand. It is a district-level city.[1] The population of Jizzakh is 179,200 (2020 est.).")




@dp.message(Command("surxandaryo"))
async def navoi_info(message: Message):
    imae_url_file = FSInputFile("image/surxondayo.jpg")
    await message.answer_photo(photo=imae_url_file, caption="Surxondaryo viloyati — Oʻzbekiston Respublikasi tarkibidagi viloyat. 1941-yil 6-martda tashkil etilgan (1925-yil 29-iyundan Surxondaryo okrugi boʻlgan). Respublikaning janubi-sharqida, Surxon-Sherobod vodiysida joylashgan. Viloyat nomi vohadan oqib oʻtuvchi “Surxon” (fors-tojik: “qizil”) daryosi nomidan kelib chiqqan. Janubidan Amudaryo boʻylab Afgʻoniston, shimoliy, shimoli-sharq va sharqdan Tojikiston, janubi-gʻarbdan Turkmaniston, shimoli-gʻarbdan Qashqadaryo viloyati bilan chegaradosh. Maydoni 20,1 ming km². Aholisi 2 million 907 ming kishi (2024-yil 1-Iyun holatiga koʻra). Tarkibida 14 ta tuman (Angor, Bandixon, Boysun, Denov, Jarqoʻrgʻon, Muzrabot, Oltinsoy, Sariosiyo, Termiz, Uzun, Sherobod, Shoʻrchi, Qiziriq, Qumqoʻrgʻon), 8 ta shahar (Boysun, Denov, Jarqoʻrgʻon, Termiz, Shargʻun, Sherobod, Shoʻrchi, Qumqoʻrgʻon), 114 ta shaharcha, 865 ta qishloq aholi punktlari mavjud")





@dp.message(Command("samarqand"))
async def navoi_info(message: Message):
    mage_url_file = FSInputFile("image/samarqand.jpg")
    await message.answer_photo(photo=mage_url_file, caption="Samarqand- Samarqand viloyati O'zbekiston Respublikasida qadimiy shahar. Amir Temur ordeni sohibi[3]. Viloyatning maʼmuriy, iqtisodiy va madaniy markazi (1938-yildan). 1925-1930-yillarda Respublika poytaxti. Oʻzbekistonning janubi-gʻarbida, Zarafshon vodiysining markaziy qismida (Dargʻom va Siyob kanallari orasida) joylashgan. Oʻrtacha 695 m balandlikda. Toshkentdan 300 km. Samarqanddan Toshkent—Dushanbe, Toshkent—Turkmanboshi, Toshkent—Uchquduq—Qoʻngʻirot temir yoʻllari, Katta Oʻzbek trakti (Toshkent—Termiz yoʻli) oʻtadi. Shahar aholisi va xoʻjaliklari Shovdor, Bogʻishamol ariqlaridan suv oladi. Iyulning oʻrtacha harorati 25,9°, eng baland harorat 40—42°, yanvar oʻrtacha harorati 0,2°, eng past harorat —26°. Maydoni −120 km². Aholisi 585 ming kishi (2024). 2022-yilning 15-16-sentyabr kunlari ShHTga aʼzo davlat rahbarlarining 22-yigʻilishi  Samarqand sammiti  boʻlib oʻtgan.")





@dp.message(Command("buxoro"))
async def navoi_info(message: Message):
    image_url_file = FSInputFile("image/buxoro.jpg")
    await message.answer_photo(photo=image_url_file, caption="Buxoro — Oʻzbekiston Respublikasining qadimiy shaharlaridan biri, Buxoro viloyatining maʼmuriy, iqtisodiy va madaniy markazi. Oʻzbekistonning ilk poytaxti hisoblanadi.Buyuk ipаk yoʻlida yirik tijorat markazlaridan boʻlgan. Oʻzbekistonning janubiy-gʻarbida, Zarafshon daryosi quyi oqimida joylashgan. Toshkentdan 616 km. Buxoro 2 ta shahar rayoni (Fayzulla Xoʻjayev va Toʻqimachilik)ga boʻlingan. Aholisi 290 000 (2019). Aholisining katta qismini oʻzbeklar tashkil etadi. Oliy ta‘lim muassasalari: Buxoro davlat universiteti, Buxoro davlat pedagogika instituti, Buxoro muhandislik-texnologiya instituti.")

async def main() -> None:
   
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

   
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())