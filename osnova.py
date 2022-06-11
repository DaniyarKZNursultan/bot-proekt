from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import random
import requests
import json
path = 'popular_movie.json'


TOKEN = '5337735380:AAHz_OYHl69uvXUha3pLK8WS5B3ujvNKd14'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)




@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Что я умею")
    button_2 = types.KeyboardButton(text="Курс валют")
    button_3 = types.KeyboardButton(text="Рандомный персонаж из доты")
    button_4 = types.KeyboardButton(text="Топ-20 лучших фильмов")
    button_5 = types.KeyboardButton(text="Топ-20 лучших сериалов")
    keyboard.add(button_1).add(button_2).add(button_3).add(button_4).add(button_5)
    await message.answer("Салам, {0.first_name}!".format(message.from_user), reply_markup=keyboard)


@dp.message_handler(Text(equals="Что я умею"))
async def umeet(message: types.Message):
    await message.reply("Ну пока что ничего собственно...")


@dp.message_handler(Text(equals="Курс валют"))
async def exchange(message: types.Message):
    await message.reply("Нету")


@dp.message_handler(Text(equals="Мета героев"))
async def exchange(message: types.Message):
    await message.reply("Нету")


@dp.message_handler(Text(equals="Топ-20 лучших фильмов"))
async def exchange(message: types.Message):
    with open('popular_movies.json', 'r') as file:
        data = json.load(file)
    for item in data:
        movie_get = item.get("movie_name")
        movie_spisok = ''
        for movie in movie_get:
            movie_spisok = movie_spisok + movie + '\n'
        await message.reply(movie_spisok)


@dp.message_handler(Text(equals="Топ-20 лучших сериалов"))
async def exchange(message: types.Message):
    with open('popular_tv.json', 'r') as file:
        data = json.load(file)
    for item in data:
        tv_get = item.get("tv_name")
        tv_spisok = ''
        for tv in tv_get:
            tv_spisok = tv_spisok + tv + '\n'
        await message.reply(tv_spisok)


@dp.message_handler(Text(equals="Рандомный персонаж из доты"))
async def exchange(message: types.Message):
    await message.reply(random.choice(['Abaddon',
                                        'Alchemist',
                                        'Ancient Apparition',
                                        'Anti-Mage',
                                        'Arc Warden',
                                        'Axe',
                                        'Bane',
                                        'Batrider',
                                        'Beastmaster',
                                        'Bloodseeker',
                                        'Bounty Hunter',
                                        'Brewmaster',
                                        'Bristleback',
                                        'Broodmother',
                                        'Centaur Warrunner',
                                        'Chaos Knight',
                                        'Chen',
                                        'Clinkz',
                                        'Clockwerk',
                                        'Crystal Maiden',
                                        'Dark Seer',
                                        'Dark Willow',
                                        'Dawnbreaker',
                                        'Dazzle',
                                        'Death Prophet',
                                        'Disruptor',
                                        'Doom',
                                        'Dragon Knight',
                                        'Drow Ranger',
                                        'Earth Spirit',
                                        'Earthshaker',
                                        'Elder Titan',
                                        'Ember Spirit',
                                        'Enchantress',
                                        'Enigma',
                                        'Faceless Void',
                                        'Grimstroke',
                                        'Gyrocopter',
                                        'Hoodwink',
                                        'Huskar',
                                        'Invoker',
                                        'Io',
                                        'Jakiro',
                                        'Juggernaut',
                                        'Keeper of the Light',
                                        'Kunkka',
                                        'Legion Commander',
                                        'Leshrac',
                                        'Lich',
                                        'Lifestealer',
                                        'Lina',
                                        'Lion',
                                        'Lone Druid',
                                        'Luna',
                                        'Lycan',
                                        'Magnus',
                                        'Marci',
                                        'Mars',
                                        'Medusa',
                                        'Meepo',
                                        'Mirana',
                                        'Monkey King',
                                        'Morphling',
                                        'Naga Siren',
                                        'Natures Prophet',
                                        'Necrophos',
                                        'Night Stalker',
                                        'Nyx Assassin',
                                        'Ogre Magi',
                                        'Omniknight',
                                        'Oracle',
                                        'Outworld Destroyer',
                                        'Pangolier',
                                        'Phantom Assassin',
                                        'Phantom Lancer',
                                        'Phoenix',
                                        'Primal Beast',
                                        'Puck',
                                        'Pudge',
                                        'Pugna',
                                        'Queen of Pain',
                                        'Razor',
                                        'Riki',
                                        'Rubick',
                                        'Sand King',
                                        'Shadow Demon',
                                        'Shadow Fiend',
                                        'Shadow Shaman',
                                        'Silencer',
                                        'Skywrath Mage',
                                        'Slardar',
                                        'Slark',
                                        'Snapfire',
                                        'Sniper',
                                        'Spectre',
                                        'Spirit Breaker',
                                        'Storm Spirit',
                                        'Sven',
                                        'Techies',
                                        'Templar Assassin',
                                        'Terrorblade',
                                        'Tidehunter',
                                        'Timbersaw',
                                        'Tinker',
                                        'Tiny',
                                        'Treant Protector',
                                        'Troll Warlord',
                                        'Tusk',
                                        'Underlord',
                                        'Undying',
                                        'Ursa',
                                        'Vengeful Spirit',
                                        'Venomancer',
                                        'Viper',
                                        'Visage',
                                        'Void Spirit',
                                        'Warlock',
                                        'Weaver',
                                        'Windranger',
                                        'Winter Wyvern',
                                        'Witch Doctor',
                                        'Wraith King',
                                        'Zeus'
                                        ]))



if __name__ == '__main__':
    executor.start_polling(dp)



