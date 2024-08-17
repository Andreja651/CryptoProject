import asyncio
from decimal import Decimal

import httpx
from Wallet.Service.cryptocurrencyWallet_service import CryptocurrencyWalletService

from config import Config


class COINAPIService:

    @staticmethod
    async def get_portfolio_value(self, user_id, currency):
        """
        Calculates the portfolio value
        :param self:
        :param user_id: the user
        :param currency: the passed currency
        :return: the sum of the portfolio value
        """
        try:
            wallets = await fetch_wallets_from_db(user_id)
            total_portfolio_value = Decimal(0.0)
            portfolio_values = dict()
            async with httpx.AsyncClient() as client:
                tasks = [
                    self.fetch_wallet_value(self=self, client=client, wallet=wallet, currency=currency)
                    for wallet in wallets
                ]
                results = await asyncio.gather(*tasks)
            total_portfolio_value += sum(results)

            return total_portfolio_value

        except Exception as e:
            raise e

    @staticmethod
    async def fetch_wallet_value(self, client, wallet, currency):
        """
        Calculates the wallet value with the crypto value info
        :param self:
        :param client: The client that executes the async task
        :param wallet: The Wallet to calculate value for
        :param currency: The Currency it calculates with
        :return: The Wallet value decimal
        """
        symbol_id = wallet.currency
        quantity = Decimal(wallet.balance)

        response = await self.get_crypto_info(client=client, symbol_id=symbol_id, currency=currency)
        if response.status_code == 200:
            data = response.json()
            current_price = Decimal(data.get('rate', 0.0))
            return {'wallet': wallet, 'value': quantity * current_price, 'currency': currency}
        return {'wallet': wallet, 'value': Decimal(0.00), 'currency': currency}

    @staticmethod
    async def get_crypto_info(client, symbol_id, currency='USD'):
        """
        Fetches the Value of the Crypto Currency
        :param client: The client that executes the async task
        :param symbol_id: The Wallet Currency
        :param currency: The Currency for fetching value on the CoinAPI
        :return: The response from the COINAPI
        """
        try:
            response = await client.get(Config.COIN_API_ENDPOINT.format(symbol_id, currency),
                                        headers={'X-CoinAPI-Key': Config.COIN_API_KEY})
            return response
        except Exception as e:
            raise e


async def fetch_wallets_from_db(user_id):
    return CryptocurrencyWalletService.get_wallets_by_user(user_id)
