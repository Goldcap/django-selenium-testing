#Installation Instructions

The first step is to ensure you have Python 2.7 installed. Most current (Fall 2014) distros run on Python 2.7, but to check, just run this in cli:

```Shell
python --version
```

Once Python is found, you'll need to install a few python "modules", using a utility known as PIP. Instructions for installing PIP can be found here:  

http://pip.readthedocs.org/en/latest/installing.html  

One last step, optional but highly recommended, create a "virtual environment" for Python to run in. All your installed Python modules will live within it, it's a great way to keep different python projects separate:  

http://virtualenv.readthedocs.org/en/latest/virtualenv.html  

So once you have Python, PIP, and VirtualEnv, you're ready to go!  

##Installing Program Prerequisites

###Installing python modules

```Shell
mkdirtualenv $somevenv  #Or if you have one set up, workon $someenv
pip install -r requirements.txt
```

###Installing Redis
A standard vanilla install of Redis is required, docs can be found online for that.

###Installing Tornado Logging Proxy
Copy the init script "doc/tornadoproxy/tornadoproxy" to your "init.d" folder, making sure the path to the binary is correct.  

Then run the tornado proxy logging script:  

```Shell
service tornadoproxy start
```

###Installing Squid
All requests from the Selenium browser will be proxied through a program called Squid. Notes for installing Squid are here, but note, it's a standard install. The only twist is, we need to proxy SSL requests, so to do that:  

+ Install Squid with ssl-crtd (Most distros have that. If not, contact Andy)
+ Copy the certs from the "doc/squid/ssl_cert" directory, along with the squid.conf file.
+ Start Squid

###Install Virtual (Headless) Display
Since we're using Selenium as a headless display, you'll finally need to install Xvfb, on Fedora like this:  

```Shell
yum -y install Xvfb libXfont xorg-x11-fonts* firefox
```

Some startup scripts are in the "doc/xvfb" directory.

```Shell
cp doc/xvfb/xvfb /etc/init.d
cp doc/xvfb/xvfb.sh /etc/profile.d 
source /etc/profile.d/xvfb.sh

chmod +x /etc/init.d/xvfb
chkconfig xvfb on
service xvfb start
```

##Starting The Python Django Application

###Nginx Configuration
There is a sample Nginx configuration in "doc/nginx", you can use that to proxy your services. Note, we run both a TCP Webserver, and a TCP Websocket. Make sure you modify the IP Address and file locations for your specific system.  


###Installing the Database
Copy the settings document:  

```Shell
cp  ppfa/ppfa/settings_local.py.sample ppfa/ppfa/settings_local.py
```

Modify the settings for your DB, and create that DB. Then, we'll sync our Django database, follow the instructions given there and make sure to create an administrative account:

```Shell
cd ppfa
python manage.py migrate
```

###Starting the webserver
Django has a standalone testing server, you can use to run your app during development.  

```Shell
python manage.py runserver 127.0.0.1:8020
```

###Modify your hosts file
Put the following lines in your hosts file, matching the nginx config above:  

127.0.0.1       dev.test.ppfa.net  

#Using the system. 
You should be able to browse dev.test.ppfa.net, and see it running.  Writing tests is pretty easy, given some basic knowledge of Python, view the tests here:  

```Shell
cd ppfa/selenium_tests/tests
vi testme.py
```

#Contact with Questions
Feedback would be great, missing steps in the install, things that broke, alternate instructions, just ping me and let me know what I can do to help get you off the ground.  

Thanks!

