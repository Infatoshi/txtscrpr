# txtscrpr

<img src="./assets/folders.png" alt="Folders" width="300" height="440">

## Purpose
Instead of buying my friend an expensive hardcopy textbook for his birthday, I thought it would be a good idea to write a script that would scrape 1500 textbook pdfs from the internet. This way, he can have access to a wide range of textbooks for free. Lots of other people liked the motivation behind this and wants a way to reproduce the ~15GB of textbooks. So, I decided to make this repo public.

## How to use
```
git clone https://github.com/Infatoshi/txtscrpr.git
cd txtscrpr
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```
Expect roughly 15GB of textbooks to be downloaded to the `topics` directory.
The variable `first_n_results` in main.py can be adjusted. For example, setting `first_n_results = 10` will download the first 10 textbooks from the internet in each subtopic within each topic.
Feel free to edit `topics.json` to include/change/delete more topics and subtopics. It should give you an idea about the topics and subtopics structure.

## Extra
I plan on adding advanced features to this repo (eg. chatting with textbooks via RAG networks, summarizing textbooks, etc.). If you have any ideas, feel free to open an issue or reach out to me. (links at the bottom)

[Map of Engineering](https://twitter.com/DominicWalliman/status/1522525405391036427/photo/1)
Credit goes to *Domain of Science* for the cover image (map of engineering).

## Links
- [Discord](https://discord.gg/893q6n3TB8)
- [LinkedIn](https://www.linkedin.com/in/elliot-arledge-a392b7243/)
- [Twitter](https://twitter.com/elliotarledge)
- [YouTube](https://www.youtube.com/channel/UCjlt_l6MIdxi4KoxuMjhYxg)
- [GitHub](https://www.github.com/Infatoshi)
- [Website](https://elliotarledge.com)
- Email - `elliot@arledge.net`
- Schedule a meeting with me [here](https://calendly.com/elliot-ayxc/60min)