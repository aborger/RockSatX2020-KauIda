1. Clone RockSatX2020-KauIda repository: ``` $ git clone https://github.com/aborger/RockSatX2020-KauIda ```
2. Update Pi: ``` $ sudo apt-get update ```
3. Install Ricoh Software: 
``` sudo apt-get -y install build-essential
sudo apt-get -y install libtool
sudo apt-get -y install automake
sudo apt-get -y install pkg-config
sudo apt-get -y install subversion
sudo apt-get -y install libusb-dev

svn checkout svn://svn.code.sf.net/p/libptp/code/trunk libptp-code

cd libptp-code

./autogen.sh
./configure
make

sudo make install 
sudo ldconfig

sudo apt-get install -y android-tools-adb
```
4. Install Bluetooth code: ``` pip3 install Adafruit-BluefruitLE```
5. Fix Bluetooth code: https://github.com/donatieng/Adafruit_Python_BluefruitLE/commit/af46b05cbcfd82110c8bbd08ed3d483de128fed1
