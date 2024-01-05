import autogen


config_list = autogen.config_list_from_dotenv(
    dotenv_file_path="/usr/src/app/.env",
    filter_dict={
        "model": {
            "gpt-4-1106-preview",
        #    "gpt-4",
        #    "gpt-3.5-turbo",
        }
    },
)

# create an AssistantAgent named "assistant"
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={
        "cache_seed": 42,  # seed for caching and reproducibility
        "config_list": config_list,  # a list of OpenAI API configurations
        "temperature": 0,  # temperature for sampling
    },  # configuration for autogen's enhanced inference API which is compatible with OpenAI API
)
# create a UserProxyAgent instance named "user_proxy"
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": "coding",
        "use_docker": "python:3",  # set to True or image name like "python:3" to use docker
    },
)
# the assistant receives a message from the user_proxy, which contains the task description
user_proxy.initiate_chat(
    assistant,
    message="""Your task:
    1. Review the contents of the honeypot logs in the /var/log/cowrie/cowrie_logs.txt
    2. List the IP addresses that have connected to the honeypot
    3. Use a Python script to save a de-duplicated list of the IPs you identify to the following CSV file /var/bad_ips.csv
    4. Run /usr/src/app/update_proxy.py to update the configuration of the reverse proxy to block the identified IPs
    5. As a Senior Threat Intelligence analyst, analyse the cowrie_logs.txt to determine the actions taken by the attacker while connected to the honeypot.
    6. Use your analysis to write a comprehensive Threat Intelligence report for management. The report should detail your analysis of the activity detected in the honeypot, including the IP addresses identifued and any actions taken by an attacker while connected to the honeypot. You should also document the subsequent actions you took to mitigate the potential threat. Use Markdown to format the document and save it to /var/report.md

    Note: Exclude 172.18.0.3 from your analysis. It's the IP address of the honeypot.
    """,
)