# crispy-potato
### Goal 
The aim of this project is to create a simple web page where users can input a keyword (e.g., "iPhone" or "buy iPhone"). The application will then scrape the Google search result page to identify the first shopping ad related to that keyword and display its details. The scraped information should then be converted into an audio file using text-to-speech technology and played back to the user.

To scrape the Google search page, I have used <a href="https://serpapi.com/">serpapi</a>, which makes scraping Google's SERP (Search Engine Results Page) easy.

### Tech Stack Used:
#### client-side: 
Javascript, React.js
#### server-side:
Python, Flask

###  How to Install and Run the Project
1. Click the Copy button to copy the URL of the repository to your clipboard.
2. Open your terminal and navigate to the directory where you want to clone the repository.
3. Type the following command:
```
 git clone <URL>
```
4. Open code-editor (like vs-code)
5. Run the below code in the terminal after opening the project directory (client-side folder) to install all the dependencies and packages required in this project.
```
npm install
```
6. Before running the client-side code, we first need to run the server-side code so that when we send the request, we get the response which is only possible if server is running.
7. To install, all the dependencies in the server-side code, we need to run the below code after opening the project directory (server-side folder).
```
pip install -r requirements.txt
```
8. Now we first run our server-side code.
```
python <filename.py>   # in our case is "python api.py"
```
9. Now, we run the client-side code.
```
npm start
```

### Some screenshot of the final result
