# bitcoin-regtest

# build
docker build -t mybitcoind .

# run
docker run -p 127.0.0.1:18332:18332 -dit mybitcoind

You can access bitcoin blockchain inside docker through port 18332 by using RPC calls(like https://github.com/jgarzik/python-bitcoinrpc).
