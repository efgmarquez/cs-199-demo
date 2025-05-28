# CS 199 Demo
This is the demo website of Paolo De los Santos and Ellian Marquez's CS 199 undergraduate thesis project named **"Misinformation Representation and Machine Unlearning
Mechanics in Large Language Models (LLMs)"**. In this app, we aim to give a high level overview of what our study is and what sparse crosscoders can do. This includes: steering a feature, seeing features' interpretations, analysis, and even our data.

For added interactivity, we have a **feature steering** feature in the website where you can steer a fake news-containing vector in the model's activation layers in order to ablate or strengthen fake news in the model. Interestingly, you can see how a model changes its answer based on how you control this "fake" vector

## Run local
```streamlit run streamlit_app.py``` 

Note: Since this is being run locally, the model might take a long time to load or generate answers. We recommend to change the device in the code to gpu as cpu may be extremely inefficient for transformer models like ours. 

## Study Abstract
This study investigates how misinformation is internally represented and unlearned in Large Language Models (LLMs). Using sparse crosscoders, we analyze feature dynamics across a multi-phase pipeline of contamination and unlearning using gradient ascent. We find that fake news is not encoded in isolated features, but is deeply entangled with real content—making targeted removal difficult. Despite this, crosscoders decompose entangled features into interpretable latents, enabling precise diagnosis of representational shifts. Our experiments show that gradient ascent robustly deletes harmful features: attempts to reactivate misinformation via feature steering failed. These findings support crosscoders as a diagnostic tool and gradient ascent as a durable unlearning method. This work contributes a new framework for auditing safety interventions and understanding internal knowledge structures in LLMs.

## Acknowledgments
We are advised by Mr. Paul Regonia (UP DCS CVMIL) and Mr. Kyle Reynoso (WhiteBox Research). Thank you so much for your guidance in our study and in this app.
