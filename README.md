# Jupyter Copilot in CML with Self-Hosted LLM

[Jupyter-AI](https://github.com/jupyterlab/jupyter-ai) Copilot, a cutting-edge extension for Jupyter Notebooks, represents a significant advancement by leveraging LLM to provide intelligent code assistance. When deployed in an air-gapped environment where systems are isolated from external networks, Jupyter Copilot with self-hosted LLMs offers unique advantages and technical considerations that are critical for secure environment. Additionally, this solution is ideal for users who prefer not to incur costs with AI managed-service provider :)

<img width="779" alt="image" src="https://github.com/user-attachments/assets/cbb7bfb3-81c0-4e8a-be3d-dd1bb11ef588">

vLLM includes an HTTP server that supports OpenAI’s Completions and Chat APIs. To interact with this server, you can use the official OpenAI Python client library or any other HTTP client. Since Jupyter-AI utilizes the OpenAI API, vLLM can be employed to replicate this connection, enabling Jupyter-AI to work with the vLLM server as a substitute. Behind the scenes, the backend LLM serving the requests through vLLM is powered by OpenHermes2.5-7B model.

## Procedure

**Step 1**: Create a new CML project, open a CML session, clone the model from the HF github.

```
git clone https://huggingface.co/teknium/OpenHermes-2-Mistral-7B
```

**Step 2**:  Deploy [vLLM](https://docs.vllm.ai/en/latest/getting_started/installation.html).

```
pip install vllm
```

**Step 3**:  In the same project, set up a CML application using a CUDA runtime image and execute the provided sample code. Keep in mind that the cloned image folder has been renamed to `gpt-3.5-turbo` because Jupyter-AI is specifically programmed to recognize only the model provided by OPENAI. Renaming the model is a clever workaround :)

```
import os

DASHBOARD_PORT = os.environ['CDSW_READONLY_PORT']
CDSW_APP_PORT=os.environ['CDSW_APP_PORT'] 

os.system("python -m vllm.entrypoints.openai.api_server --host=127.0.0.1 --model=gpt-3.5-turbo --port=$CDSW_APP_PORT > openai.log 2>&1 &")
```

<img width="1440" alt="image" src="https://github.com/dennislee22/copilot-cml-localmodel/assets/35444414/42ace8f9-ea65-43b3-a663-c992cc82e61e">

**Step 4**:  Create a new user CML project. This project will be used by data scientist who needs Jupyter-AI Copilot. Add a new environment variable as follows.

<img width="1434" alt="image" src="https://github.com/dennislee22/copilot-cml-localmodel/assets/35444414/06f82b6b-e749-41b6-be96-da01bf2691e8">

**Step 5**:  Open a CML session, deploy the associated `jupyter_ai` libraries.

```
cdsw@amd942yvvgm8521k:~$ pip list | grep jupyter
jupyter_ai                    2.18.1
jupyter_ai_magics             2.18.1
jupyter_client                8.6.2
jupyter_core                  5.3.0
jupyter-events                0.10.0
jupyter-lsp                   2.1.0
jupyter_server                2.14.1
jupyter_server_fileid         0.9.0
jupyter-server-mathjax        0.2.6
jupyter_server_terminals      0.5.3
jupyter_server_ydoc           0.6.1
jupyter-ydoc                  0.2.4
jupyterlab                    4.2.3
jupyterlab-git                0.41.0
jupyterlab-lsp                4.1.0
jupyterlab-pygments           0.2.2
jupyterlab_server             2.27.2
jupyterlab_widgets            3.0.11
```

**Step 6**:  Configure Jupyter extension `Jupyternaut` with the exposed vLLM URL in step 3.

<img width="1439" alt="image" src="https://github.com/dennislee22/copilot-cml-localmodel/assets/35444414/11e0ee38-e467-44b8-b677-19e591a5156c">

**Step 7**:  Jupyter Copilot is now ready!

<img width="1438" alt="image" src="https://github.com/dennislee22/copilot-cml-localmodel/assets/35444414/0273ce22-2cb3-4cf5-a148-7be371dfad45">



