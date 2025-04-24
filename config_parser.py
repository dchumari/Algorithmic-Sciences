import os

def parse_config():
    return {
        'linuxpath': os.getenv('LINUXPATH', '200k.txt'),
        'REREAD_ON_QUERY': os.getenv('REREAD_ON_QUERY', 'False').lower() == 'true'
    }