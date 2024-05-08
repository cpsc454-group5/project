Vagrant.configure("2") do |config|
  config.hostmanager.enabled = true
  config.hostmanager.manage_host = true
  config.hostmanager.include_offline = true
  config.vm.define "db" do |db|
    db.vm.box = "ubuntu/bionic64"
    db.vm.hostname = 'database'
    #No, I didn't want to use static IPs but I must because DHCP is broken for hostmanager https://github.com/devopsgroup-io/vagrant-hostmanager/issues/86
    db.vm.network :private_network, ip: '192.168.42.2'
    db.vm.synced_folder "./DatabaseAPI", "/home/vagrant/databaseapi"
    db.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update
      sudo apt-get install -y python3 python3-pip
      sudo pip3 install flask waitress
      cd /home/vagrant/databaseapi/
      python3 app.py &
    SHELL
  end
  
  config.vm.define "frontend" do |frontend|
    frontend.vm.box = "ubuntu/bionic64"
    frontend.vm.hostname = 'frontend'
    frontend.vm.network :private_network, ip: '192.168.42.3'
    frontend.vm.synced_folder "./Frontend", "/home/vagrant/frontend"
    frontend.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update
      sudo apt-get install -y python3 python3-pip
      sudo pip3 install flask waitress requests
      python3 /home/vagrant/frontend/app.py &
    SHELL
  end
  
  config.vm.define "storage" do |storage|
    storage.vm.box = "ubuntu/bionic64"
    storage.vm.hostname = 'storage'
    storage.vm.network :private_network, ip: '192.168.42.4'
    storage.vm.synced_folder "./Storage", "/home/vagrant/storage"
    storage.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update
      sudo apt-get install -y python3 python3-pip
      sudo pip3 install flask waitress
      python3 /home/vagrant/storage/app.py &
    SHELL
  end
end