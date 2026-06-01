# Simplified-Trading-Bot-Binance-Futures-Testnet

A robust, production-ready Python CLI for executing trades on the Binance Futures Testnet, designed for modularity, scalability, and error handling.

## 🏗️ Architecture

The project follows a clean, decoupled architecture:

*   **`bot/client.py`**: Async wrapper for the Binance API using `httpx`.
*   **`bot/validators.py`**: Enforces business logic and exchange constraints using `Pydantic`.
*   **`cli.py`**: The entry point, built with `Typer` for an intuitive command-line interface.
*   **`bot/logging_config.py`**: Structured logging for system observability.

## 🚀 Setup

1.  **Clone the repository**:
```bash
    git clone [https://github.com/SpaceTurtle-git/Simplified-Trading-Bot-Binance-Futures-Testnet-.git](https://github.com/SpaceTurtle-git/Simplified-Trading-Bot-Binance-Futures-Testnet-.git)
    cd Simplified-Trading-Bot-Binance-Futures-Testnet
```

2.  **Setup virtual environment**:
```bash
    python -m venv venv
```
    *   **Windows**: `venv\Scripts\activate`
    *   **macOS/Linux**: `source venv/bin/activate`

3.  **Install dependencies**:
```bash
    pip install -r requirements.txt
```

4.  **Configuration**:
    Create a `.env` file in the root directory and add your credentials:
```text
    API_KEY=your_testnet_api_key
    API_SECRET=your_testnet_secret_key
```
    > **Note**: Ensure this file is added to your `.gitignore` to prevent leaking credentials.

## 📈 Usage

Execute trades directly via the command line.

**Market Order:**
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```
**Market Limit Order:**
```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 45000
```
