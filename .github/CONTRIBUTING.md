# Contribution Guidelines

## Create an Issue

Before creating an issue, *please search all closed and open issues to make sure that your question has not already been answered*. If that is the case, open an issue and follow the [Issue Template](https://github.com/mantiumai/mantiumclient-py/blob/main/.github/templates/issue_template.md). Please explain any *relevant and necessary* details to the issue.

## Create a Pull Request

In order for us to take the appropriate action with your Pull Request, please use the PR templates from the PR dropdown menu.

Feel free to use and reproduce these templates from our [Pull Request Templates](https://github.com/mantiumai/mantiumclient-py/tree/main/.github/templates).

### Pull Request Guide:

1. Create a personal fork of the repository to your own Github and clone it onto your local machine. Your remote repo is now called `origin`.
2. Add the original repo (ours) as a remote called `upstream`. Check out [Configuring a Remote For a Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/configuring-a-remote-for-a-fork) if you're unsure of how to do this.
3. If you have a fork but haven't updated it recently, be sure to pull changes from `upstream`.
4. Create a branch off of the `main` branch to work on the feature you intend to modify! It is highly recommended that you work on one feature per branch so that any changes can be easily documented and understood.
To name your branch please use this format: `username-issue#-name-of-feature`
5. Implement the changes in your branch - please be sure to add any necessary comments and follow the style conventions of our codebase.
6. Have you run a linter over your code? Do you have tests for it? Please do that now! (*Poetry implementation guide coming soon)*.
7. Correct any linting or testing errors you may have encountered.
8. Double check your documentation and update it as necessary.
9. Squash your commits into one commit - details on how to do that [here](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History#:~:text=file%E2%80%9D%20commit%20completely.-,Squashing%20Commits,-It%E2%80%99s%20also%20possible).
10. Push your branch up to your Github fork (`origin`).
11. Open a pull request to our project's `main` branch from the correct branch in your fork. Be sure to follow the relevant template.
12. Once your pull request has been approved and merged, you can then pull from `upstream` into your main local repository and delete the branch(es) to which those changes belonged.

### General Tips for Contributions:

1. Documentation is good! If you made a design choice that may not be obvious, concisely explain why it was done. If you might forget why you made a change when you look at your code later, add a short comment to that change.
2. Readable code helps everyone - variables should be named descriptively and functions should be as short and modular as possible.
3. Commit messages should be relevant to the changes made.
4. Follow code style standards!
5. If you were asked to make changes in your PR review, request another review once you have applied the necessary changes.

## Questions? Find us on [developer.mantiumai.com](https://developer.mantiumai.com/discuss).

If you have any general questions that are not directly related to a Github issue, please use the Developer Hub Discussions page.
