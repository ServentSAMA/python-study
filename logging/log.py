import logging
import logging.config
import os

# pro_path = os.path.abspath('.')
# conf_path = os.path.abspath(os.path.join(pro_path + '/study/logging/logging.conf'))
# print(conf_path)
logging.basicConfig(format='[%(asctime)s] [%(levelname)s]:%(message)s', filename='log/test.log', level=logging.DEBUG)
# logging.config.fileConfig(conf_path)
logging.info('this is log')
logging.error('this is error')
logging.debug('this is debug')
logging.warning('this is warning')
logging.critical('this is critical')