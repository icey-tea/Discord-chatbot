# Discord Chatbot

Welcome to the **Discord Chatbot** repository! This bot is designed as a beginner-friendly project for learning how to build and deploy simple yet functional Discord bots using Python and the Discord API.

## Features
- **User Interaction:**
  - Greets users when they join the server.
  - Bids users farewell when they leave the server.
- **Dice Roll Command:**
  - Simulate a dice roll with a random number generation feature.
- **Environment Variable Management:**
  - Securely handles sensitive information like the bot token using `dotenv`.

## Technologies Used
- **Programming Language:** Python
- **APIs:** Discord API
- **Libraries:**
  - `discord.py`: Core library for interacting with Discord.
  - `python-dotenv`: To securely manage environment variables.

## Setup and Installation

### Prerequisites
1. Python 3.8 or higher installed on your system.
2. A Discord account.
3. A Discord bot token. You can create one by following [Discord's bot creation guide](https://discord.com/developers/docs/intro).

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/icey-tea/Discord-chatbot.git
   cd Discord-chatbot
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate # For Linux/MacOS
   venv\Scripts\activate   # For Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add the Bot Token**
   - Create a `.env` file in the project directory.
   - Add your bot token to the `.env` file as follows:
     ```
     DISCORD_TOKEN=your_bot_token_here
     ```

5. **Run the Bot**
   ```bash
   python bot.py
   ```

## Usage
- Invite the bot to your Discord server.
- Use the bot commands to interact with it:
  - Greet the bot to see its response.
  - Type the dice roll command to simulate rolling a dice.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a clear description of your changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author
**Eniola Akinpelumi**

For questions or suggestions, feel free to reach out or open an issue in the repository!

---
Happy coding and enjoy building your Discord bots! 🚀


