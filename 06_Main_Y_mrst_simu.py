from yby import *

startup = r"D:\YAN\Research\MRST\mrst-2021b\startup.m"
temp_input = r"D:\YAN\Research\Paper\Paper_1\Code\Code_v3_master\temp_08_input.m"
temp_simu = r"D:\YAN\Research\Paper\Paper_1\Code\Code_v3_master\temp_08_simu.m"
info = 'master'
log_lhs = r"E:\Data\Paper_1\Data_v3\Y_lhs\20230724_191040_Y_lhs_master_log.pkl"
root_krige = r"E:\Data\Paper_1\Data_v3\Y_krige"

sat = [0.7, 0.3, 0]
pres = 70

log_lhs = y_read(Path(log_lhs))
root_krige = Path(root_krige)
poro_file = [i for i in root_krige.glob('*poro*.mat')]
perm_file = [i for i in root_krige.glob('*perm*.mat')]


for i,v in log_lhs.df_lhs.iterrows():
    frac_half_length = v['frac_length'] / 2
    frac_height = v['frac_height']
    frac_width = v['frac_width']
    poro_m = poro_file[i]
    perm_m = perm_file[i]
    poro_f = v['poro_f']
    perm_f = v['perm_f']

    revise = '''
    the_input.frac.halfLength={};
    the_input.frac.height={};
    the_input.frac.aperture={};
    the_input.rock.poro_file="{}";
    the_input.rock.perm_file="{}";
    the_input.frac.poro={};
    the_input.frac.perm={};
    '''.format(
        frac_half_length,
        frac_height,
        frac_width,
        str(poro_m),
        str(perm_m),
        poro_f,
        perm_f
    )

    Y_mrst().simu(startup, temp_input, revise, temp_simu, info='case_{:0>3d}'.format(i))
