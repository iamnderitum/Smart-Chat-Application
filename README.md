### Smart-Chat-App - Intelligent Chat App for Educational Purpuses
The Smart Chat App is an innovative & intelligent chat application designed specifically for students
learning programming, DevOps, and related fields.
Built using the powerful Django framework. This application leverages Intelligent Document Processing (IDP) technologies, Including ML, NLP, & OCR, to create an enriching  and interactive environment.

##### Key Features.
###### 1. Interactive Learning Environment:
- Students can seamlessly interact with tutors, peers, and the integrated chatbot to enhance their experience.

###### 2. Advanced AI Capabilities:
- The chatbot uses both NLP & ML to understand and respond to students' queries, providing accurate and context-aware answers.

###### 3. Document Processing:
- Leveraging OCR technology, the application can process and extract information from various document types, making it easier for students to access and understand learning materials.

###### 4. User-Friendly API:
- An intuitive API with A simple that allows students to focus on learning without getting bogged down by complex navigation.

###### 5. Real-Time Communication:
- Facilitates real-time chat functionality for efficient communication between students and tutors.


##### Prerequisites.
Python => 3.10

##### Considerations.
The project root folder contains optional docker files to simplify the build. If you want to use
the docker build, you should install Docker and Docker Compose on your local machine.

##### Setup & Installation guidelines.
1. Clone the repository:
    ~~~
    git clone https://github.com/iamnderitum/Smart-Chat-Application.git
    ~~~

2. Navigate to the project directory:
   ~~~
   cd smart-chat-app
   ~~~
3. Install the required packages using the requirements.txt file:
   ~~~
   pip install -r requirements.txt
   ~~~

4. Run the django Development server:
   ~~~
   python chatapp/manage.py runserver
   ~~~

##### Running Application Using Docker:
###### 1. Build & run the Docker Containers:
  ~~~
    docker-compose up --build
  ~~~

###### 2. Run the Django development Server:
~~~
  docker-compose run -rm chatapp python chatapp/manage.py test
~~~


##### Contributing
We welcome contributions to the Smart Chat App. If you would like to contribute, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

##### Contact
For any inquiries or support, please contact us at iamnderitum@gmail.com or support@smartchatapp.com

Feel free to modify this description to better fit the specifics of your project & personal preferences.