Vagrant.configure("2") do |config|
  config.vm.box = "debian/bullseye64"

  # Máquina maestro
  config.vm.define "NGINX" do |tierra|
    tierra.vm.hostname = "NGINX.sistema.test"
    tierra.vm.network "public_network", bridge: "Realtek PCIe GBE Family Controller" # Clase
    tierra.vm.provider "virtualbox" do |vb|
      vb.name = "NGINX"
    end
    tierra.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update -y
      sudo apt-get install nginx -y
      sudo apt-get install git -y

      # Configuración de NGINX
      sudo systemctl status nginx
      sudo mkdir -p /var/www/amz/html
      cd /var/www/amz/html
      git clone https://github.com/cloudacademy/static-website-example
      sudo chown -R www-data:www-data /var/www/amz/html
      sudo chmod -R 755 /var/www/amz
      
      sudo cp /vagrant/config/amz /etc/nginx/sites-available/default
      sudo ln -s /etc/nginx/sites-available/amz /etc/nginx/sites-enabled/default
      sudo cp /vagrant/index.html /usr/share/nginx/html/index.html
      sudo systemctl restart nginx
      sudo systemctl status nginx

      # Configuración de FTPS
      sudo apt-get install vsftpd -y
      sudo useradd -m -s /bin/bash amz
      echo "amz:amz" | sudo chpasswd
      sudo mkdir /home/amz/ftp # Esta parte la he hecho porque lo pedía la práctica, pero luego tu cambiaste la idea principal de la práctica

      # Permisos para luego poder subir, modificar y eliminar archivos
      sudo chown -R amz:amz /var/www/amz/html/static-website-example
      sudo chmod -R 755 /var/www/amz/html/static-website-example

      # Generarión de certificados
      sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/vsftpd.pem -out /etc/ssl/private/vsftpd.pem
      sudo cp /vagrant/config/vsftpd.conf /etc/vsftpd.conf

      #  Convertir carácteres de Windows a Unix
      sudo apt-get install dos2unix -y
      sudo dos2unix /etc/vsftpd.conf
      
      sudo systemctl restart vsftpd
      sudo systemctl status vsftpd

    SHELL
  end
end