from bitcoinrpc.authproxy import AuthServiceProxy

#check bitcoin.conf
rpc_user = 'test'
rpc_password = 'test'
rpc_port = '18332'

rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:%s"%(rpc_user, rpc_password,rpc_port))
#generate some blocks
rpc_connection.generate(101)

balance = rpc_connection.getbalance()

print('balance: ',balance)

#get best block hash
blockhash = rpc_connection.getbestblockhash()
block = rpc_connection.getblock(blockhash)

print('last block: ',block)
