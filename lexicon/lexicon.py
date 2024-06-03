LEXICON_RU = {
    '/start': 'Привет! Говорят, в прошлой жизни все мы были булками...\n'\
        'Так сложилось, что я могу заглянуть внутрь тебя, задав всего  несколько вопросов.\n\n'\
        'Ты хочешь узнать кое-что новое о себе?',
    '/help': 'Для запуска нажмите /start\n\n'\
        'Тест создан при поддержке @sakurasshhii 🥰',
    'quest_no': 'Жаль... Если передумаешь, просто нажми кнопку ниже!',
    'quest_start': 'Класс, поехали!',
    'quest_load/1': 'Такс... посмотрим, секундочку...',
    'quest_load/2': 'Щас-щас... секундочку...',
    'quest_end': 'С точностью 99.999{}% могу сказать,\n'\
         'твое истинное обличие — это\n\n{}'
}

BUTTONS_LEXIC: dict[str, str] = {
    'quest_y': 'Конечно!',
    'quest_n': 'Отказываюсь :/'
}

QUEST_RES = dict(zip(
    ['печень', 'блин', 'багет', 'кулич', 'пирог', 'корги', \
    'пицца', 'наполеон', 'эчпочмак', 'слойка'],
    'Пирожок с печенью 🍘,Блинчик со сметанкой 🥞,Багет 🥖,'\
    'Кулич 🍮,Вишневый пирог 🥧,Булка-корги 🐶,Школьная питса 🍕,'\
    'Наполеон! 🍰,Эчпочмак 🥟,Куассссан 🥐'.split(',')
))

MAIN_MENU = {
    '/start': 'Запустить тест',
    '/help': 'Информация о боте'
}

PIC_URL = dict(zip(
    QUEST_RES.keys(),
    ('https://food.pibig.info/uploads/posts/2023-03/1680026580_food-pibig-info-p-pirog-s-kurinoi-pechenyu-v-dukhovke-krasiv-6.jpg',
     'https://petersfoodadventures.com/wp-content/uploads/2016/04/blini-recipe-1.jpg',
     'https://www.imagella.com/cdn/shop/products/e91459be19f6a5ebb11b2200179356c7.jpg?v=1692629605',
     'https://masterpiecer-images.s3.yandex.net/877d733a933e11eea4e92631fd27757d:upscaled',
     'http://image.plus/images/secure/G8XZ6G/yk3Fnall9yAtMzE_1717355428.png',
     'https://masterpiecer-images.s3.yandex.net/4418a8046ea411eeb1704659bdca6a39:upscaled',
     'https://image.plus/images/secure/zo1edm/xuO8D20gTPPSPo1_1717355019.png',
     'https://image.plus/images/secure/z4yb9G/6rAXj8x9ioeBeu3_1717354897.png',
     'https://static.wikia.nocookie.net/edopedia/images/a/a6/%D0%AD%D1%87%D0%BF%D0%BE%D1%87%D0%BC%D0%B0%D0%BA.png/revision/latest?cb=20180706160220&path-prefix=ru',
     'https://image.plus/images/secure/zeVjeG/7tkRRqBrY4liBCU_1717354819.png')
))