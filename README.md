# PROJECT NAME
Hangman

## Author
Emma Lawlor

## Project Overview
A simple interactive hangman game, written in Python. This game randomly chooses a word from a list of words. The user is then prompted to guess the letters of the word, or the word itself until they have correctly identified the word or until they run out of lives. Each incorrect answer adds to the hangman image, with the game ending when the hangman has been fully completed. 

![Google Chrome - Python Terminal by Code Institute - Google Chrome](https://user-images.githubusercontent.com/84344402/135355526-41012bfc-9773-4a9c-8ed8-eb6079be6303.gif)

Deployed Site:
https://hangman-emma-lawlor.herokuapp.com/

## Table of Contents
Generate after readme is complete for UX and below

## How To Play
- On visiting the site, the game initialises with a "Let's Play Hangman" message
- Start by choosing a letter
- Keep guessing letters until the word is correctly completed or until all lives have been used and the game is over. 
- Each time a letter is chosen, it is checked to see if it is correct/incorrect with the relevant message displayed to the user. 
- At the end of the game, play again by entering 'Y' or finish the game by entering 'N'

## Features

### Implemented Features
- Start of game: On visiting the site, the user is greeted with a "Let's Play Hangman" message as well as an empty hangman image and the entire word represented by dashes since the user has not yet made any guesses. The user is also prompted to guess a letter by asking for input "Choose a letter:"

![image](https://user-images.githubusercontent.com/84344402/135350017-8529ced5-17c1-4ebe-9009-3a3c2b53ef5d.png)

- Input Validation: The user's chosen letter is checked against a number of conditions. 
  - If the input is invalid, the user is alerted and prompted to choose again
  
  ![image](https://user-images.githubusercontent.com/84344402/135350370-d13a8a78-d68c-4792-b08d-ee769673100d.png)#
  
  - If the user correctly chooses a letter in the word, text is displayed green and the dashes in the word are replaced with the correct letter as appropriate
  
  ![image](https://user-images.githubusercontent.com/84344402/135350606-1b86aa18-a49f-482e-94cc-34b08bbf8e95.png)
  
  - If the user chooses a letter that is not in the word, the text is displayed in red and the hangman image is updated to the next stage indicating the loss of a life
  
  ![image](https://user-images.githubusercontent.com/84344402/135350767-0ed0d1c3-6a91-43cb-8c1c-d5201f0b4d88.png)
  
  - If the user chooses a letter that they have already guessed, they are asked to try again without the loss of an extra life
  
  ![image](https://user-images.githubusercontent.com/84344402/135351977-6df1edce-dbe8-4ae8-8567-6b31ff5c33b9.png)

- End of Game:
  - If the user has correctly completed the word or guessed the word, they get a congratulations message in green text and are asked if they want to play again
  
  ![image](https://user-images.githubusercontent.com/84344402/135351418-5d434ad0-9fcd-4995-b86b-4afb0ea45472.png)
  
  - If the user fails to guess the word correctly, they get a game over message in red text and are asked if they would like to play again
  
  ![image](https://user-images.githubusercontent.com/84344402/135351558-030edaa5-2956-44fb-b69e-3fda96f1a665.png)

  - If the user chooses not to play the game their result is displayed in terms of the number of games won out of the total number of games played
  
  ![image](https://user-images.githubusercontent.com/84344402/135351720-14d29960-a874-4f58-ad78-34bb79e5afbc.png)
  
 - Data Collection:
 
     - In designing the game, every effort was made to try to ensure the successful collection of data from the user when choosing a letter. 
     - Letters are used in their lowercase format by using the .lower() method on the user's input. Because of this, the user can enter both upper or lowercase letters, with the game functioning normally in all scenarios. 
     - Any leading or trailing spaces before or after the user's guessed letter is trimmed using the .strip() method. This ensures that even if the user accidentally enters spaces, only the letter entered will be evaluated as their guess. 
     - The application of both of these methods to the user's input enhances the user experience. They ensure that these minor typing errors can be overlooked by the app and that the game will function as expected when they are encountered. 
     ![image](https://user-images.githubusercontent.com/84344402/135769105-ea107fbe-ce50-4b86-97e2-cea9c31a4abf.png) 

### Future Features

- Score Tracking: By linking with Google Sheets, the game could ask the user for their name and email address, store their score details and email them a copy of their results upon exiting the game. 
- Personalised Messages: Through the use of a 'user' class, the game could collect the user's first name and use this to personalise the welcome message and the end of game text. 
- Rules: At the start of the game, the user could be given the option to have the rules of Hangman displayed, explaining how to play the game. 

## Design Documents

- In the early planning stages, a flowchart was drawn up to help visualise the steps required to create a functioning hangman game. 
- This chart was helpful to the developer when creating functions as the logic of the game was broken down into simple steps.
- [This flowchart](https://1drv.ms/b/s!AtrJulJDGsm2qFf5wKQGuJDN1MRH) was created using [Lucidchart](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier1_mixed_search_brand_exact_&km_CPC_CampaignId=1490375427&km_CPC_AdGroupID=55688909257&km_CPC_Keyword=lucidcharts&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433236001&km_CPC_TargetID=aud-826163889020:kwd-84176206937&km_CPC_Country=20483&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&mkwid=sMDuh5elr_pcrid_442433236001_pkw_lucidcharts_pmt_e_pdv_c_slid__pgrid_55688909257_ptaid_aud-826163889020:kwd-84176206937_&gclid=Cj0KCQjw1ouKBhC5ARIsAHXNMI-XHJRavE5VCyXoRZMUJrufGkLIFrq_iz1oKO4xAXMed81uEqSRagMaAsA5EALw_wcB)
![image](https://user-images.githubusercontent.com/84344402/133690510-8f1d770e-ccfe-4bea-908d-a1321736cb1d.png)

## Data Model

The class 'Hangman' is used as the data model for the game. 

The __init__ method initialises the following attributes for use in all instances of the class:
- self.word: uses the random method to choose a random word from the provided list in the words.py file. This is the word used for gameplay, which the user will try to decipher by guessing letters.
- self.stage: Used to display the correct version of the 'Hangman' image. The stage is incremented by 1 each time the user enters an incorrect letter, therefore displaying the next stage of the hangman each time an incorrect letter is entered.
- self.guessed_letters: An empty list, to which all letters guessed by the user throughout the game are added. This list is vital in gameplay, as it allows us to check if the user has already guessed the letter. If the letter has already been guessed, the user is advised of this and is asked to choose again. 
- self.guessed_words: As with guessed_words, this starts as an empty list. If the user chooses to guess an entire word, it is then added to this list. If they guess another word, this list is used to check if the word has already been guessed. 
- self.games_played: Starting at 0, this number is increased by 1 each time the user completes a game. 
- self.games_won: Again starting at 0, this is increased by 1 each time the user correctly completes the word and wins the game. A combination of games_played and games_won is used to return the user's overall result for the session when they choose to exit the game.  

The display_hangman function uses the self keyword to access the attributes of the hangman class. It displays the first stage of the hangman image to the user. It also displays the randomly generated word as a series of dashes, representing the letters the user needs to guess. 

The play_hangman function again uses the self keyword to access the attributes of the hangman class. While the user still has lives remaining, this function asks the user to guess a letter or word. The user's guess is then checked against the word in play. The user gets a message returned to them indicated if their guess is correct or incorrect. Correct letter guesses are shown in the word, replacing the dash in the relevant position. Incorrect guesses updates the hangman image, showing the hangman in it's next stage indicating the loss of a life. The game ends when the user has run out lives, has guessed all letters correctly r has correctly guessed the word. 

The play_again function also uses the self keyword to access the class attributes. At the end of the game the user is asked if they would like to play again. If they play again all attributes are re-initialised and the play-hangman function is called again. If the user does not wish to play again they get a 'thanks for playing' message as well as their result for the session. The result is displayed as the amount of games won out of the total number of games played in the session. 

## Libraries used
- Random module was imported to allow the program to select a random word from the words.py file for use in gameplay. 
- Colorama module was imported to allow styling and colouring of text displayed to the user in the terminal. This was used to enhance the user's experience and make the game more visually attractive. 
  - The main game text is yellow, with the hangman image and dashes representing letters are cyan.
  
  ![image](https://user-images.githubusercontent.com/84344402/135340001-b1b364be-b163-4216-813a-1d4fc6b1bc8b.png)
  
  - An incorrect guess is displayed in red text
  
  ![image](https://user-images.githubusercontent.com/84344402/135340201-dea4916c-4c58-4a36-b3d0-005642b6ed8a.png)
  
  - A correct guess is displayed in green text 
  
  ![image](https://user-images.githubusercontent.com/84344402/135340338-d41dc63d-e160-4aef-a1e5-3b8c1be07ae3.png)

## Testing

### Validation Testing

Both Python files of this repository were checked using the [Pep8Online](http://pep8online.com/) validator.

1.  The run.py file returned several errors for lines of code being too long, over 79 characters, as seen here. 

![image](https://user-images.githubusercontent.com/84344402/135769749-385a30a8-2f20-4b70-8a26-34168ac6e5a6.png)

These warnings were overwritten by adding '  # noqa' to the end of each line which was identified as being too long, as shown below. This tells the linter to ignore any issues with the particular line. It was decided not to break the code into shorter lines for readability and future maintainability of the file. 

![image](https://user-images.githubusercontent.com/84344402/135770089-3ecf6934-c4a8-43ca-9ab9-3cc6cb6a8844.png)

This eliminated all previous errors and on rechecking the run.py file, no errors were found in the code.

![image](https://user-images.githubusercontent.com/84344402/135770124-bc7d56e8-3817-4d16-a347-579cd3b7f1cc.png)

2. The words.py file returned a large number of errors and warnings, relating to the formatting of the list of words. The list was not properly indented, in line with the square brackets and several list items had trailing whitespace. 

![image](https://user-images.githubusercontent.com/84344402/135770395-1b3c44d3-e910-4293-aa2a-87239f5214ff.png)

This was corrected by moving all list items in line with the first list item. All instances of trailing whitespace identified by the linter were deleted. 

![image](https://user-images.githubusercontent.com/84344402/135772854-dfe52a67-3699-4b11-ab0e-214c1c9ed78d.png)

These changes corrected all errors and warnings and rec-checking the words.py file returned no errors. 

![image](https://user-images.githubusercontent.com/84344402/135770600-460a3e45-8910-47fb-9010-6d8be70029c5.png)

### Manual Testing

A template for test cases was created in the GitHub repository for this project. All instances of possible correct/incorrect user input were tested and results were recorded using these test case templates. The testing can be found in the GitHub Issues section [here](https://github.com/EmmaLawlor/hangman/issues?q=is%3Aissue+is%3Aclosed)


### Defect Tracking

### Defects of Note
- Any defects which occurred during development were tracked using the GitHub Issues section of this repository, which can be found [here](https://github.com/EmmaLawlor/hangman/issues).
![image](https://user-images.githubusercontent.com/84344402/135771710-36ca6cf2-8dd0-40cc-b45e-fd36bd5034f3.png)
- Details of each bug were noted as they were discovered, with screenshots taken to demonstrate the problem where possible.
- Some other minor bugs which occurred during development were not documented in this way as they were extremely quick and simple to fix. 
- The GitHub Issues section allowed for closeout of defects as they were rectified, again using screenshots to show the solution when possible.

### Outstanding Defects
- No outstanding defects have been noted. 

## Commit History

On review of this repository, an error in git commit messages was noted. For a time, when editing the README file directly in GitHub, the commit message was mistakenly entered in the 2nd entry field for optional extra data as seen here.

![image](https://user-images.githubusercontent.com/84344402/135771796-21da2f27-e1b4-4c5c-b338-436e463b8912.png)

This has resulted in the following main message for some commits.

![image](https://user-images.githubusercontent.com/84344402/135771827-e9cfb19a-7fa8-482d-b803-d0da2eaee8e7.png)

The intended commit message can be seen by clicking the ... beside the main message, as seen here.

![image](https://user-images.githubusercontent.com/84344402/135771851-1e131e1c-dab8-4dd2-8178-22578352f9dc.png)

Though this was noticed and corrected going forward, it was decided not to edit the affected commit messages. On researching the topic, while I learned it is possible to change commit messages, it is not recommended as it can confuse the commit history and make future development difficult. 

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

12. When the app has been deployed successfully, the page updates with a link to view the app
![image](https://user-images.githubusercontent.com/84344402/134729634-35e5c778-0071-4747-b72a-37491f01981a.png)


### Gitpod

To run locally in Gitpod use the following steps:

1. Navigate to the [GitHub repository](https://github.com/EmmaLawlor/hangman) for the project

![image](https://user-images.githubusercontent.com/84344402/135773220-de0823ae-552f-4721-a057-31122d6567a3.png)

2. Ensuring the Gitpod extension is installed in Google Chrome, click the green Gitpod button

![image](https://user-images.githubusercontent.com/84344402/135773232-21d146fc-a7ba-4e4c-aece-25503138fee5.png)

3. When the workspace launches, type "pip3 install -r requirements.txt" in the terminal to install requirements

![image](https://user-images.githubusercontent.com/84344402/135773271-c6be48f0-4106-42c5-a2b3-2a0cfd80df38.png)

4. Type "python3 run.py" to run the project in the terminal

![image](https://user-images.githubusercontent.com/84344402/135773303-45a2a355-7c23-4dda-85b5-87b3389fbe6e.png)

## Credits

-[Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
    - The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.

### Content

- List of random words generated using [Random Word Generator](https://randomwordgenerator.com/)
- Stages of hangman taken from (https://inventwithpython.com/invent4thed/chapter8.html)
- Gameplay screen recorded using [Loom](https://www.loom.com/)
- Loom video converted to GIF format using [CloudConvert](https://cloudconvert.com/mp4-to-gif)

### Acknowledgments

- A special thanks, as always, to my mentor Malia for her invaluable help, feedback and advice. 
- The logic and code for this Hangman game was inspired by and adapted from [this tutorial](https://www.youtube.com/c/KiteHQ)
- Code for replacing underscores with correct letter guesses adapted from [this tutorial](https://github.com/kiteco/python-youtube-code/blob/master/build-hangman-in-python/hangman.py)
- This readme file was checked for spelling and grammar issues using [Grammarly](https://app.grammarly.com/)
