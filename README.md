# Group project on the course "API: program interaction interface" - YaMDb

### Description
The YaMDb project collects user reviews of works. The works themselves are not stored in YaMDb, you cannot watch a movie or listen to music here.
The works are divided into categories such as "Books", "Movies", "Music". For example, in the "Books" category there may be works "Winnie the Pooh and everything-everything-everything" and "Martian Chronicles", and in the "Music" category there is the song "Recently" by the group "Beetles" and the second suite by Bach. The list of categories can be expanded (for example, you can add the category "Fine Art" or "Jewelry"). 
A work can be assigned a genre from the preset list (for example, "Fairy Tale", "Rock" or "Arthouse"). 
Only the administrator can add works, categories and genres.
Grateful or outraged users leave text reviews for the works and give the work a rating in the range from one to ten (an integer); an average rating of the work is formed from user ratings — a rating (an integer). The user can leave only one review per work.
Users can leave comments on reviews.
Only authenticated users can add reviews, comments, and ratings.

### Technologies
![python version](https://img.shields.io/badge/Python-3.9-yellowgreen?logo=python)
![django version](https://img.shields.io/badge/Django-2.2-yellowgreen?logo=django)
![djangorestframework version](https://img.shields.io/badge/djangorestframework-3.12-yellowgreen?logo=django)
![pytest version](https://img.shields.io/badge/pytest-6.2-yellowgreen?logo=pytest)
![sqlite version](https://img.shields.io/badge/SQLite-3-yellowgreen?logo=sqlite)
![requests version](https://img.shields.io/badge/requests-2.26-yellowgreen)

#### Functional

- Authentication using a JWT token.
- Reading for anonymous users.
- User management.
- Get a list of all categories and genres, add and remove.
- Getting a list of all the works, adding them.Receiving, updating and deleting a specific work.
- Getting a list of all reviews and adding them.Receiving, updating, and deleting a specific review.  
- Getting a list of all comments and adding them.Receiving, updating, and deleting a specific comment.
- The ability to get detailed information about yourself and delete your account.
- Filtering by fields.

### Request Examples

- User registration:  
``` POST /api/v1/auth/signup/ ```  
- Getting your account details:  
``` GET /api/v1/users/me/ ```  
- Adding a new category:  
``` POST /api/v1/categories/ ```  
- Deleting a genre:  
``` DELETE /api/v1/genres/{slug} ```  
- Partial updating of information about the work:  
``` PATCH /api/v1/titles/{titles_id} ```  
- Getting a list of all reviews:  
``` GET /api/v1/titles/{title_id}/reviews/ ```   
- Adding a comment to a review:  
``` POST /api/v1/titles/{title_id}/reviews/{review_id}/comments/ ```

The full list of endpoints and examples of requests/responses can be found after launching the dev server at the link:
``` http://localhost:8000/redoc/ ```


### Launching a project in development mode
Clone the repository and go to it on the command line:

```
git clone <here is the link to the repository>
```

```
cd api_yamdb
```

Create and activate a virtual environment:

```
python -m venv venv
```

```
source venv/Script/activate
```

```
python -m pip install --upgrade pip
```

Install dependencies from a file requirements.txt:

```
pip install -r requirements.txt
```

Perform migrations:

```
python manage.py migrate
```

Launch a project:

```
python manage.py runserver
```

After the server is started, detailed documentation is available at: http://localhost:8000/redoc/
### Development team and authors:
- 🐱‍💻 Rostyslav Zhytkov (Teamlead) - [https://github.com/Zulusssss](https://github.com/Zulusssss)
- 🐱‍👓 Ekaterina Myndresko - [https://github.com/Catiska](https://github.com/Catiska)
- 🐱‍👤 Manoilov Ilya - [https://github.com/pyttho](https://github.com/pyttho)
