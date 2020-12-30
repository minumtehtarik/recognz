python -m venv project1
which python
source project1/bin/activate
pip install opencv-contrib-python --upgrade
pip install opencv-python 
pip install pillow
pip list --format=columns
deactivate

Migrasi environment
pip freeze  --local > requirement.txt
pindahkan file txt ke environemtn yg diinginkan
pip install -r requirement.txt

C:\> python
>>> import cv2
>>> print(cv2.__version__)
>>> print(cv2.__file__)

.gitignore
git init
git add .
git commit -m ""
git remote 
git push
