import requests
import time
import json

from Options.Options import version, nom, codage, language, createur, discord, couleur, Reset, LAPprint, APprint, TitrePage

TitrePage("Red-Tiger | Webhook Create")

print(f"""
{couleur.LIGHTRED_EX}[01]{couleur.RED} -> Message Classique
{couleur.LIGHTRED_EX}[02]{couleur.RED} -> Message Embed
""")
choix = int(input(f"[->] {couleur.RESET}"))
try:
    
    if choix == 1:
        choix = 1
        def send_webhook_message(webhook_url, content):
         payload = {
             'content': content
         }

         headers = {
             'Content-Type': 'application/json'
          }

         response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

         if response.status_code == 204:
             LAPprint(f'\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Message envoyé avec succès')
             time.sleep(5)
             Reset()
         else:
             LAPprint(f'\n{couleur.RED}[ERREUR] | {couleur.LIGHTRED_EX}Message non envoyé.')
             time.sleep(5)
             Reset()


        webhook_url = input(f"{couleur.RED}Entrer le lien du Webhook -> {couleur.RESET}")
        if webhook_url.lower().startswith("https://discord.com/api/webhooks"):

            message_content = input(f"{couleur.RED}\nEntrer le message -> {couleur.RESET}")
            send_webhook_message(webhook_url, message_content)


    if choix == 2:
        choix = 2

        def send_embed_webhook(webhook_url, embed_content):
            payload = {
            'embeds': [embed_content]
             }

            headers = {
            'Content-Type': 'application/json'
             }

            response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

            if response.status_code == 204:
               LAPprint(f'\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Message envoyé avec succès !')
               time.sleep(5)
               Reset()
            else:
             LAPprint(f'\n{couleur.RED}[ERREUR] | {couleur.LIGHTRED_EX}Message non envoyé.')
             time.sleep(5)
             Reset()
    
        webhook_url = input(f"{couleur.RED}\nEntrer le lien du Webhook -> {couleur.RESET}")

        print(f""" {couleur.RED}
{couleur.LIGHTRED_EX}[01]{couleur.RED} -> Rouge
{couleur.LIGHTRED_EX}[02]{couleur.RED} -> Orange
{couleur.LIGHTRED_EX}[03]{couleur.RED} -> Jaune
{couleur.LIGHTRED_EX}[04]{couleur.RED} -> Vert
{couleur.LIGHTRED_EX}[05]{couleur.RED} -> Bleu
{couleur.LIGHTRED_EX}[06]{couleur.RED} -> Violet
{couleur.LIGHTRED_EX}[07]{couleur.RED} -> Blanc
{couleur.LIGHTRED_EX}[08]{couleur.RED} -> Noir 
""")
        couleur_input = int(input(f"{couleur.RED}Choisissez une couleur -> {couleur.RESET} "))
        try:
            if couleur_input == 1:
                couleure = 0xFF0000  # Rouge
            elif couleur_input == 2:
                couleure = 0xFFA500  # Orange
            elif couleur_input == 3:
                couleure = 0xFFFF00  # Jaune
            elif couleur_input == 4:
                couleure = 0x00FF00  # Vert
            elif couleur_input == 5:
                couleure = 0x0080FF  # Bleu
            elif couleur_input == 6:
               couleure = 0x7f00ff  # Violet
            elif couleur_input == 7: 
                couleure = 0xffffff # Blanc
            elif couleur_input == 8:
                couleure = 0x000000 # Noir
            else:
                couleure = 0xFF0000  # Rouge (par défaut)
        except ValueError as e:
            couleure = 0xFF0000  # Rouge (par défaut)

        embed_content = {
           'title': input(f"{couleur.RED}Titre ->{couleur.RESET} "),
           'description': input(f"{couleur.RED}Description ->{couleur.RESET} "),
           'color': couleure,
           'footer': {
                "text": "Red-Tiger",
                "icon_url": "https://media.discordapp.net/attachments/944760272265031720/1179429697495498834/IMG_1506.png?ex=6582fb00&is=65708600&hm=cbdc48779b762d4d7c95c34bb68a8aabf8314519d0b50c4d7371bea19eac5db4&=&format=webp&quality=lossless",
                    }
        }
        send_embed_webhook(webhook_url, embed_content)

    else:
        LAPprint(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le choix n'existe pas !", couleur.RESET)
        time.sleep(3)
        Reset()
except ValueError as e:
    LAPprint(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le choix n'existe pas !", couleur.RESET)
    time.sleep(3)
    Reset()