import lightbulb
import hikari

#PARAMETERS

#Bot that needs cleaning
#For example bot_to_clean = 'Bongo#3445'
bot_to_clean = ''
#Filter to delete the bot command messages
#In my case ive used filter = 'b.' since b. is the bot command
filter = ''
#Token for your bot
token = ''

#Bot's Token
bot = lightbulb.BotApp(token)

#Ive used MessageCreateEvent but I think internally GuildMessageCreateEvent is the one being used
@bot.listen (hikari.MessageCreateEvent)
async def deleteMessages(event):
    if(bot_to_clean == str(event.author)):
        await event.message.delete()
    if event.message.content is None:
        event.message.content = []
    else:
        if(filter in event.message.content):
            await event.message.delete()



bot.run()



