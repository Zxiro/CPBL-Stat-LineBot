from django.test import TestCase

# Create your tests here.
def setUp(self):
    super(TestNginxBackend, self).setUp()
    settings.SENDFILE_BACKEND = 'sendfile.backends.nginx'
    settings.SENDFILE_ROOT = self.TEMP_FILE_ROOT
    settings.SENDFILE_URL = '/private'
    _get_sendfile.clear()