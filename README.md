# troll
troll_Linux.py (only tested on ubuntu. dont expect it to work on windows or mac yet)
Allows for a simple Troll Box in a Terminal that should run on any Komodo Asset Chain (z-only chains (such as Pirate) not tested and would require some tweaking if even possible). This has been tested on the Lizze Asset Chain (LIZ). Whatever asset chain you choose to Troll on must be running/synced before starting troll_Linux.py.

I'm not a coder so the code may be brute at best. Always welcome to guidance or help :) I commented as best as I could so others could try to follow what I did. I'm pulling messages from mempool before blocks mine which seems pretty quick. I don't know how this will handle with alot of input yet. IF anyone wants to clean up the code, please feel free. 

If you dont already have Komodo installed, you'll need to install komodo first. https://github.com/KomodoPlatform/komodo

If you want to test on LIZ you'll need to create a LIZ directory and LIZ.conf file in .komodo/LIZ/

Add the following to it:

rpcuser=yourrpcusername

rpcpassword=yoursecurerpcpassword

rpcport=52928

server=1

txindex=1

rpcworkqueue=256

rpcallowip=127.0.0.1



addnode=73.201.153.236

addnode=70.119.217.80

addnode=45.32.204.239

addnode=45.32.227.213

addnode=45.32.210.35



Then run LIZ (or whatever chain you want to troll on). LIZ is a 50% PoW and 50% PoS asset chain.
If LIZ

./src/komodod -ac_name=LIZ -ac_supply=100000000 -ac_reward=10000000000 -ac_halving=250000 -ac_end=3000000 -ac_staked=50 -gen -genproclimit=$(nproc)

NOTE: The last two parameters are optional if you would like to mine LIZ (donate some hash power)
You can either remove them and start it with:

./src/komodod -ac_name=LIZ -ac_supply=100000000 -ac_reward=10000000000 -ac_halving=250000 -ac_end=3000000 -ac_staked=50

or specify less threads to mine with such as 

./src/komodod -ac_name=LIZ -ac_supply=100000000 -ac_reward=10000000000 -ac_halving=250000 -ac_end=3000000 -ac_staked=50 -gen -genproclimit=1


When you run troll_Linux.py it will first ask for a few things
- Username for Session
- Directory Path where komodod is installed (Make sure to include all of the forward slashes such as:
    /home/mydirectroy/komodo/src/
-Asset Chain you wish to Troll on
Then simply troll away!!

Notes:
- Still have some glitches in terminal when receiving messages; input line disappears but still accepts input
- When a transaction is made on the chain you will see a print out ______________Transaction on [asset chain]________
- I don't currently have a method to manage usernames and they are not password protected. (expect spoofing)
- Spacing isn't always great
 
Goals: (If anyone is interested)
- Clean up/optimize the code first and foremost.
- Write scripts for windows and mac
- Create a simple GUI
- Perhaps transfer to oracles instead of KV for messaging and if not at least use oracles for username/pw management
- Dispaly the following in GUI: local mining hashrate, global mining hashrate, balance.
- Implement Secure messaging using encryption (perhaps an enable/disable button on gui). Encryption Key would be provided up front.
- Implement a Lotto CC that pays out daily to users in the last 24 hrs. It would be an opt-in option and each message would send a transaction of a pre-defined amount to the Lotto CC (in additiona to the mining fee). This could also be an enable/disable button on the GUI. Each transaction is an entry to the lotto.
- I've got some other ideas that i think might be pretty good. Depening on the size of data that can be transferred with either KV or Oracles CC.

Let me know what you all think.
 
