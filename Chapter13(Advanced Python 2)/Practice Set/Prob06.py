#  Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv.

# Step 1: Freeze the installed packages of the system interpreter to a requirements file

# !pip freeze > requirements.txt

# Step 2: Create a virtual environment

# !python -m venv myenv

# Step 3: Activate the virtual environment

# !myenv\Scripts\activate

# Step 4: Install the packages from the requirements file

# !pip install -r requirements.txt
