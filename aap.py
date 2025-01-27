import nlpcloud 

class NLPApp:

  def __init__(self):

    self.__db = {}
    self.__first_menu()

  def __first_menu(self):

    user_input = input("""

    Hello how would you like to proceed ?

    1. New to site then register
    2. If already registered then please login
    3. Exit

    """)

    if user_input == '1':
      self.__register()


    elif user_input == '2':
      self.__login()

    elif user_input == '3':
      exit()


  def __second_menu(self):

    second_input = input("""

    Hi! how would you like to proceed ?

    1. NER
    2. Language Detection
    3. Sentiment Analysis
    4. Conversation with AI
    5. Logout

    """)

    if second_input == '1':
      self.__ner()

    elif second_input=='2':
      self.__LD()

    elif second_input=='3':
      self.__SA()

    elif second_input == '4':
      self.__talk_with_ai()

    elif second_input=='5':
      exit()



  def __register(self):

    name = input("Enter your name = ")
    email = input("Enter your mail_id = ")
    password = input("Enter your password = ")

    if email in self.__db.keys():
      print("Email is already exist")

    else:
      self.__db[email] = [name, password]
      print(self.__db)
      print("============================================================================")
      print("You have successfully registered")
      print("============================================================================")
      print("Now login by valdating your email id and password")
      self.__first_menu()

  def __login(self):

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email in self.__db:
        if self.__db[email][1] == password:
            print("Login successful")
            self.__second_menu()
        else:
            print("Valid email but incorrect password please reenter the password")
            self.__first_menu()
    else:
        print("Invalid email")
        self.__first_menu()

  # Name Entity Recognition

  def __ner(self):

   para =  input('enter the paragraph')
   search_term = input('what would you like to search')

   client = nlpcloud.Client("finetuned-llama-3-70b", "53f75202a2e7a665122ef81321b03098aa364c04", gpu=True)
   response = client.entities(para,searched_entity=search_term)
   print(response)

  # Language detection

  def __LD(self):

   para =  input('enter the paragraph')
   #search_term = input('what would you like to search')

   client = nlpcloud.Client("python-langdetect", "53f75202a2e7a665122ef81321b03098aa364c04", gpu=False)
   response = client.langdetection(para)
   print(response)


  # Semtiment Analysis

  def __SA(self):

   para =  input('enter the paragraph')
   #search_term = input('what would you like to search')

   client = nlpcloud.Client("finetuned-llama-3-70b", "53f75202a2e7a665122ef81321b03098aa364c04", gpu=True, lang="en")
   response = client.sentiment(para)
   print(response)

   # Conversation with AI

  def __talk_with_ai(self):

    para = input("Please type.....")
    client = nlpcloud.Client("finetuned-llama-3-70b", "53f75202a2e7a665122ef81321b03098aa364c04", gpu=True)
    response = client.chatbot(para,context="""This is a discussion between a human and an AI. The human is sad but the AI is empathetic and reassuring. The AI is called Patrick.""", history=[])
    print(response)
    #Answer = response['response']
    #for i in Answer.split('\n'):
      #print(i)

obj = NLPApp()






