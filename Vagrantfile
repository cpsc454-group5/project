Vagrant.configure("2") do |config|
  config.vm.define "db" do |db|
    db.vm.box = "ubuntu/bionic64"
    db.vm.network "forwarded_port", guest: 8005, host: 8005
    db.vm.synced_folder "./DatabaseAPI", "/home/vagrant/databaseapi"
    db.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update
      sudo apt-get install -y python3 python3-pip
      sudo pip3 install flask waitress
      python3 /home/vagrant/databaseapi/app.py &
    SHELL
  end
  
  config.vm.define "frontend" do |frontend|
    frontend.vm.box = "ubuntu/bionic64"
    frontend.vm.network "forwarded_port", guest: 8006, host: 8006
    frontend.vm.synced_folder "./Frontend", "/home/vagrant/frontend"
    frontend.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update
      sudo apt-get install -y python3 python3-pip
      sudo pip3 install flask waitress
      python3 /home/vagrant/frontend/app.py &
    SHELL
  end
  
  config.vm.define "storage" do |storage|
    storage.vm.box = "ubuntu/bionic64"
    storage.vm.network "forwarded_port", guest: 8007, host: 8007
    storage.vm.synced_folder "./Storage", "/home/vagrant/storage"
    storage.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update
      sudo apt-get install -y python3 python3-pip
      sudo pip3 install flask waitress
      python3 /home/vagrant/storage/app.py &
    SHELL
  end
end