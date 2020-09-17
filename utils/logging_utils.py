from loguru import logger

time = '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> |'
level = "<level>{level: ^18}</level> |"
function =  "<cyan>{name: <32}</cyan>:<cyan>{function: ^30}</cyan>:<cyan>{line: 3}</cyan> |"
message = "<bold>{message}</bold>"

DEFAULT_FORMAT = ' '.join([time, level, function, message])


def log_request(level: str, method: str, id: str, ip: str, endpoint: str, tempo: str = None):
    message = f"{method: ^4} | ID: {id: <36} | IP: {ip: ^16} | ENDPOINT: {endpoint: ^20}|"
    if tempo:
        message += f" TEMPO: {tempo}"
    logger.log(level, message)


