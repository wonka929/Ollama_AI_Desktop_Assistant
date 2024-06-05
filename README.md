# AI for your desktop

### The easy way

This piece of software was born from the necessity for incorporating a bit of artificial intelligence into my PC's daily usage.

The final spark ignites thanks to Microsoft's release of [Phi3]([Tiny but mighty: The Phi-3 small language models with big potential - Source](https://news.microsoft.com/source/features/ai/the-phi-3-small-language-models-with-big-potential/)) which I found to be incredibly impressive given its size. It runs smoothly on both CPU and GPU without causing irritation, making it highly usable during working routines.

II decided to find a way to further integrate this large language model (LLM) into my desktop experience.

As I'm not a programmer, I opted to adapt an existing UI in Python for real-world use with the software. 

While chatbots are indeed cute, their integration into the system often feels lacking.

### Requirements

* Ollama installed on your system. Follow the guide here for your OS [Download Ollama on Linux](https://ollama.com/download/linux)

* Ollama up and running. On Linux should be enough to send a
  `sudo systemctl start ollama.service`

* fire `ollama run phi3:mini-128K` in the terminal to download the Phi3 model to be used in Ollama

* python3 installed on your system. For the UI we will use **tkinter**
  `sudo apt install python3-tk`

* make OllamaAssistant.py file executable

* add a system shortcut to the file

Should be fine.

### How it works

The scipt is pretty self-explanatory.

It uses Ollama APIs to interact directly with the LLM from the desktop.
I bounded my F7 key to run the script.

There are 5 functions right now, but everything is just determinated by the prompt used: 

* Sum up the text

* Explain

* Rewrite

* Grammar Check

* and a input text field to make every other possible thing

* **NEW FEATURE:** RAG (thanks to Phi3-mini-128K or Phi3-medium-128K)

As per default behaviour SumUp, Explain, Rewrite and Check take as input the content of the clipboard.
So while you suft the internet or do your job on documents or else you can just ctrl + c,  F7 and select the function you want the model to perform.

https://github.com/wonka929/Ollama_AI_Desktop_Assistant/assets/14088894/dea8623c-87a3-4a4d-9caa-125241fdc784

Easy peasy. Enjoy.

What I woud add? 

* I couldn't stream the output of the request to the interface word by word but just everything at the end. I'm not sure i can do it differently, it should be an asyncronous behaviour. 

* Find the perfect prompt to make the LLM perform its actions based on the original language of the text copied. I'm still trying to figure out a functioning prompt.

Feel free to contribute. 
As I said I'm not a programmer, pretty sure many of you can improve my ideas.

#### Release notes:

30/04/2024: initial release

02/05/2024: changed the model from phi3 (which is instruct) to phi3:3.8b which is general. In addition i think i've found the correct prompt to use automatically english or italian

03/06/2024: added RAG like feature to use with 128K token lenght with phi3. It is enough fot a 180 pages book more or less.
