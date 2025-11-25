# CSFloat Async API Client (Unofficial)

An **unofficial**, **asynchronous** Python library for interacting with the [CSFloat](https://csfloat.com) API. This library provides full support for programmatic access to listings, buy orders, user data, exchange rates, and more. All prices returned by the server are in **cents**.

## Key Features

* **Asynchronous design**: Built on `aiohttp` for non-blocking I/O.
* **Fetch listings**: Retrieve detailed listings with filters (price in cents, float, rarity, etc.).
* **Buy orders**: Get and manage buy orders for specific items.
* **User information**: Access your own profile, trades, and stall data.
* **Listing management**: Create, delete, and modify listings and buy orders.
* **Proxy support**: Optional SOCKS4/5 and HTTP(S) proxy support.
* **Error handling**: Clear exceptions with descriptive messages.

## Installation

Install via pip:

```bash
pip install csfloat_api
```

## Quick Start

```python
import asyncio
from csfloat_api.csfloat_client import Client

async def main():
    async with Client(api_key="YOUR_API_KEY") as client:
        # Fetch up to 50 listings priced between $1.00 and $10.00 (i.e., 100–1000 cents)
        listings = await client.get_all_listings(min_price=100, max_price=1000)
        for listing in listings["listings"]:
            print(f"ID: {listing.id}, Price: {listing.price} cents, Float: {listing.item.float_value}")

        # Create a buy order for an item
        buy_order = await client.create_buy_order(
            market_hash_name="AK-47 | Redline (Field-Tested)",
            max_price=5000,  # 5000 cents = $50.00
            quantity=1
        )
        print(buy_order)

asyncio.run(main())
```

## Session Management

The `Client` class manages an underlying HTTP session using `aiohttp.ClientSession`. To ensure that resources are properly released, it is important to close the session when you are done using the client.

### Using `async with`

The recommended way to use the `Client` is with an `async with` statement, which automatically closes the session when the block is exited:

```python
async with Client(api_key="YOUR_API_KEY") as client:
    # Use the client...
```

### Manual Session Closing

If you cannot use `async with`, you can manually close the session using the `close` method:

```python
client = Client(api_key="YOUR_API_KEY")
try:
    # Use the client...
finally:
    await client.close()
```

Failing to close the session may result in warnings about unclosed client sessions and potential resource leaks.

## Core Methods

### Meta
* `get_exchange_rates()` - Retrieve current exchange rates.
* `get_location()` - Get detected location metadata.

### Account
* `get_me(raw_response=False)` - Fetch authenticated user profile.
* `get_account_standing()` - Retrieve account standing details.
* `get_transactions(page=0, limit=10)` - Get your transaction history.

### Trades and Offers
* `get_pending_trades(limit=500, page=0)` - List pending trades.
* `get_trades(states, limit=500, page=0)` - List trades filtered by state.
* `get_trade_history(role="seller", limit=30, page=0)` - List completed, failed, or cancelled trades.
* `get_offers(limit=40)` - Fetch your offers timeline.
* `accept_sale(trade_ids)` - Accept one or more sales.

### Listings (Browse)
* `get_all_listings(...)` - List items with optional filters (prices in cents).
* `get_specific_listing(listing_id, raw_response=False)` - Get detailed info for a specific listing.
* `get_similar(listing_id, raw_response=False)` - Find listings similar to a given listing.
* `get_sales(market_hash_name, paint_index=None)` - Retrieve historical sales for an item.
* `get_stall(user_id, limit=40, raw_response=False)` - Get a user's stall (listed items).

### Inventory and Watchlist
* `get_inventory()` - Retrieve your inventory.
* `get_watchlist(limit=40)` - Retrieve your watchlist.
* `delete_watchlist(id)` - Remove a listing from your watchlist.

### Listing Management
* `create_listing(asset_id, price, ...)` - Create a new listing (price in cents).
* `update_listing_price(listing_id, price)` - Update a listing price.
* `delete_listing(listing_id)` - Remove an existing listing.
* `make_offer(listing_id, price)` - Make an offer on a listing.
* `buy_now(total_price, listing_id)` - Instantly buy one or more listings.

### Buy Orders
* `get_buy_orders(listing_id, limit=10, raw_response=False)` - Retrieve buy orders for a listing.
* `get_my_buy_orders(page=0, limit=10)` - List your own buy orders.
* `create_buy_order(market_hash_name, max_price, quantity)` - Place a buy order.
* `delete_buy_order(id)` - Cancel an existing buy order.

For detailed parameters and return types, refer to `csfloat_client.py`.

## Proxy Support

Optionally provide a proxy URL in the constructor:

```python
client = Client(
    api_key="YOUR_API_KEY",
    proxy="socks5://user:pass@host:port"
)
```

## Error Handling

The client raises exceptions for HTTP errors with clear messages:

* **401** Unauthorized – Invalid API key.
* **404** Not Found – Resource missing.
* **429** Too Many Requests – Rate limit exceeded.
* **500** Internal Server Error – Server-side issue.

## Contributing

Contributions are welcome! Please submit issues and pull requests on the [GitHub repository](https://github.com/Rushifakami/csfloat_api).

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
