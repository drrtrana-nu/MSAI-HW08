## Homework Instructions
MBAI 401 Tech Onramp<br>
Suggested completion date: 09/09/21

Test Instructions
---
- This homework uses the unittest testing framework instead of the pytest testing framework. 
- However, it behaves very similarly. At any point, you can run individual tests by clicking 
  on the green play button next to the tests. 
- You can also run all the tests by right-clicking on the runner.py and choosing Run. This will run all 
  the tests for all the problems and provide useful information.
  
Problem 1 - Practice with Stacks, Queues, and BSTs
---
1. In the `p1` package, you have been provided with a module named `bst.py` that contains a
   `Node` class and a `BST` class to represent a binary search tree (bst). In addition, you 
   have also been provided with the `insert` method and the `create` method so that you can 
   create a bst. A small sample tree has been provided for you.
2. Write the method `traverse_inorder` that does not take any arguments (only has the `self` parameter).
   This method should traverse a binary search tree using a stack/iteration and return the list of nodes
   traversed inorder (left-root-right).
   - Do not do this using recursion. Instead, you should use a stack and iteration. The import 
     needed for this has been provided for you at the top of the file. An `if __main__` block has been
     provided for you with a method call commented out.
   - Uncomment the tests in the file that begin with `test_inorder...`. Remove the pass keyword.
 3. Write the method `breadth_first_traversal` that does not take any arguments (only has the `self` parameter).
    This method should traverse a binary search tree and return the list of nodes using breadth-first
    search traversal from the root node to the leaves.
   - Do not use recursion. Instead, you should use a queue and iteration. The import 
     needed for this has been provided for you at the top of the file. An `if __main__` block has been
     provided for you with a method call commented out.
   - Uncomment and run the tests in the `test_bst.py` file that begin with `test_breadth...`. 
     Remove the pass keyword.
   
Problem 2 - APIs and JSON
---
The goal of this problem is to practice working with APIs. Due to some of the challenges of writing tests when
working with APIs, we won't be writing tests for this problem. We will be working with the PetFinder API which 
requires authentication. To get started, you will need to do the following:
1. Create an account on PetFinder: https://www.petfinder.com/user/register/
2. Request a developer API key: https://www.petfinder.com/developers/ <br>
   For this, you will need to provide a name for your application (PetFinderHomework) and a link to your
   application. For the link to the application, you can provide a personal link or you can make a quick
   GitHub repo and provide the link to the repo.
3. Once you request the API key, you will be provided with the key (also referred to as client_id) and a
   secret (also referred to as a secret). THESE ARE CONFIDENTIAL. You will be asked to put them in your code
   for purposes of this assignment, but please remove them before submitting your assignment (replace with
   XXXXXXX). There are multiple ways of storing API keys/secrets, but that is beyond the scope of this assignment.
   However, if you're interested, you can set up a quick meeting with me and I'll walk you through a quick way
   to do it in PyCharm.
4. A class named `PetAuthorization` has been created for you. This class has a static method named `get_token` 
   that takes your API key and your secret as a parameter and posts a request for authorization, and gets back 
   the token needed for authorization. Put your secret and API key where indicated in the code.
5. Create the `get_json_response` method:
    - This method should include the following code for the authorization header:
       `headers = {'Authorization': 'Bearer ' + PetAuthorization.get_token()}`
    - The API call is: `'https://api.petfinder.com/v2/animals'`
    - This method should take one parameter that represents a dictionary of the query parameters.
    - Using the `requests` library (imported for you at the top), make a call to the PetFinder API with the 
       headers variable first (use `headers=headers` after the API url), and then include the query parameters 
       provided as the parameter.
    - For examples on query parameters, see here: https://www.petfinder.com/developers/v2/docs/#get-animals
6. Create a file named `pet_finder.py` in the `p2` package. Then, create a function named 
   `get_chicago_terriers` that does not have any parameters and does the following:
    - Use the `get_json_response` method from the `PetAuthorization` class (make sure to import the file
      using relative imports) to get the json response for the following query parameters 
      (remember to make these strings):<br>
      breed: Terrier <br>
      location: 60657
    - Print out the total number of animals returned.
    - For each animal returned, print out the data for the following properties: `name`, `url`, `type`, `age`, `photos`
7. Use the `if __main__` block and call this function. Pending time, play around with other query parameters 
   to see what types of responses you get.
     
**Push your code to GitHub!**