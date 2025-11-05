# Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?


# Step 1: Create the first virtual environment and install packages
# Open your terminal and run the following commands:
# python -m venv env1
# source env1/bin/activate  # On Windows use `env1\Scripts\activate`
# pip install numpy pandas matplotlib
# Step 2: Freeze the installed packages to a requirements file
# pip freeze > requirements.txt
# Step 3: Create the second virtual environment
# Deactivate the first environment
# deactivate
# Create the second virtual environment
# python -m venv env2
# Step 4: Activate the second virtual environment
# source env2/bin/activate  # On Windows use `env2\Scripts\activate`
# Step 5: Install the packages from the requirements file
# pip install -r requirements.txt
# Now, the second virtual environment (env2) has the same packages installed as the first one (env1).
# Note: Make sure to have Python and pip installed on your system to execute these commands.
