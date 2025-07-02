
print("bot démarré")

from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from telegram import InputFile

# Fonction pour /start
async def start(update, context):
    await update.message.reply_text("Salut 👋, je suis Mr.Mng!")

# Fonction pour /help
async def help_command(update, context):
    await update.message.reply_text("Voici les commandes disponibles :\n/start - pour démarrer le bot\n/help - pour recevoir de l'aide\nÉcris-moi un mot-clé comme 'vidéo' ou 'image'.")

# Fonction pour gérer tous les messages
async def handle_message(update, context):
    text = update.message.text.lower()

    if "salut" in text:
        await update.message.reply_text("Salut à toi 👋 bienvenue chez I'm MR.Mng! Comment vas-tu ?")

    elif "ça va" in text or "ca va" in text:
        await update.message.reply_text("Oui ça va bien, et toi ? 😄")

    elif "merci" in text:
        await update.message.reply_text("De rien, avec plaisir 😉")

    elif "vidéo" in text or "video" in text:
        try:
            with open("video.mp4", "rb") as video_file:
                await update.message.reply_video(video=InputFile(video_file), caption="Voici ta vidéo 📹")
        except Exception as e:
            await update.message.reply_text(f"Sorry, les vidéos sont peut-être trop lourdes. Réessaye ou compresse-les. Erreur : {e}")

    elif "image" in text or "photo" in text:
        try:
            with open("image.jpg", "rb") as img_file:
                await update.message.reply_photo(photo=InputFile(img_file), caption="Je suis BG ein... Oui je sais 😎")
        except Exception as e:
            await update.message.reply_text(f"Erreur lors de l'envoi de l'image : {e}")

    else:
        await update.message.reply_text(f"Tu m'as dit : {text}, mais je n'ai pas encore de réponse spéciale pour ça 😅")

# Création de l'application
app = ApplicationBuilder().token("7178620711:AAG1-qGhXxYnobLJ3ooEtGMwUFdcbag7enE").build()

# Ajout des handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Lancement du bot
app.run_polling()

