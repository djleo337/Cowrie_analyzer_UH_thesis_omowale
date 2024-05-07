import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Data Loading
df = pd.read_json('C:/Users/Workdesk/Desktop/cowrie_analyser/cowrie.json.1', lines=True)

# Step 2: Data Preprocessing
connection_events = df[df['eventid'] == 'cowrie.session.connect']
closed_events = df[df['eventid'] == 'cowrie.session.closed']
client_version_events = df[df['eventid'] == 'cowrie.client.version']
kex_events = df[df['eventid'] == 'cowrie.client.kex']
login_attempts = df[df['eventid'] == 'cowrie.login.failed']

# Step 3: Analysis and Visualization
# Example: Connection Duration Analysis
connection_events['timestamp'] = pd.to_datetime(connection_events['timestamp'])
closed_events['timestamp'] = pd.to_datetime(closed_events['timestamp'])

try:
    #connection_events['duration'] = closed_events['timestamp'] - connection_events['timestamp']
    # Plotting connection duration histogram
    plt.figure(figsize=(8, 6))
    #plt.hist(connection_events['session'].dt.total_seconds().dropna(), bins=10)
    plt.xlabel('session')
    plt.ylabel('Frequency')
    plt.title('Histogram of Connection sessions')
    plt.savefig('Connection_Durations_Histogram.png')  # Save the plot as a picture file
    plt.show()
except ValueError as ve:
    print("Error occurred while calculating connection duration:", ve)

# Example: SSH Client Version Analysis
plt.figure(figsize=(10, 6))
client_versions = client_version_events['version'].value_counts()
client_versions.plot(kind='bar', color='skyblue')
plt.xlabel('SSH Client Version')
plt.ylabel('Frequency')
plt.title('Distribution of SSH Client Versions')
plt.xticks(rotation=30)
plt.savefig('SSH_Client_Versions_Distribution.png')  # Save the plot as a picture file
plt.show()

# Example: Key Exchange Algorithm Analysis
plt.figure(figsize=(10, 6))
key_exchange_algs = kex_events['kexAlgs'].explode().value_counts()
key_exchange_algs.plot(kind='bar', color='salmon')
plt.xlabel('Key Exchange Algorithm')
plt.ylabel('Frequency')
plt.title('Distribution of Key Exchange Algorithms')
plt.xticks(rotation=75)
plt.savefig('Key_Exchange_Algorithms_Distribution.png')  # Save the plot as a picture file
plt.show()

# Example: Failed Username Login Attempts Analysis
plt.figure(figsize=(10, 6))
failed_login_users = login_attempts['username'].value_counts()
failed_login_users.plot(kind='bar', color='orange')
plt.xlabel('Username')
plt.ylabel('Frequency')
plt.title('Distribution of Failed Username Attempts by ')
plt.xticks(rotation=45)
plt.savefig('Failed_Login_Attempts_Distribution.png')  # Save the plot as a picture file
plt.show()

# Example: Failed Password Login Attempts Analysis
plt.figure(figsize=(10, 6))
failed_login_users = login_attempts['password'].value_counts()
failed_login_users.plot(kind='bar', color='orange')
plt.xlabel('Password')
plt.ylabel('Frequency')
plt.title('Distribution of Failed Password Login Attempts by User')
plt.xticks(rotation=45)
plt.savefig('Failed_Password_Attempts_Distribution.png')  # Save the plot as a picture file
plt.show()

# Example: IP Attempts Analysis
plt.figure(figsize=(10, 6))
failed_login_users = login_attempts['src_ip'].value_counts()
failed_login_users.plot(kind='bar', color='orange')
plt.xlabel('src_ip')
plt.ylabel('Frequency')
plt.title('Distribution of IP connection by User')
plt.xticks(rotation=45)
plt.savefig('Failed_ip_connections_Distribution.png')  # Save the plot as a picture file
plt.show()