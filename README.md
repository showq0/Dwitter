# Dwitter Overview

**Dwitter** is a simple social media web application built using **Django**, where users can create posts ("dweets"), follow other profiles, and view dweets from the profiles they follow. This project demonstrates key concepts like user authentication, relational models, and dynamic content rendering.

## Features

- **User Profiles:** Each user has a unique profile created upon registration, providing a personalized experience.
- **Dweeting:** Users can create and post dweets with a maximum of 140 characters.
- **Follow System:** Users can follow and unfollow other profiles, creating a network of content they can view.
- **Feed:** Users see dweets from profiles they follow, ordered by creation date.
- **Automatic Profile Creation:** A signal ensures that every time a new user registers, a corresponding profile is automatically created. Additionally, each profile follows itself by default, establishing a basic relationship structure for the follow system.

## Models

In Dwitter, every user has exactly one profile, and these profiles can follow one another. The follow system is **asymmetrical**, meaning a user can follow someone without being followed back.

### Profile Model

The `Profile` model is created automatically for each user upon registration. It represents the user's social profile within the application and contains:

- **user (OneToOneField):** This field links each profile to a specific user via a one-to-one relationship.
- **follows (ManyToManyField):** This field represents the profiles that the user follows. It allows users to create a network of profiles they are interested in. The relationship is asymmetrical, meaning users can follow others without being followed back.

This model is used to manage user connections and interactions within the social network.

### Dweet Model

The `Dweet` model represents the posts that users can create. Each dweet is associated with a specific user and contains the following fields:

- **user (ForeignKey):** This field links each dweet to the user who created it. It establishes a one-to-many relationship between users and their dweets.
- **body (CharField):** The content of the dweet, limited to 140 characters. This field allows users to share their thoughts in short, concise posts.
- **created_at (DateTimeField):** The timestamp of when the dweet was created. This field helps order the dweets chronologically.

The `Dweet` model provides a way for users to communicate their thoughts and share content with others within the platform.

## How to Run the Project

Follow these steps to run the Dwitter project locally:

1. **Clone the repository:**
    
    ```bash
    git clone <repository-u
    ```
    
2. **Navigate to the project directory:**
    
    ```bash
    cd dwitter
    ```
    
3. **Create a virtual environment and activate it:** For macOS/Linux:
    
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```
    
    For Windows:
    
    ```bash
    python -m venv env
    .\env\Scripts\activate
    ```
    
4. **Install the dependencies:**
    
    ```bash
    pip install -r requirements.txt
    ```
    
5. **Apply the migrations to set up the database:**
    
    ```bash
    python manage.py migrate
    ```
    
6. **Run the development server:**
    
    ```bash
    python manage.py runserver
    ```
    

Now, you can open your browser and navigate to `http://127.0.0.1:8000/` to view the application.

## Usage Instructions

- **Register and Log In:** Sign up to create a profile and log in to access the platform.
- **Create Dweets:** Post dweets with a maximum of 140 characters to share your thoughts.
- **Follow/Unfollow Users:** Visit other user profiles and follow or unfollow them to customize your feed.
- **View Feed:** On your dashboard, view dweets from the profiles you follow, sorted by creation date.

## Future Improvements

Here are some planned improvements for the Dwitter platform:

- **Comments and Likes:** Users will be able to interact with dweets by commenting and liking them.
- **Improved UI Design:** The user interface will be enhanced to provide a more visually appealing and user-friendly experience.
- **Security Features:** Additional security measures, including password hashing and email verification, will be implemented to enhance user protection.
- **Notifications:** Users will receive notifications when someone follows them or interacts with their dweets.