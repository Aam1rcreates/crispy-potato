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

### Some screenshots of the final result
<br>
Here's our first page: 
<br>

![page1](https://github.com/Aam1rcreates/crispy-potato/assets/68699410/84216059-767f-4bd2-bc13-8b39b31e2004)
<br>
<br>

Now, Let's search "mouse" and see what's result looks like:
<br>
![page2](https://github.com/Aam1rcreates/crispy-potato/assets/68699410/5d44a6a2-34c7-45f9-a2f9-62c923cc53e2)
<br>
<br>

Let's search for something for which there wouldn't be any result
<br>
![page3](https://github.com/Aam1rcreates/crispy-potato/assets/68699410/8be7d214-9b43-49da-9be3-be1e4e4d6264)
<br>
<br>


![page5](https://github.com/Aam1rcreates/crispy-potato/assets/68699410/e120ee17-8efb-451f-944d-f5ec55c5d750)









