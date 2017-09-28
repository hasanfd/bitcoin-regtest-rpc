# bitcoin-regtest-rpc

# build
docker build -t mybitcoind .

# run
docker run -p 127.0.0.1:18332:18332 -dit mybitcoind

You can access bitcoin blockchain in docker through port 18332 by using RPC calls(check out https://github.com/jgarzik/python-bitcoinrpc).
