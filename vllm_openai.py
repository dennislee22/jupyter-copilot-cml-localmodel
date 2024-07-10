import os

DASHBOARD_PORT = os.environ['CDSW_READONLY_PORT']
CDSW_APP_PORT=os.environ['CDSW_APP_PORT'] 

os.system("python -m vllm.entrypoints.openai.api_server --host=127.0.0.1 --model=gpt-3.5-turbo --port=$CDSW_APP_PORT > openai.log 2>&1 &")
