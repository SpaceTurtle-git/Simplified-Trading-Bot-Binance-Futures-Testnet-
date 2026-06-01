import typer
import asyncio
import os
from dotenv import load_dotenv
from bot.client import BinanceClient
from bot.validators import OrderSchema

load_dotenv()
app = typer.Typer(add_completion=False)

client = BinanceClient(os.getenv("API_KEY"), os.getenv("API_SECRET"))

@app.command()
def order(
    symbol: str = typer.Option(..., help="Trading symbol (e.g., BTCUSDT)"),
    side: str = typer.Option(..., help="BUY or SELL"),
    type: str = typer.Option(..., help="MARKET or LIMIT"),
    quantity: float = typer.Option(..., help="Quantity to trade"),
    price: float = typer.Option(None, help="Price for LIMIT orders")
):
    """Places an order on Binance Futures Testnet."""
    try:
        data = OrderSchema(symbol=symbol, side=side, type=type, quantity=quantity, price=price)
        params = {"symbol": data.symbol, "side": data.side, "type": data.type, "quantity": data.quantity}
        if data.price: 
            params["price"] = data.price
        
        result = asyncio.run(client.place_order(params))
        typer.echo(f"Success! Order ID: {result.get('orderId')}")
    except Exception as e:
        typer.secho(f"Error: {str(e)}", fg=typer.colors.RED)

if __name__ == "__main__":
    app()