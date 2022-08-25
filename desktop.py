import logging
import sys
import requests
import multiprocessing
from time import sleep
from webview import Viewer

def start_flask():
    try:
        from app import app
        app.run(threaded=True,
                debug=False,
                port=8081,
                host="127.0.0.1",
                use_reloader=False)
    except:
        logging.fatal("Could not start flask")


def wait_server_ready():
    attempts = 50
    while attempts > 0:
        try:
            resp = requests.get('http://127.0.0.1:8081')
            if resp.status_code == 200:
                return
            else:
                logging.info("Status code %s", resp.status_code)
        except:
            logging.info("Server not ready: request errored")
        attempts = attempts-1
        sleep(.2)
    raise Exception("No server could be loaded")

if __name__ == '__main__':
    # Not 100% sure what this does, but it 
    # makes sure multiprocessing works in a "sealed application"
    # which it is after you package it. If you don't do this
    # the app will go completely haywire and spawn itself in
    # and endless loop. Not recommended.
    multiprocessing.freeze_support()
    
    try:
        # Allright, lets start Flask in a background thread
        server = multiprocessing.Process(
                target=start_flask, args=())
        logging.info("Starting server")
        server.start()
        logging.info("Waiting for server ready")

        # Wait for Flask to be ready. If you really want to
        # Be hip, you could also show a splash screen at this 
        # point. I was too lazy for that.
        wait_server_ready()
        logging.info("Server ready")

        # Open and show the viewer
        viewer = Viewer("http://127.0.0.1:8081/hedy")
        viewer.run_viewer()
    except Exception as e: 
        logging.exception("Could not start")
        viewer.show_error(str(e))
        viewer.exec_app()
    finally:
        logging.info("Shutting down flask")
        server.terminate()
        server.join()    
        sys.exit(0)
