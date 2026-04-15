import argparse
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_order(args.symbol, args.side, args.type, args.quantity, args.price)

        print("\n📊 Order Summary:")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        print(f"Price: {args.price}")

        order = place_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n Order Placed Successfully!")
        print(f"Order ID: {order['orderId']}")
        print(f"Status: {order['status']}")
        print(f"Executed Qty: {order['executedQty']}")

    except Exception as e:
        print(f"\n Error: {str(e)}")

if __name__ == "__main__":
    main()