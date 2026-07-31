import os
import sys

# Point Python to the chanbomaydi_system folder so imports work correctly
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chanbomaydi_system'))
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chanbomaydi_system'))

from auth_server import app

port = int(os.environ.get('PORT', 5000))
print(f"Starting auth server on port {port}")
app.run(host='0.0.0.0', port=port, debug=False)
