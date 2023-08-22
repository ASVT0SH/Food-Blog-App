# Food Blog App

Welcome to the Food Blog App! This Django-based web application is designed to help restaurant owners share culinary adventures, prices, and food experiences with the world. Whether you're a professional chef or just a passionate home cook, this app provides you with the perfect platform to connect with fellow food enthusiasts.

## Features

- **User Authentication:** Sign up, log in, and manage your profile. Only authenticated users can create, edit, and delete their posts.

- **Create and Edit Posts:** Share your recipes, cooking tips, and food stories through engaging blog posts.

- **Responsive Design:** Enjoy a seamless browsing experience on various devices, including desktops, tablets, and smartphones.

- **User-Friendly Interface:** The intuitive and clean interface makes navigating the app a breeze, ensuring both new and experienced users can enjoy all its features.

## Getting Started

To run the Food Blog App locally on your machine, follow these steps:

1. **Clone the Repository:** Start by cloning this repository to your local machine using the following command:

   ```
   [git clone https://github.com/asvt0sh/food-blog-app.git](https://github.com/ASVT0SH/Food-Blog-App.git)
   ```

2. **Set Up Virtual Environment:** Navigate to the project directory and create a virtual environment to isolate project dependencies:

   ```
   cd food-blog-app
   python -m venv .venv
   ```

3. **Activate the Virtual Environment:** Activate the virtual environment based on your operating system:

   - On Windows:

     ```
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```
     source venv/bin/activate
     ```

4. **Install Dependencies:** Install the required dependencies using `pip`:

   ```
   pip install django~=4.0.0
   ```

5. **Run Migrations:** Apply the database migrations to set up the initial database schema:

   ```
   python manage.py migrate
   ```

6. **Create Superuser:** Create a superuser account to access the admin panel and manage the app:

   ```
   python manage.py createsuperuser
   ```

7. **Run the Development Server:** Start the development server to run the app locally:

   ```
   python manage.py runserver
   ```

8. **Access the App:** Open your web browser and navigate to `http://127.0.0.1:8000/` or `localhost:8000` to access the Food Blog App.

## License

The Food Blog App is open-source software licensed under the [MIT License](LICENSE).

---

If you encounter any issues or have suggestions for improvements, feel free to [contact us](mailto:asutoshurs@gmail.com). Your feedback is invaluable to us.
