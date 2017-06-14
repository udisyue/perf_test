# sudo easy_install virtualenv (OR sudo pip install virtualenv)
# mkdir priceUtility && cd priceUtility && virtualenv venv
. venv/bin/activate
cd view && nohup ../venv/bin/python view.py &
