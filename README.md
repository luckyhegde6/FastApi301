# FastApi301
FastApi project

## Getting Started

- Venv init
```
python -m venv .venv```

- Activating the venv
```
.venv\Scripts\activate.bat
```
## Adding and installing Dependencies
You can also install it part by part.

This is what you would probably do once you want to deploy your application to production:
```
pip install fastapi
```
Also install uvicorn to work as the server:
``` 
pip install "uvicorn[standard]"
```
And the same for each of the optional dependencies that you want to use.

### For first run
```
uvicorn main:app --reload
```