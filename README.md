# Lecture 13 - Testing  

Get started by running `git clone https://github.com/Sresht/lect13`  

## Basic Unit Testing  

Welcome to the wonderful world of Test Driven Development (TDD)!  
For this exercise, you're going to be fixing already written test cases.  

1. Run the success tests: `python split_test.py SplitTestCase.test_split_success`   
2. Run the failure tests: `python split_test.py SplitTestCase.test_split_failure`  
3. Read through `split_test.py` with your in-class partners and understand what's  
   happening.  
4. Fix those test cases by modifying the test code   
    (you should not need to modify `test_split_success` or `test_split_failure`)  
5. Add your own success case and your own failure case!  


## Treat Yo Self (To Unit Tests)  

1. Run the success tests: `python chatbot_test.py ChatbotTestCase.test_parse_message_success`  
2. Read through `chatbot_test.py` with your in-class partners and understand what's  
   happening.  
3. Fix those text cases by modify the test code  
    (you should not need to modify `test_parse_message_success`)  
4. For homework, add at least one additional success test and at least 3 failure tests.  

## CircleCI Set Up

1. Set your origin to the new site: `git remote set-url origin git+ssh://git@github.com/<username>/lect13.git`  
1.5. Make a new github repository called lect13
2. `git commit -am "Fix unit tests"`  
3. `git status` should be empty  
3. `git push origin master`  

### Sign up for Circle CI:    
1. Navigate to https://circleci.com/signup/ and *Sign up with Github*  
2. Authorize CircleCI.  
3. Make sure you're in the right repo in the top right hand corner (this should be your account, not the organization).  
4. Once you've verified that, follow the demo on YouTube!
