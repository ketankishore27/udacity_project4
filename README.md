### Environment Setup

1. Download and install Conda if it's not already installed.
2. Create a new environment using the provided requirements file or run:
   ```bash
   conda create -n [envname] "python=3.8" scikit-learn dvc pandas numpy pytest jupyter jupyterlab fastapi uvicorn -c conda-forge
   ```
3. Install Git either through Conda (`conda install git`) or via your CLI (e.g., `sudo apt-get install git`).

### Repositories

1. Create a directory for your project and initialize Git within it.
2. As you work on the code, commit changes regularly. Any generated models that you want to preserve should be committed to Git.
3. Connect your local Git repository to GitHub.
4. Set up GitHub Actions on your repository. Use one of the pre-made GitHub Actions to ensure that at a minimum, it runs `pytest` and `flake8` on push, requiring both to pass without errors.
5. Ensure that the GitHub Action uses the same version of Python as in your development environment.
6. Set up a remote repository for Git.

### Data

1. Download `census.csv` and commit it to Git.
2. The data is messy; try opening it in Pandas to examine it.
3. Clean the data by removing all spaces using your preferred text editor.
4. Commit the cleaned data to Git (it's common to keep raw data untouched while updating the cleaned version).

### Model

1. Using the starter code, develop a machine learning model that trains on the cleaned data and saves the model. Complete any partially written functions.
2. Write unit tests for at least three functions in the model code.
3. Create a function that outputs the model's performance on different slices of the data. For simplicity, this function can focus on the categorical features.
4. Write a model card using the provided template.

### API Creation

1. Develop a RESTful API using FastAPI that includes:
   - A GET request at the root providing a welcome message.
   - A POST request for model inference.
   - Use type hinting.
   - Utilize a Pydantic model to handle the body of the POST request, including an example.
   - Note: The data contains names with hyphens, which are not allowed as variable names in Python. Do not modify the column names in the CSV; instead, use FastAPI/Pydantic features to handle this.
2. Write three unit tests for the API (one for the GET request and two for the POST request, testing different predictions).

### API Deployment

1. Create a free Heroku account. You can use either the web GUI or the Heroku CLI for the following steps.
2. Create a new app and deploy it from your GitHub repository.
3. Enable automatic deployments that only proceed if your continuous integration tests pass.
   - Hint: Consider how paths will differ between your local environment and Heroku.
   - Hint: Development in Python is fast, but relying on CI/CD to catch errors can slow down iteration. Running `flake8` locally before committing changes is recommended.
4. Write a script using the `requests` module to perform a POST request on your live API.