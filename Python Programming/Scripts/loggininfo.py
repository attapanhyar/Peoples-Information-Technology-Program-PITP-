
import logging
def main() -> None:
    logging.basicConfig(level=logging.DEBUG,
                        
                        format="%(asctime)s %(levelname)s %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S",
                        filename='basic.log'
                        ) #Replace WARNING WITH INFO
    logging.debug('this is a debug message')
    logging.info('this is logging info')
    logging.warning('This is logging warning')
    logging.error('This is a logging error')
    logging.critical('this is a critical message')

if __name__ == "__main__":
    main()