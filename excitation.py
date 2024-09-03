import numpy as np
import re

def V2Read(FileName):
    with open(FileName, 'r') as fid0:
        endrow = sum(1 for _ in fid0)

    Ti_number = endrow

    Damping = None
    dt = None
    npts = None
    accstart = None
    velstart = None
    disstart = None

    with open(FileName, 'r') as fid1:
        for i in range(Ti_number):
            Tline = fid1.readline()

            if 'Damping' in Tline:
                str_line = re.sub(r'\s+', '', Tline)
                str_split = str_line.split(',')
                for item in str_split:
                    if 'Damping' in item:
                        k = re.findall(r'(?<=Damping=)\S\d*', item)
                        if k:
                            Damping = float(k[0])
                        break

            if 'accel data equally spaced' in Tline:
                accstart = i + 1
                str_split = Tline.split()
                loc1 = str_split.index('at')
                dt = float(str_split[loc1 + 1])
                loc2 = str_split.index('points')
                npts = int(str_split[loc2 - 1])

            if 'veloc data equally spaced' in Tline:
                accend = i - 1
                velstart = i + 1

            if 'displ data equally spaced' in Tline:
                velend = i - 1
                disstart = i + 1

    Acc = []
    Vel = []
    Dis = []

    number_regex = re.compile(r'[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?')

    with open(FileName, 'r') as fida:
        for i in range(Ti_number):
            Tline = fida.readline()
            if i == accstart - 1:
                Acc = [float(num) for num in number_regex.findall(fida.read())[:npts]]

    with open(FileName, 'r') as fidv:
        for i in range(Ti_number):
            Tline = fidv.readline()
            if i == velstart - 1:
                Vel = [float(num) for num in number_regex.findall(fidv.read())[:npts]]

    with open(FileName, 'r') as fidd:
        for i in range(Ti_number):
            Tline = fidd.readline()
            if i == disstart - 1:
                Dis = [float(num) for num in number_regex.findall(fidd.read())[:npts]]

    return Acc, Vel, Dis, Damping, dt, npts

file_path = 'E:/CESMD_DATA混凝土/钢筋混凝土办公室/6层酒店/roof7/1CHAN007.V2'
Acc, Vel, Dis, Damping, dt, npts = V2Read(file_path)

def calculate_response_spectra(zeta, dt, Tmin, Tmax, DT, Acceleration):
    zeta = float(zeta)
    dt = float(dt)

    # Initialize the time array and response spectra array
    T = np.arange(Tmin, Tmax + DT, DT)
    Sa = np.zeros(len(T))
    Sv = np.zeros(len(T))
    Sd = np.zeros(len(T))
    pSa = np.zeros(len(T))
    pSv = np.zeros(len(T))
    Beta = np.zeros(len(T))

    Tmin0 = Tmin + DT if Tmin == 0 else Tmin

    # Calculate the response spectra
    for N, TT in enumerate(np.arange(Tmin0, Tmax, DT)):
        omega = 2 * np.pi / TT
        omega_d = omega * np.sqrt(1 - zeta**2)
        et = np.exp(-zeta * omega * dt)
        s = np.sin(omega_d * dt)
        c = np.cos(omega_d * dt)
        A1 = et * (zeta / np.sqrt(1 - zeta**2) * s + c)
        B1 = et * s / omega_d
        C1 = et * ((1 / omega**2 + 2 * zeta / (omega**3 * dt)) * c + 
                   (zeta / (omega * omega_d) - (1 - 2 * zeta**2) / (omega**2 * omega_d * dt)) * s) - 2 * zeta / (omega**3 * dt)
        D1 = et * (-2 * zeta * c / (omega**3 * dt) + 
                   (1 - 2 * zeta**2) / (omega**2 * omega_d * dt) * s) - 1 / omega**2 + 2 * zeta / (omega**3 * dt)
        A2 = -et * (omega / np.sqrt(1 - zeta**2) * s)
        B2 = et * (c - zeta / np.sqrt(1 - zeta**2) * s)
        C2 = et * (-1 / (omega**2 * dt) * c - 
                   (zeta / (omega * omega_d * dt) + 1 / omega_d) * s) + 1 / (omega**2 * dt)
        D2 = et * (1 / (omega**2 * dt) * c + 
                   zeta / (omega * omega_d * dt) * s) - 1 / (omega**2 * dt)

        a = np.zeros(len(Acceleration))
        v = np.zeros(len(Acceleration))
        d = np.zeros(len(Acceleration))
        v[0] = 0
        d[0] = 0

        for i in range(len(Acceleration) - 1):
            d[i+1] = A1 * d[i] + B1 * v[i] + C1 * Acceleration[i] + D1 * Acceleration[i+1]
            v[i+1] = A2 * d[i] + B2 * v[i] + C2 * Acceleration[i] + D2 * Acceleration[i+1]
            a[i+1] = -2 * zeta * omega * v[i+1] - omega**2 * d[i+1]

        Sa[N] = np.max(np.abs(a))
        Sv[N] = np.max(np.abs(v))
        Sd[N] = np.max(np.abs(d))
        Sa[0] = np.max(np.abs(Acceleration))
        pSv[N] = Sd[N] * omega
        pSv[0] = 0
        pSa[N] = Sd[N] * omega**2
        pSa[0] = np.max(np.abs(Acceleration))
        Beta[N] = Sa[N] / np.max(np.abs(Acceleration))

    return T, Sa, Sv, Sd, pSa, pSv, Beta

T, Sa, Sv, Sd, pSa, pSv, Beta = calculate_response_spectra(0.05, dt, 0.1, 6, 0.1, Acc)