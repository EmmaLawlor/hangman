## Helpful tools

Markdown's not all that easy so sometimes you may want to use some tools to make tables. 

- [Markdown Cheatsheet](https://guides.github.com/features/mastering-markdown/)
- [markdown table generator](https://www.tablesgenerator.com/markdown_tables) - used to help with documentation table formatting
- [mardown table of contents generator](https://ecotrust-canada.github.io/markdown-toc/) - used to create table of contents (be weary it does have some bugs if you have dashes or trailing spaces in your headers)
- [readme.so](https://readme.so/) - if you don't want to learn markdown, this tool might help you

# Table of Contents
Copy your readme to http://ecotrust-canada.github.io/markdown-toc/ to make a table of contents.  This will help assessors to see the structure of your readme. Just test it out ast this tool isn't perfect. It tends to mess up with special characters like dashes.

====================================== The Sections you Fill in are below ==============================

# PROJECT NAME
Hangman

## Author
Emma Lawlor

## Project Overview
A simple interactive hangman game, written in Python. This game randomly chooses a word from a list of words. The user is then prompted to guess the letters of the word, or the word itself, until they have correctly guessed the word or until they run out of lives. Each incorrect answer adds to the hangman image, with the game ending when the hangman has been fully completed. 

![Google Chrome - Python Terminal by Code Institute - Google Chrome](https://user-images.githubusercontent.com/84344402/135355526-41012bfc-9773-4a9c-8ed8-eb6079be6303.gif)

Deployed Site:
https://hangman-emma-lawlor.herokuapp.com/

## Table of Contents
Generate after readme is complete for UX and below

## How To Play/Use
Paragraph or bullet points of how the user initiates the program and interfaces with it. You could have videos of each bit if you want and ditact what the user should do.

## Features

### Implemented Features
- Start of game: On visiting the site, the user is greeted witha "Let's Play Hangman" message as well as an empty hangman image and the entire word represented by dashes, since the user has not yet made any guesses. The user is also prompted to guess a letter by asking for input "Choose a letter:"

![image](https://user-images.githubusercontent.com/84344402/135350017-8529ced5-17c1-4ebe-9009-3a3c2b53ef5d.png)

- Input Validation: The user's chosen letter is checked against a number of conditions. 
  - If input is invalid, the user is alerted and promplted to choose again
  
  ![image](https://user-images.githubusercontent.com/84344402/135350370-d13a8a78-d68c-4792-b08d-ee769673100d.png)#
  
  - If the user correctly chooses a letter in the word, text is displayed green and the dashes in the word are replaced with the correct letter as appropriate
  
  ![image](https://user-images.githubusercontent.com/84344402/135350606-1b86aa18-a49f-482e-94cc-34b08bbf8e95.png)
  
  - If the user chooses a letter which is not in the word, the text is displayed in red and the hangman image is updated to the next stage indicating the loss of a life
  
  ![image](https://user-images.githubusercontent.com/84344402/135350767-0ed0d1c3-6a91-43cb-8c1c-d5201f0b4d88.png)
  
  - If the user chooses a letter that they have already guessed, they are asked to try again without the loss of an extra life
  
  ![image](https://user-images.githubusercontent.com/84344402/135351977-6df1edce-dbe8-4ae8-8567-6b31ff5c33b9.png)

- End of Game:
  - If the user has coorrectly completed the word or guessed the word, they get a congratulations message in green text and are asked if they want to play again
  
  ![image](https://user-images.githubusercontent.com/84344402/135351418-5d434ad0-9fcd-4995-b86b-4afb0ea45472.png)
  
  - If the user fails to guess the word correctly, they get a game over message in red text and are again asked if they would like to play again
  
  ![image](https://user-images.githubusercontent.com/84344402/135351558-030edaa5-2956-44fb-b69e-3fda96f1a665.png)

  - If the user chooses not to play the game their result is displayed in terms of number of games won out of number of games played
  
  ![image](https://user-images.githubusercontent.com/84344402/135351720-14d29960-a874-4f58-ad78-34bb79e5afbc.png)

### Future Features

- Score Tracking: By linking with Google Sheets, the game could ask the user for their name and email address, store their score details and email them a copy of their results upon exiting the game. 

## Design Documents

- In the early planning stages, a flowchart was drawn up to help visualise the setps required to create a functioning hangman game. 
- This chart was helpful to the developer when creating functions as the logic of the game was clearly broken down into simple steps.
- [This flowchart](https://1drv.ms/b/s!AtrJulJDGsm2qFf5wKQGuJDN1MRH) was created using [Lucidchart](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier1_mixed_search_brand_exact_&km_CPC_CampaignId=1490375427&km_CPC_AdGroupID=55688909257&km_CPC_Keyword=lucidcharts&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433236001&km_CPC_TargetID=aud-826163889020:kwd-84176206937&km_CPC_Country=20483&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&mkwid=sMDuh5elr_pcrid_442433236001_pkw_lucidcharts_pmt_e_pdv_c_slid__pgrid_55688909257_ptaid_aud-826163889020:kwd-84176206937_&gclid=Cj0KCQjw1ouKBhC5ARIsAHXNMI-XHJRavE5VCyXoRZMUJrufGkLIFrq_iz1oKO4xAXMed81uEqSRagMaAsA5EALw_wcB)
![image](https://user-images.githubusercontent.com/84344402/133690510-8f1d770e-ccfe-4bea-908d-a1321736cb1d.png)

## Data Model

The class 'Hangman' is used as the data model for the game. 

The __init__ method initialises the following attributes for use in all instances of the class:
- self.word: uses the random method to choose a random word from the provided list in the words.py file. This is the word used for gameplay, which the user will try to decipher by guessing letters.
- self.stage: Used to display the correct version of the 'Hangman' image. The stage is incremented by 1 each time the user enters an incorrect letter, therefore displaying the next stage of the hangman each time an incorrect letter is entered.
- self.guessed_letters: An empty list, to which all letters guessed by the user throughout the course of a game are added. This list is vital in gameplay, as it allows us to check if the user has already guessed the letter. If the letter has already been guessed, the user is advised of this and is asked to choose again. 
- self.guessed_words: As with guessed_words, this starts as an empty list. If the user chooses to guess an entire word, it is then added to this list. If they guess another word, this list is used to check if the wprd has already been guessed. 
- self.games_played: Starting at 0, this number is increased by 1 each time the user completes a game. 
- self.games_won: Again starting at 0, this is increased by 1 each time the user correctly completes the word and wins the game. A combination of games_played and games_won are used to return the user's overall result for the session when they choose to exit the game.  


## Libraries used
- Random module imported to allow the program to select a random word from the words.py file for use in gameplay. 
- Colorama module imported to allow styling and coloring of text displayed to the user in the terminal. This was used to enhance the user's experience and make the game more visually attractive. 
  - The main game text is yellow, with the hangman image and dashes representing letters are cyan.
  
  ![image](https://user-images.githubusercontent.com/84344402/135340001-b1b364be-b163-4216-813a-1d4fc6b1bc8b.png)
  
  - An incorrect guess is displayed in red text
  
  ![image](https://user-images.githubusercontent.com/84344402/135340201-dea4916c-4c58-4a36-b3d0-005642b6ed8a.png)
  
  - A correct guess is displayed in green text 
  
  ![image](https://user-images.githubusercontent.com/84344402/135340338-d41dc63d-e160-4aef-a1e5-3b8c1be07ae3.png)

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your features and ensure that they all work as intended in an easy and straightforward way for the users to achieve their goals.

### Validation Testing
You should try to ensure you code is valid and follows proper indentation.  In this section you should write up any websites you used to validate your code. As your projects becomes more complex these tools may change.

- [PEP8 Validator](http://pep8online.com/) include a screenshot of results

If the line is too long just add 
```$python 
# noqa
```
There is a space before the # and after it to skip the quality assurance for that line.

### Manual Testing

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Startup:
    1. User enters name
    2. try to submit no entry, blank name not allowed
    3. Try to submit the name with spaces
    4. Try to submit the name as special characters
    5. Try to submit the name as calling a function in the code
   
    
Here is a [Manual Testing Template](https://docs.google.com/spreadsheets/d/189VpSeEG9oevSRhvb2WZl8zCk9L3s2iWQyrJ_1jjAGQ/edit?usp=sharing) that you can use as a starting point to keep track of your testing efforts. Make a copy of it in your own account and update as needed to reflect the browsers you are testing and features.  

Or you could open a Project in github and write your tests there in a basic khanban board. 
1. Click on the projects menu:

![image](https://user-images.githubusercontent.com/23039742/132130197-465d3db9-04e0-4843-9509-041cd0639551.png)

2. Click on the create project button:

![image](https://user-images.githubusercontent.com/23039742/132130216-1623af38-827f-4fd6-9729-c9bc5a1e5485.png)

3. Select the Basic Kanban template

![image](https://user-images.githubusercontent.com/23039742/132130414-4e60b081-555f-49e3-a446-da6fc88951f2.png)

4. Fill in the information and click Create

![image](https://user-images.githubusercontent.com/23039742/132130417-f6051c42-4a1d-4faf-8ed7-780215d1805d.png)

4. Click the + sign on the project board to craete a new Test

![image](https://user-images.githubusercontent.com/23039742/132130433-dcb741ac-9deb-401a-8801-6e3d1861c7f7.png)

5. You can use the templates provided to steal the checkbox mardown to write out your test by clicking the ... button and selecting edit note option:

![image](https://user-images.githubusercontent.com/23039742/132130460-2314a026-ed12-493c-a4e9-16726e812b94.png)

6. Just copy the example text you want:

![image](https://user-images.githubusercontent.com/23039742/132130503-d4611154-d62b-4eff-9ec5-004fd89f440e.png)

7. Then you can past that into your new note and update as needed then save:

![image](https://user-images.githubusercontent.com/23039742/132130729-161ff2e6-65c0-4344-a4d4-e3baf4670a24.png)

8. Then when you start to test, just move it into progress and update as you finish the tasks in your test.  If you've used checkboxes to track the testing tasks, you should mark them off and then once all are done, you can move the item to the done list.

There are ways to create issues with these project cards so you don't have to write up everything. You can create an issue from a test item. 

For more information you can visit: https://docs.github.com/en/issues/organizing-your-work-with-project-boards/managing-project-boards/about-project-boards 


### Defect Tracking

### Defects of Note
- Any defects which occurred during development were tracked using the GitHub Issues section of this repository, which can be found [here](https://github.com/EmmaLawlor/hangman/issues).
- Details of each bug were noted as they were discovered, with screenshots taken to demonstrate the problem where possible.
- The GitHub Issues section allowed for closeout of defects as they were rectified, again using screenshots to show the solution when possible.
- 
### Outstanding Defects
- No outstanding defects have been noted. 

## Deployment

### Heroku
This project runs in the Code Institute provided Python Terminal simulator. The project repository is hosted on GitHub and was deployed to Heroku using the following steps:
1. From the Heroku dashboard, choose New > Create new app
![image](https://user-images.githubusercontent.com/84344402/134727186-9f0dfafc-5120-44cc-9209-90eb034a0a79.png)

2. In the app name field, enter a unique name for the app. Choose the region (Europe) and select 'Create App'
![image](https://user-images.githubusercontent.com/84344402/134727452-cd6a98e8-707b-47d4-a5be-308a98686927.png)

3. Click on the 'Settings' tab
![image](https://user-images.githubusercontent.com/84344402/134727805-094eda93-7cc2-4706-8502-90328cc18646.png)

4. Select 'Add buildpack'
![image](https://user-images.githubusercontent.com/84344402/134728080-e2b67f15-3e4c-42e0-9cad-69541ae922ee.png)

5. First, choose Python and click 'Save changes'
![image](https://user-images.githubusercontent.com/84344402/134728146-26f39c89-8747-419d-bc7f-406181bbe576.png)

6. Next, select nodejs and again click 'Save changes'
![image](https://user-images.githubusercontent.com/84344402/134728191-63929f98-654c-43a4-a732-e98563b7ec66.png)

7. Select the 'Deploy' tab
![image](https://user-images.githubusercontent.com/84344402/134728674-3b2737d8-3d12-4ef8-917f-086cc792b03d.png)

8. Click 'GitHub'
![image](https://user-images.githubusercontent.com/84344402/134729055-02112055-ae23-4c5d-97e9-5a8aaad1891c.png)

9. Enter the name of the repository and click search
![image](https://user-images.githubusercontent.com/84344402/134729099-5b68a72f-f0c8-49ab-bd55-ad6db45a664c.png)

10. Select the branch of the project for deployment ('Main' in this case)
![image](https://user-images.githubusercontent.com/84344402/134729273-a8fb68eb-d0cc-4331-b958-363b7de96d52.png)

11. In the 'Manual Deploy' section, click 'Deploy'
![image](https://user-images.githubusercontent.com/84344402/134729383-70980a37-810a-4161-976b-3e6663a30b1d.png)

12. When app has been deployed successfully, the page updates with a link to view the app
![image](https://user-images.githubusercontent.com/84344402/134729634-35e5c778-0071-4747-b72a-37491f01981a.png)

## Credits

-[Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
    - The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.

### Content

- List of random words generate using [Random Word Generator](https://randomwordgenerator.com/)
- Stages of hangman taken from (https://inventwithpython.com/invent4thed/chapter8.html)

### Media

Make a list of sites you used images from. If you used several sites try to match up each image to the correct site. This includes attribution for icons if they came from font awesome or other sites, give them credit.

### Acknowledgments

- Code for replacing underscores with correct letter guesses adapted from [this tutorial](https://github.com/kiteco/python-youtube-code/blob/master/build-hangman-in-python/hangman.py)
