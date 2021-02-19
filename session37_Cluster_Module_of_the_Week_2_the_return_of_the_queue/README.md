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
into `~/.ssh/config` and thus reduce the access command to `ssh login`

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

## Git on Jureca
While hambach allows you to clone git repositories easily (especially using agent forwarding), outgoing ssh communication is prohibited on Jureca.
This still leaves using git via https.
The problem with this are of course passwords, so it is recommended to use access tokens

# Running Jobs
The batch scheduling software on both clusters is called SLURM.

## SLURM Commands
Basic Stuff:
`squeue`
`sinfo`
`scancel <jobid>`

Starting Job:
`srun`
`salloc`
`sbatch`

Jobfile Stuff

