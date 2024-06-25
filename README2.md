Introduction:
- Star Wars Rest API was built in addition to the Star Wars Blog Reading List project. API endpoints and a database model was added.

Features:
- Add favorites

Technologies Used - Frontend:
- Bootstrap
- JavaScript
- React

Technologies Used - Backend:
- Python
- Flask
- SQLAlchemy

## 1) Installation

- This template installs itself in a few seconds if you open it for free with Codespaces (recommended) or Gitpod.
- Skip this installation step and jump to step 2 if you decide to use any of those services.

- Important: The boilerplate is made for python 3.10 but you can change the `python_version` on the Pipfile.

The following steps are automatically ran within Gitpod, if you are doing a local installation you have to do them manually:

```sh
pipenv install;
psql -U root -c 'CREATE DATABASE example;'
pipenv run init;
pipenv run migrate;
pipenv run upgrade;
```

Note: Codespaces users can connect to psql by typing: `psql -h localhost -U gitpod example`

Contributors:
- Truitt Janney (https://github.com/truittjanney)

We welcome contributions from the community! How to contribute:
- Search existing issues before creating a new issue. Please check to see if it has already been reported. This helps us avoid duplicates.
- If you cannot find an existing issue, you can create a new one. Please provide detailed information about the problem, including steps to reproduce, expected behavior, and any relevant screenshots.

Making Changes:
- 1) Fork the repository - Start by forking the repository to your GitHub account.
- 2) Clone the repository - Clone your forked repository to your local machine using 'git clone https://github.com/your-username/your-repo-name.git
- 3) Create a new branch - Create a new branch for your changes. Use a descriptive name for your branch to identify the feature or fix you are working on.
- 4) Use the command 'git checkout -b your-branch-name'
- 5) Make your changes - Make your changes to the codebase. Ensure your code follows the project's coding standards and passes all tests.

Committing & Pushing Changes:
- 1) Commit your changes - Once you have made and tested your changes, commit them with a clear and concise commit message. Then push your changes to your forked repository.
- 2) Use the command 'git add .'
- 3) Use the command 'git commit -m "Description of the changes"'
- 4) Use the command 'git push origin your-branch-name'

Creating a Pull Request:
- 1) Navigate to the original repository - Go to the original repository where you want to submit your changes.
- 2) Create a pull request - Click on the "New Pull Request" button. Ensure your branch is compared with the correct branch in the original repository (usually "main" or "master").
- 3) Describe your changes - Provide a detailed description of your changes in the pull request. Mention any related issues and explain why the changes are necessary.
- 4) Submit the pull request - Submit your pull request and wait for the maintainers to review it.

Code Review & Feedback:
- Respond to feedback - The maintainers may request changes to your pull request. Be sure to respond to feedback promptly and make the necessary updates.
- Merge approval - Once your pull request is approved, it will be merged into the main codebase.

Best Practices for Contributing:
- Write clear commit messages - Make sure your commit messages are clear and descriptive.
- Follow coding standards - Adhere to the coding standards and guidelines specified in the repository.
- Test your changes - Ensure that your changes do not break existing functionality and pass all tests.
- Document your changes - Update any relevant documentation to reflect your changes.

Thank you for your interest in contributing to our project!
