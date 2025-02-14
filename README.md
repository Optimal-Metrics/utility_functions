# utility_functions
a set of function to use across repositories
if you need to use any of these functions you can clone this repository as a sub repository bu doing 

git submodule add https://github.com/username/repo-to-add.git path/to/submodule

this would copy the repository inside the current repository. 

if you need to update the sub repository 
Update Submodules
To pull the latest changes from a submodule:

Navigate to the submodule’s directory:

bash
Copy code
cd path/to/submodule
Pull updates from the submodule’s repository:

bash
Copy code
git pull origin main
Commit the updated submodule in the main repository:

bash
Copy code
cd /path/to/your-main-repo
git add path/to/submodule
git commit -m "Update submodule to latest version"
Push changes:

bash
Copy code
git push

# be sure to pip install the requirements.txt
