from telethon import TelegramClient, events

# defina as suas credenciais de API do Telegram
api_id = 28182803
api_hash = 'b12b7d312ff1fac4bc3a6f43371fe27e'

# crie uma instância do cliente do Telegram
client = TelegramClient('session_name', api_id, api_hash)

#source_channel_id = -1001958799336  # ID do canal de origem
source_channel_id = -1001608456675
destination_channel_id = -1001876905503  # ID do canal de destino


# crie um manipulador de eventos para novas mensagens
@client.on(events.NewMessage(chats=source_channel_id))
async def handle_new_message(event):
    message = event.message

    #if message.photo:
        ##photo_id = message.photo[-1].id
        #image_path = await message.download_media()
        #await client.send_file(
            #destination_channel_id,  # ID do canal de destino
            #file=image_path,  # caminho para a imagem baixada
            #caption=message.text,  # legenda da mensagem original
            #buttons=message.buttons,  # botões da mensagem original
            #link_preview=message.web_preview,  # link preview da mensagem original
        #)
        #await client.forward_messages(destination_channel_id,message,messages=[photo_id])


    # verifique se a mensagem contém algum texto
    if message.text:
        # encaminhe a mensagem para o canal de destino
        #client.send_message(destination_channel_id, 'Olá, mundo!')

        await client.send_message(
            destination_channel_id,  # ID do canal de destino
            message
            #file=image_path,  # caminho para a imagem baixada
            #caption=message.text,  # legenda da mensagem original
            #buttons=message.buttons,  # botões da mensagem original
            #link_preview=message.web_preview,  # link preview da mensagem original
        )
        
        #await client.forward_messages(destination_channel_id, message,event.message.photo)

    # verifique se a mensagem contém a palavra "oi"
    #if 'oi' in event.raw_text.lower():
        # envie uma resposta personalizada
        #await event.respond('Olá! Tudo bem?')

#@client.on(events.MessageDeleted(chats=source_channel_id))
#async def handle_deleted_message(event):
    #print(f"Uma mensagem foi excluída")
    #message_id = event.deleted_ids[0]
    ##try:
    #await client.delete_messages(destination_channel_id, message_id)
    ##except:
     ##   print(f"Não foi possível deletar a mensagem {message_id} no canal {destination_channel_id}")


# inicie o cliente do Telegram
client.start()

# execute o cliente até que seja desconectado
client.run_until_disconnected()
