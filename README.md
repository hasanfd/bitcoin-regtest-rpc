# bitcoin-regtest

# build
docker build -t mybitcoind .

# run
docker run -p 127.0.0.1:18332:18332 -dit mybitcoind
