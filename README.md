# discord filge source
#  Для тех кто хочет ставить на Heroku #
Итак в боте есть такая штука как воспроизведение аудио
И если вы попоробуете провернуть эту фичу на heroku то у вас это не получится
Так что я сейчас расскажу что надо сделать что-бы работало аудио
### 1 этап! ###
![фотка](https://github.com/votin306/discord-filge/blob/main/picture/auth.png "Вход")
1) Мы дожны войти на heroku и создать там проект
2) Полная инструкция есть тут --> https://vk.com/@-197363571-kak-zahostit-bota-dlya-discord-python
### 2 этап! ###
![фотка](https://github.com/votin306/discord-filge/blob/main/picture/setting.png "Настройка")
После настройки переходим в вкладку Settitgs
### 3 этап! ###
![фотка](https://github.com/votin306/discord-filge/blob/main/picture/buildpack.png "buildpack")
Находим пункт buildpack и вводим такие ссылки 
1) https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git
2) https://github.com/xrisk/heroku-opus.git

По умолчанию там стоит heroku/python
### 4 этап! ###
ВКЛЮЧАЕМ БОТА)))))
