# Systems Design

Crypto price alert system.

## Requirements

- Handle multiple tickers
- Real time data feed
- trigger events on various scenarios
- Action events - when specific stock price indicaters/metrics happen events will be triggered

## Thoughts

Initially single monolith arch, can move to distributed down the line. want a fronted ui in simple JS, CSS and HTML, uses can input stock tickers and will stream data. Users can set certain trigger events.

### Key Components

- API to handle calling/streaming stock price data.
- Event driven architecture.
- need statistical analysis - maybe risk metrics for alerts on when to sell or buy. Need to research this part, but need it extensible to add new metrics etc. over time.

Multithreaded streaming? For streaming multiple tickers etc?

Going to change to crypto price alerting. Move into algo trading crypto currencies. Incorporate sentiment analysis on different tickers.
