# Ansible 2 Cloud Cookbook

## How to use this repository?
This repo has code for Ansible 2 Cloud Cookbook. The code is organized chapter-wise and should be consulted in the same wa
y. Please go through the relevant recipe to understand the code better.

For installing Ansible, please use pip.

```
pip install ansible==2.4.0.0
```

For each chapter, please go through the first recipe in the book to install dependencies before trying out the code.

Each chapter has playbook which excutes all the code relevant to that chapter, except dynamic inventory and phonebook samp
le application. Several tasks depends on the variables created by previous tasks. Hence it is recommeneded to execute the
playbook entirely or replace the variables with a suitable value.

Most of the chapters have a dynamic inventory script and a phonebook playbook. This playbook should be executed in the end
 since it may use the infrastructure created by the recipes and tasks in the same chapter.
 
To run a playbook, simply do the following:
```
ansible-playbook <playbook.yml>
```

### Note: 
Since our tasks are executed in the same machine from which we run the playbook and interact with cloud providers API, we
do not need to specify the inventory.
