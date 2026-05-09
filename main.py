import os

def setup_marketing_env():
    directories = ['data', 'outputs', 'figures']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
    print("Marketing Analytics Environment is ready.")

if __name__ == "__main__":
    setup_marketing_env()