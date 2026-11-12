import os, sys
import pandas as pd
import numpy as np

df = pd.read_excel(sys.argv[1])
comps = df['compounds'].tolist()
#ALIE
alie_min = [ ]
alie_max = [ ]
#LEAE
leae_min = [ ]
leae_max = [ ]
#HOMO and LUMO ODI
hodi = [ ]
lodi = [ ]
#mvol
mvol = [ ]
#HOMO metrics
hvol = [ ] #HOMO Volume
hden = [ ] #HOMO density
hsa = [ ] #HOMO surface area
#LUMO metrics
lvol = [ ] #LUMO Volume
lden = [ ] #LUMO density
lsa = [ ] #LUMO surface area
#ESP metrics
esp_min = [ ]
esp_max = [ ]
#Internal charge separation
pi = [ ]
#Molecular polarity index (MPI)
mpi = [ ]
#Nonpolar surface area 
npsa = [ ]
#Polar surface area
psa = [ ]
#Balance of charges (nu)
nu = [ ]
#positive and negative surface area for ESP
ptsa = [ ]
ntsa = [ ]
#positive and negative variance for ESP
pv = [ ]
nv = [ ]
#positive and negative average value for ESP
pav = [ ]
nav = [ ]
#Energy of HOMO and LUMO orbitals 
he = [ ]
le = [ ]
hl_gap = [ ]
#dipole moment
dm = [ ]
#EA and VIP
ea = [ ]
vip = [ ]
#HOMO and LUMO dipole moment
hod = [ ]
lod = [ ]
#Overlap integrals between HOMO and LUMO orbitasl
hl_olap = [ ]
#Centroid distance between HOMO and LUMO orbitals:
hlcd = [ ]
#number of electron in Pi orbitals
pi_ele = [ ]
##MPP and SDP##
mpp = [ ]
sdp = [ ]

