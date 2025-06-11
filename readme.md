<h1>Build a Google Rank Checker</h1>

<h2>Watch the full tutorial on my YouTube Channel</h2>
<div>

<a href="https://youtu.be/c5jHhMXmXyo">
    <img src="thumbnail_small.png" alt="Thomas Janssen Youtube" width="200"/>
</a>
</div>

<h2>Prerequisites</h2>
<ul>
  <li>Python 3.11+</li>
</ul>

<h2>Installation</h2>
<h3>1. Clone the repository:</h3>

```
git clone https://github.com/ThomasJanssen-tech/Google-Rank-Checker
cd Google-Rank-Checker
```

<h3>2. Create a virtual environment</h3>

```
python -m venv venv
```

<h3>3. Activate the virtual environment</h3>

```
venv\Scripts\Activate
(or on Mac): source venv/bin/activate
```

<h3>4. Install libraries</h3>

```
pip install -r requirements.txt
```

<h3>5. Configuration</h3>
<ul>
<li>Rename the .env.example file to .env</li>
<li>Get your $15 Bright Data credits: https://brdta.com/tomstechacademy</li>
<li>Add your Bright Data API key</li>
<li>Add GOOGLE_COUNTRY (e.g. US or NL) in the .env file to indicate in which country you want to check results</li>
<li>Add WEBSITE_URL (e.g. pizzahut.com) in the .env file to indicate for which website you want to check results</li>
<li>Get your Google Service account here: http://gspread.readthedocs.org/en/latest/oauth2.html</li>
<li>Rename the file with credentials to credentials.json and store it in the same folder</li>
</ul>

<h2>Executing the scripts</h2>

- Open a terminal in VS Code

- Execute the following command:

```
python main.py
```

<h2>Further reading:</h2>
<ul>
<li>https://github.com/burnash/gspread</li>
</ul>
