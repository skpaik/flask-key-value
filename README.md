# flask-key-value

For store and retrieve data from a url.


## Steps
- Clone the project
```shell
git clone https://github.com/skpaik/flask-key-value.git
```

- Goto inside the folder
```shell
cd flask-key-value
```

- Create a environment
```shell
python3 -m virtualenv .env
```

- Activate the environment
```shell
source .env/bin/activate
```

- Install the library
```shell
pip install -r requirements.txt
```

- Run the project
```shell
flask run
```
### Helper methods
File name: `tests/fkv_helper.py`
Methods name: `set_kv, get_kv, delete_kv, set_series_kv, get_series_kv, delete_series_kv`

Uses example in class `tests/kv.py`

### Test the project
- Keep `flask run` on current terminal
- Open a new terminal on current project
- Activate Environment
- In terminal run 
```shell
python tests/kv.py
```