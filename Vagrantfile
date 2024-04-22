Vagrant.configure("2") do |config|
  # Define the VM box and version
  config.vm.box = "ubuntu/bionic64"

  # Port forwarding for Flask server (optional)
  config.vm.network "forwarded_port", guest: 8005, host: 8005

  # Folder synchronization
  config.vm.synced_folder "./DatabaseAPI", "/home/vagrant/DatabaseAPI"

  # Provisioning script
  config.vm.provision "shell", inline: <<-SHELL
    # Update apt package index
    sudo apt-get update

    # Install Python3 and pip3
    sudo apt-get install -y python3 python3-pip

    # Install Flask
    sudo pip3 install flask waitress

    python3 /home/vagrant/databaseapi/app.py &
  SHELL
end