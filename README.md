# DiscordBot

## A Discord Bot made using Python

### 1. Go to [link](https://discord.com/developers/docs/intro) , sign up/log in and create a new application.

### 2. Open the following Link : [link](https://replit.com/) 

### 3. Click on "Sign Up" and create an account.

### 4. Click on `Import from Github` and select `Python`    as the language. You will now see the files in the repl.it editor.

### 5. Now got to the  Discord Developer Portal to select the created application and go to "Bot" and then click on "Add Bot". Click on "Reset Token" and then click on "Yes, do it!".

### 6. Copy the token and you'll have to use this new GUI by clicking the lock icon in the sidebar (near where the files are kept). Then you just enter the `name` of a key and its `value` , which is atcually the `token`. And in the repl, you do `import os`, and `my_secret = os.environ['name of your key here']`

### 7. Now moving back to Discord Developer Portal , go to `OAuth2` and select `Bot` in the "Scopes" section. In the `Bot Permissions` section, select `Administrator`.

### 8. Now got to the URL Generater under OAuth2 and Copy the URL and paste it in a new tab. Select the server you want to add the bot to and click on "Authorize".

### 9. Now got to Discord to create a new server. Go to Advanced Settings and enable `Developer Mode`.

### 10. Create a channel int he server to which the bot was added and right click to get the `Copy ID`. Paste it in the `channel_id` variable in the main.py file.

### 11. Now in the repl.it editor and click on `Run` and your bot will be online.

### 12. Now we want our bot to be awake at all times. For this, we will use a service called `Uptime Robot`. Go to [link](https://uptimerobot.com/) and create an account.

### 13. Click on `Add New Monitor` and select `HTTP(s)`.

### 14. In the "Friendly Name" field, enter the name of your choice. In the `URL` field, enter the `URL of your repl.it project`. Which will refelctedon running the keep_alive.py file in the repl.it editor.

### 15. Click on `Create Monitor` and you are done.


> ###  Now you can use the commands in the "main.py" file to control your bot. You can also add more commands to the bot by adding more functions in the "main.py" file.

> ### Woohoo! You have created your own Discord Bot.


