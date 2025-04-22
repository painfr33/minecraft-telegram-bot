# 🤖 Minecraft Telegram Bot (MTB)  
### _Умный бот-ассистент для твоего Minecraft сервера в Telegram!_ 🎮✨  

MTB — это быстрый, гибкий и суперполезный бот, который поможет управлять твоим Minecraft сервером прямо из Telegram!  

![](https://cdn.dribbble.com/users/1140536/screenshots/17790766/media/18d84ee30cbebf638fc9773196be4e84.gif)  

## 🔥 Возможности (пока что):  
- **Количество игроков онлайн** 👥  
- **Список ников онлайн-игроков** 📝  
- **Сборка и отправка коллажа с аватарками игроков** 🖼️✨  

## ⚡ Установка  
MTB работает на [Docker](https://www.docker.com/) — просто, быстро и без лишних заморочек!  

### 1️⃣ Ставим Docker:  
```sh
apt install docker-ce
```  

### 2️⃣ Клонируем репозиторий:  
```sh
git clone https://github.com/revisto/minecraft-telegram-bot
cd minecraft-telegram-bot
```  

### 3️⃣ Настраиваем конфиг (.env):  
```sh
cp mc_bot/.env.example .env
```  
Открываем `.env` и заполняем:  
```
minecraft_server_ip=<IP_ТВОЕГО_СЕРВЕРА>  
minecraft_server_port=<ПОРТ>  
telegram_robot_access_token=<ТОКЕН_ТВОЕГО_БОТА>  
```  

## 📸 Добавляем фото игроков  
Хочешь, чтобы бот отправлял фотки игроков? Легко!  
Создай папку `users_pictures` и добавляй фото по никам:  
```sh
users_pictures/revisto:  
rev.jpg  another_pic.jpg  

users_pictures/mehrshad:  
mehrshad.jpg  photo_2024-01-31_10-31-26.jpg  
```  
Бот сам соберёт коллаж и отправит его по запросу! 🎨  

## 🐳 Запуск через Docker  
Всё настроил? Тогда погнали! 🚀  
```sh
docker build -t mc_bot .
docker run -d mc_bot
```  

## 💡 Хочешь помочь проекту?  
Присоединяйся! Баги, идеи, улучшения — всё здесь:  
🔹 [Страница с issues](https://github.com/revisto/minecraft-telegram-bot/issues)  

## 💙 Поддержать проект  
Поставь ⭐️ репозиторию, если бот тебе понравился!  
