from web3 import Web3
import pandas as pd

# Connect to Ethereum using Infura
infura_url = 'https://mainnet.infura.io/v3/your_project_id'
web3 = Web3(Web3.HTTPProvider(infura_url))

# Verify connection
if web3.is_connected():
    print("Connected to Ethereum")
else:
    print("Failed to connect to Ethereum")
    exit()

# ERC-20 Token Contract Address and ABI
token_contract_address = 'Token_address'
token_abi = """contract_abi"""

# Create contract object
contract = web3.eth.contract(address=token_contract_address, abi=token_abi)

# Block number for snapshot
block_number = 18652536

latest_block = web3.eth.get_block('latest').number
print(f"Latest block number: {latest_block}")

# List of token holder addresses (this needs to be provided or obtained)
holder_addresses = ['list_of_holders']
# Fetch balances and prepare data
holder_data = []
for address in holder_addresses:
    balance = contract.functions.balanceOf(Web3.to_checksum_address(address)).call(block_identifier=block_number)
    holder_data.append({'address': address, 'balance': balance})

# Convert to DataFrame
df = pd.DataFrame(holder_data)

# Export to CSV
df.to_csv('holders_snapshot.csv', index=False)

print("Snapshot created successfully.")
