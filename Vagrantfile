# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
	config.vm.box = "dummy"
    config.ssh.keys_only = "false"
    config.vm.provider :aws do |aws, override|
        aws.region = "eu-west-1"
        aws.instance_type = "t2.micro"
        aws.ami = "ami-394f4b40"

        aws.keypair_name = "aws"
        override.ssh.username = "ubuntu"
        override.ssh.private_key_path = "/home/adalsa/.ssh/aws"
    end
    config.vm.provision :ansible do |ansible|
        ansible.playbook = "playbook.yml"
        ansible.extra_vars = { ansible_python_interpreter:"/usr/bin/python3" }
        ansible.vault_password_file=".vault_pass"
    end
end
