Disclaimer: huge parts of this presentation are stolen from Jari's beautiful first Cluster Module of the Week.
# Motivation
What do you need in order to run jobs on Hambach/Jureca?
1. Access -> ssh
2. the right programs -> modules, git
3. some way to tell the cluster what to do -> slurm, jobfiles

# Access
Both Hambach and Jureca have to be accessed via ssh.
This means you will have to generate a key-pair, whose private part you will give to absolutely noone and whose public part has to be registered in the cluster of you choice.
For hambach this this is probably been taken care of already, or you have to write a mail to IT.
For Jureca you can upload a key via Judoor (given youare part of some project I think).

Furthermore both clusters can only be accessed via certain IP-addresses.
For Hambach this is the Jülich internal network, for Jureca a range can be specified on Judoor.
As most people don't have access to a static IP-Address the easiest way is to specify here the range Jülich internal range aswell.
This way Jureca can be accessed via VPN aswell, or via tunneling through login

## Key Generation:

`ssh-keygen -a 100 -t ed25519 -f ~/.ssh/id_ed25519`


## actual accessing something

`ssh dick@login.inm.kfa-juelich.de`

flags to keep in mind are:
`-A`, `-J`

mounting locally via `sshfs`, but don't forget to unmount (`fusermount -u <folder>`)

## ssh config
put something like:
```
Host hambach
    Hostname hambach.inm.kfa-juelich.de
    ProxyJump: login
    User dick
    IdentitiesOnly yes
    IdentityFile ~/.ssh/juelich_git
    ForwardAgent yes

Host login
    Hostname login.inm.kfa-juelich.de
    User dick
    IdentitiesOnly yes
    IdentityFile ~/.ssh/juelich_git
    ForwardAgent yes
```
into `~/.ssh/config` and thus reduce the access command to `ssh login` and as we set `ProxyJump: login` for hambach we don't even have to `ssh -J login hambach` but can simply `ssh hambach`.

## Moving Files
when moving files to jureca it should be mentioned that space and number of files in the home directory are very limited.
Whenever possible use your project folder.
The cleanest way of doing so is by activating your project via `jutil env activate -p <project id>` and then use the `$PROJECT`.

A way of figuring out which project you could activate is via Dennis' terminal voodoo `set | grep PROJECT`.

# Code

Both cluster allow loading of modules.
But what are Modules?

- Modules are a way of managing the user environment
- they let the user modify the environment on the fly
- provide preinstalled software
- can be loaded

## Basic Module commands:
`module`
`module avail`
`module load <module name>`
`module unload <module name>`
`module spider <module name>`

## Git on Jureca
While hambach allows you to clone git repositories easily (especially using agent forwarding), outgoing ssh communication is prohibited on Jureca.
This still leaves using git via https.
The problem with this are of course passwords, so it is recommended to use access tokens.
Once you created such a token, use `git config --global credential.helper store` to enable git to store you "Password", then `git clone`, type in your normal username when prompted but use the access token instead of a password.

# Running Jobs
The batch scheduling software on both clusters is called SLURM.

## SLURM Commands
Basic Stuff:
`squeue`
`sinfo`
`scancel <jobid>`
`sacct`

Starting Job:
`srun`
`salloc`
`sbatch`

## Jobfile Stuff
for example:
```
#!/bin/bash -x
#SBATCH --account=<project id>
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=32
#SBATCH --output=snake.out.%j
#SBATCH --error=snake.err.%j
#SBATCH --time=6:00:00
#SBATCH --partition=dc-gpu
#SBATCH --gres=gpu:1

cd /p/home/jusers/dick3/jureca/memory_kernel
module load Python PyTorch
../.local/bin/snakemake\
        --cluster ./submit_script.py\
        --jobs 100\
        --cluster-config cluster.json\
        --rerun-incomplete\
        --keep-going
```

whereby `--account` is only necessary on jureca and only if you have not activated your project using `jutil`.
