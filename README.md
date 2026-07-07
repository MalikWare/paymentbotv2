# Payment Discord Bot

A simple Discord bot that allows you to quickly share your payment information using commands. Instead of manually typing your payment details, the bot responds with clean, organized embeds for each payment method.

## Features

* Embed response for `$venmo`
* Embed response for `$cash`
* Embed response for `$paypal`
* `$methods` command to display all available payment methods
* Clean and customizable embeds
* Lightweight and easy to configure
* Staff only commands
  
## Commands

| Command    | Description                                               |
| ---------- | --------------------------------------------------------- |
| `$venmo`   | Displays your Venmo payment information.                  |
| `$cash`    | Displays your Cash App payment information.               |
| `$paypal`  | Displays your PayPal payment information.                 |
| `$methods` | Displays all available payment methods in a single embed. |

## Installation

1. Clone the repository.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Open `bot.py` and replace the placeholder values with:

   * Your Discord bot token
   * Your Venmo information
   * Your Cash App information
   * Your PayPal information
4. Start the bot:

   ```bash
   python bot.py
   ```

## Requirements

* Python 3.10 or newer
* discord.py

## Customization

You can easily edit:

* Embed titles
* Embed descriptions
* Embed colors
* Payment usernames
* Footer text
* Images and thumbnails

## License

This project is available for personal and commercial use. Feel free to modify it to fit your needs.