for cp in comps :
    #####grep ALIE-min and ALIE-max#####
    tmp_alie_min_max = os.popen('''grep 'Minimal value:' %s '''%(cp + '-alie.txt')).read().splitlines()[0].split()
    alie_min.append(np.float64(tmp_alie_min_max[2]))
    alie_max.append(np.float64(tmp_alie_min_max[-2]))
    #####grep LEAE-min and LEAE-max#####
    tmp_alie_min_max = os.popen('''grep 'Minimal value:' %s '''%(cp + '-leae.txt')).read().splitlines()[0].split()
    leae_min.append(np.float64(tmp_alie_min_max[2]))
    leae_max.append(np.float64(tmp_alie_min_max[-2]))
    ######grep HOMO and LUMO ODI#####
    hlodi_txt = os.popen('''grep 'Orbital delocalization index:' %s '''%(cp + '-hodi.txt')).read().splitlines()
    hodi_value = hlodi_txt[0].split()[-1]
    lodi_value = hlodi_txt[1].split()[-1]
    hodi.append(np.float64(hodi_value))
    lodi.append(np.float64(lodi_value))
    ######grep mvol#####
    mvol_value = os.popen('''grep 'Volume:' %s '''%(cp + '-vol-result.txt')).read().splitlines()[0].split()[2]
    mvol.append(np.float64(mvol_value))
    ######grep HOMO metrics#####
    hvol_value = os.popen('''grep 'Volume:' %s '''%(cp + '-homovol-result.txt')).read().splitlines()[0].split()[2]
    hden_value = os.popen('''grep 'Estimated' %s '''%(cp + '-homovol-result.txt')).read().splitlines()[0].split()[-2]
    hsa_value = os.popen('''grep 'Overall' %s '''%(cp + '-homovol-result.txt')).read().splitlines()[0].split()[4]
    hvol.append(np.float64(hvol_value))
    hden.append(np.float64(hden_value))
    hsa.append(np.float64(hsa_value))
    ######grep LUMO metrics#####
    lvol_value = os.popen('''grep 'Volume:' %s '''%(cp + '-lumovol-result.txt')).read().splitlines()[0].split()[2]
    lden_value = os.popen('''grep 'Estimated' %s '''%(cp + '-lumovol-result.txt')).read().splitlines()[0].split()[-2]
    lsa_value = os.popen('''grep 'Overall' %s '''%(cp + '-lumovol-result.txt')).read().splitlines()[0].split()[4]
    lvol.append(np.float64(lvol_value))
    lden.append(np.float64(lden_value))
    lsa.append(np.float64(lsa_value))
    #####grep ESP-min and ESP-max#####
    tmp_esp_min_max = os.popen('''grep 'Minimal value:' %s '''%(cp + '-esp.txt')).read().splitlines()[0].split()
    esp_min.append(np.float64(tmp_esp_min_max[2]))
    esp_max.append(np.float64(tmp_esp_min_max[-2]))
    #Internal charge separation pi
    pi_value = os.popen('''grep 'Internal charge separation' %s '''%(cp + '-esp.txt')).read().splitlines()[0].split()[7]
    pi.append(np.float64(pi_value))
    #Molecular polarity index (MPI)
    mpi_value = os.popen('''grep 'Molecular polarity index (MPI)' %s '''%(cp + '-esp.txt')).read().splitlines()[0].split()[7]
    mpi.append(np.float64(mpi_value))
    #Nonpolar surface area 
    npsa_value = os.popen('''grep 'Nonpolar surface area' %s '''%(cp + '-esp.txt')).read().splitlines()[0].split()[7]
    npsa.append(np.float64(npsa_value))
    #Polar surface area
    psa_value = os.popen('''grep 'Polar surface area' %s '''%(cp + '-esp.txt')).read().splitlines()[0].split()[7]
    psa.append(np.float64(psa_value))
    #Balance of charges (nu)
    nu_value = os.popen('''grep 'Balance of charges (nu)' %s '''%(cp + '-esp.txt')).read().splitlines()[0].split()[4]
    nu.append(np.float64(nu_value))
    #Positive surface area and Negative surface area for ESP
    ptsa_value = os.popen('''grep 'Positive surface area:' %s '''%(cp + '-esp.txt')).read().splitlines()[0].split()[3]
    ntsa_value = os.popen('''grep 'Negative surface area:' %s '''%(cp + '-esp.txt')).read().splitlines()[0].split()[3]
    ptsa.append(np.float64(ptsa_value))
    ntsa.append(np.float64(ntsa_value))
    #Positive and Negative variance for ESP
    pv_value = os.popen('''grep 'Positive variance:' %s '''%(cp + '-esp.txt')).read().splitlines()[0].split()[5]
    nv_value = os.popen('''grep 'Negative variance:' %s '''%(cp + '-esp.txt')).read().splitlines()[0].split()[5]
    pv.append(np.float64(pv_value))
    nv.append(np.float64(nv_value))
    #Positive and Negative average value for ESP
    pav_value = os.popen('''grep 'Positive average value:' %s '''%(cp + '-esp.txt')).read().splitlines()[0].split()[6]
    nav_value = os.popen('''grep 'Negative average value:' %s '''%(cp + '-esp.txt')).read().splitlines()[0].split()[6]
    pav.append(np.float64(pav_value))
    nav.append(np.float64(nav_value))
    #Energy of HOMO and LUMO orbitals
    he_value = os.popen('''grep 'Note: Orbital' %s '''%(cp + '-homo-lumo-number-result.txt')).read().splitlines()[0].split()[-2]
    le_value = os.popen('''grep 'Orbital' %s | tail -n 1''' %(cp + '-homo-lumo-number-result.txt')).read().splitlines()[0].split()[-2]
    hl_gap_value = np.abs(np.float64(he_value) - np.float64(le_value))
    he.append(np.float64(he_value))
    le.append(np.float64(le_value))
    hl_gap.append(hl_gap_value)
    #dipole moment
    dmt_value = os.popen('''grep 'total     (au/Debye)      :' %s | tail -n 1''' %(cp + '.log')).read().splitlines()[0].split()[-1]
    dm.append(np.float64(dmt_value))
    #VIP
    vip_value = os.popen('''grep 'Janaks theorem for IP' %s | tail -n 1''' %(cp + '.log')).read().splitlines()[0].split()[-1]
    vip.append(np.float64(vip_value))
    #EA
    ea_value = os.popen('''grep 'Janaks theorem for EA' %s | tail -n 1''' %(cp + '.log')).read().splitlines()[0].split()[-1]
    ea.append(np.float64(ea_value))
    #HOMO and LUMO dipole moment
    fn_hlnum =  cp + '-homo-lumo-number-result.txt'
    hnum = os.popen('''grep 'HOMO' %s ''' %fn_hlnum).read().splitlines()[0].split()[3]
    lnum = os.popen('''grep 'LUMO' %s ''' %fn_hlnum).read().splitlines()[0].split()[2]
    with open(cp + '-orbint.txt') as hlod :
        txt = hlod.read().splitlines()
        hod_value = float(txt[int(hnum)-1].split()[-1])
        lod_value = float(txt[int(lnum)-1].split()[-1])
        hod.append(hod_value)
        lod.append(lod_value)
    #Overlap between HOMO and LUMO
    fnhl_lap = cp + '-orbital-overlap-result.txt'
    hl_olap_value = os.popen('''grep 'Overlap' %s ''' %fnhl_lap).read().splitlines()[0].split()[-1]
    hl_cd_value = os.popen('''grep 'Centroid distance' %s ''' %fnhl_lap).read().splitlines()[0].split()[-2]
    hl_olap.append(np.float64(hl_olap_value))
    hlcd.append(np.float64(hl_cd_value))
    #number of electron in Pi orbitals
    piele_value = os.popen('''grep 'Total number of electrons in pi orbitals:' %s '''%(cp + '-piorbitalele-result.txt')).read().splitlines()[0].split()[-1]
    pi_ele.append(np.float64(piele_value))
    ####MPP and SDP####
    mpp_value = os.popen('''grep 'Molecular planarity parameter (MPP) is' %s '''%(cp + '-mpp.txt')).read().splitlines()[0].split()[-2]
    sdp_value = os.popen('''grep 'Span of deviation from plane (SDP) is' %s '''%(cp + '-mpp.txt')).read().splitlines()[0].split()[-2]
    mpp.append(np.float64(mpp_value))
    sdp.append(np.float64(sdp_value))
