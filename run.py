"""
    Runs the backend
"""
from waitress import serve
from pmm_backend import api, settings

if __name__ == '__main__':
    if settings.DEBUG:
        api.run(debug=True)
    else:
        serve(api, host='127.0.0.1', port=5000)
