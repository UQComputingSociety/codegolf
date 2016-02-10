# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 80, host: 80, protocol: 'udp', auto_correct: true
  config.vm.network "forwarded_port", guest: 80, host: 80, protocol: 'tcp', auto_correct: true
  config.vm.provision :shell, path: "scripts/setup.sh"

  config.vm.provider "virtualbox" do |vb|
    vb.name = "UQCS - Codegolf"
    vb.memory = 512
    vb.cpus = 1
  end
end
