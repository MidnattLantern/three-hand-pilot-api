Flynarc API Template
===
Debug has been set to true

Following sensitive data should be complemented in env.py:

import os
os.environ['CLOUDINARY_URL'] = 'cloudinary://`Cloudinary URL`'
os.environ['DEV'] = '1'
os.environ['DATABASE_URL'] = "`Database URL`"
os.environ.setdefault("SECRET_KEY", "`Make anything up`")