import pandasgui as pg
from yby import *

file = r"E:\Data\Paper_1\Data_v3\Y_lhs\20230724_191040_Y_lhs_master_log.pkl"

log = y_read(Path(file))
pg.show(log.df_lhs)
