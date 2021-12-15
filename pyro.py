from pyrogram import Client, filters, raw
api_id = 18024013
api_hash = '10b9cfd8e782f74c211186dd1b189466'
with Client('soroosh', api_id, api_hash) as app:
    for i in ids :
        client.leave_chat(i)
        client.unarchive_chats(i)



app.run()