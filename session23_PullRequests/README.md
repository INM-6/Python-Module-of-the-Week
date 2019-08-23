# GitHub Pull Requests & Code Review

Mostly based on this awesome gist by [Chaser324](https://github.com/Chaser324): https://gist.github.com/Chaser324/ce0505fbed06b947d962

For NEST, the development workflow is explained here: http://nest.github.io/nest-simulator/development_workflow#basic-workflow

## Hands-on

Below, I outline the steps in an abstract manner. For the details, i.e. git comands, see one of the above references.

To provide a safe playgorund, I created a dummy upstream repository: https://github.com/AlexVanMeegen/PyMotW_pullrequests

### Preparation

* Fork the [upstream repository](https://github.com/AlexVanMeegen/PyMotW_pullrequests) to your GitHub account
* Clone the forked repository to create a local copy on your computer
* Add the upstream repository as a remote to your local repository

After this, `git remote -v` should show
```
origin	git@github.com:YourAccount/PyMotW_pullrequests.git (fetch)
origin	git@github.com:YourAccount/PyMotW_pullrequests.git (push)
upstream	git://github.com/AlexVanMeegen/PyMotW_pullrequests.git (fetch)
upstream	git://github.com/AlexVanMeegen/PyMotW_pullrequests.git (push)
```

### Doing the work

* Fetch from upstream and merge into your local master branch to make sure it is up to date
* Create a feature branch (branching off master) in your local repository
* Change to your feature branch
* 'Now, go to town hacking away and making whatever changes you want to'
* Commit all changes to your feature branch

### Pull request

* Fetch upstream & merge into your local master branch to get potential changes in upstream/master
* Rebase on the up-to-date master branch (if you feel unsure create a temporary branch as a backup)
* Push the feature branch to your fork
* Create pull request from the feature branch of your fork against upstream/master

### Review pull requests

* Just play around with GitHub's [pull request review functionality](https://help.github.com/en/articles/about-pull-request-reviews)
* If you feel fancy, [check out the proposed changes locally](https://gist.github.com/Chaser324/ce0505fbed06b947d962#checking-out-and-testing-pull-requests)

### Interactive demo.

Learn git branching by playing a game: https://learngitbranching.js.org
