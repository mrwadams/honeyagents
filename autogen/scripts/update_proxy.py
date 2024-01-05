import csv

# File paths
conf_file_path = '/etc/nginx/conf.d/default.conf'
csv_file_path = '/var/bad_ips.csv'

# Placeholder in the conf file
placeholder = '# DENY_IPs'

# Read IPs from CSV
with open(csv_file_path, newline='') as csvfile:
    ips = [row[0] for row in csv.reader(csvfile)]

# Generate the NGINX deny rules
deny_rules = '\n'.join([f'deny {ip};' for ip in ips])

# Replace the placeholder in the conf file
with open(conf_file_path, 'r') as file:
    conf_content = file.read()

conf_content = conf_content.replace(placeholder, deny_rules)

# Write the updated content back to the conf file
with open(conf_file_path, 'w') as file:
    file.write(conf_content)

print("NGINX configuration updated with denied IPs.")


# Restart reverse proxy container to apply updated rules
import docker

client = docker.from_env()
container = client.containers.get('nginx')

# Execute the NGINX reload command within the container
container.exec_run("nginx -s reload")

print("NGINX reload complete.")