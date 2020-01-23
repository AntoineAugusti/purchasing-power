# Archive purchasing power parity
Archive daily data from [https://purchasing-power-parity.com](purchasing-power-parity.com).

The data is archived in the _[data](data/)_ folder.

Example data for a specific country, India:

```json
{
   "ppp":{
      "countryCodeIsoAlpha2":"ID",
      "currenciesCountry":[
         {
            "code":"IDR",
            "name":"Indonesian rupiah",
            "symbol":"Rp"
         }
      ],
      "countryCodeIsoAlpha3":"IDN",
      "currencyMain":{
         "exchangeRate":13636.812433,
         "code":"IDR",
         "name":"Indonesian rupiah",
         "symbol":"Rp"
      },
      "ppp":4305.98,
      "pppConversionFactor":0.3157614744029089
   }
}
```

The important key is `pppConversionFactor`. Use this value to convert a price from USD to a USD price in another country. You can convert this amount to another currency using the exchange rate.

## Purchasing power parity?

In the US, the average price for a cappuccino is $4.00. This doesn't mean that everyone around the world can afford it. Considering purchasing power parity, the same cappuccino should cost $1.26 in Indonesia.