########
data = {}
data['compounds'] = comps
#data['beta'] = df['beta']
#data['theta'] = (df['theta1'] + df['theta2'])/2
data['ALIE-min'] = alie_min
data['ALIE-max'] = alie_max
data['LEAE-min'] = leae_min
data['LEAE-max'] = leae_max
data['HODI'] = hodi
data['LODI'] = lodi
data['Mvol'] = mvol
data['Hvol'] = hvol
data['Hden'] = hden
data['HSA'] = hsa
data['Lvol'] = lvol
data['Lden'] = lden
data['LSA']  = lsa
data['ESP-min'] = esp_min
data['ESP-max'] = esp_max
data['ICS'] = pi
data['MPI'] = mpi
data['NPSA'] = npsa
data['PSA'] = psa
data['BC'] = nu
data['PTSA-ESP'] = ptsa
data['NTSA-ESP'] = ntsa
data['PAV-ESP'] = pav
data['NAV-ESP'] = nav
data['PV-ESP'] = pv
data['NV-ESP'] = nv
data['HOMO'] = he
data['LUMO'] = le
data['HL-Gap'] = hl_gap
data['DMT'] = dm
data['EA'] = ea
data['VIP'] = vip
data['HDMT'] = hod
data['LDMT'] = lod
data['HLCD'] = hlcd
data['HL-overlap'] = hl_olap
data['Pi-nele'] = pi_ele
data['MPP'] = mpp
data['SDP'] = sdp

df_data = pd.DataFrame(data)
df_data.to_excel('gxtb-da-total-data.xlsx', index=False)

