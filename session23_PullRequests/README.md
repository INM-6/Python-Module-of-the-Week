# GitHub Pull Requests & Code Review

Mostly based on this awesome gist by [Chaser324](https://github.com/Chaser324): https://gist.github.com/Chaser324/ce0505fbed06b947d962
For NEST, the development workflow is explained here: http://nest.github.io/nest-simulator/development_workflow#basic-workflow

## Hands-on

Below, I outline the steps in an abstract manner. For the details, i.e. git comands, see one of the above references.

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

* Fetch upstream to make sure that your local master branch is up to date
* Create a feature branch in your local repository
* 'Now, go to town hacking away and making whatever changes you want to'
* Commit all changes to your local repository

### Pull request

* Fetch upstream to get potential changes in upstream/master
* Rebase on the current master branch (if you feel unsure create a temporary branch as a backup)
* Push to the forked repository
* Create pull request against upstream/master

### Review pull requests

* Just play around with GitHub's [pull request review functionality](https://help.github.com/en/articles/about-pull-request-reviews)
* If you feel fancy, [check out the proposed changes locally](https://gist.github.com/Chaser324/ce0505fbed06b947d962#checking-out-and-testing-pull-requests)
