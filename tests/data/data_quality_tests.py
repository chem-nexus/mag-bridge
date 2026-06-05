from dataclasses import dataclass
from typing import Optional

from src import DATA_QUALITY_SUBDIR


@dataclass(frozen=True, slots=True)
class DataQualityDiamagContrTestsSDF:
    """
    Tests for evaluating the data quality of diamagnetic contribution calculations performed by MagBridge.
    The test cases are based on literature examples of chemical compounds with experimentally measured diamagnetic susceptibilities.

    Parameters
    ----------
    sdf_file : str
        Name of the SDF file used as input.
    measured_diamag_sus : float
        Experimentally measured diamagnetic susceptibility.
    literature_reference : str
        Reference for the literature value of experimentally measured diamagnetic susceptibility.

    Note@1 SDF files does not convey stereochemical information.
    # TODO generate SMILES must provide information about stereochemical futures for future ML training purposes!
    """

    sdf_file: str
    measured_diamag_sus: float
    literature_reference: str
    description: Optional[str] = ""
    skip_test: bool = False


CALC_DIAMAG_QUALITY_TESTS: list["DataQualityDiamagContrTestsSDF"] = [
    # Aluminum compounds
    DataQualityDiamagContrTestsSDF(
        sdf_file="Al(NH4)(SO4)2.sdf",
        measured_diamag_sus=-98.11,
        literature_reference="No. 3",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Al(IO4)3_6H2O.sdf",
        measured_diamag_sus=-286.9,
        literature_reference="No. 4",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="AlK(SO4)2_12H2O.sdf",
        measured_diamag_sus=-251.28,
        literature_reference="No. 6",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="AlLi(SO4)2_12H2O.sdf",
        measured_diamag_sus=-240.0,
        literature_reference="No. 7",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="AlTl(SO4)2_12H2O.sdf",
        measured_diamag_sus=-266.0,
        literature_reference="No. 8",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Al(NH4)(SO4)2_12H2O.sdf",
        measured_diamag_sus=-253.63,
        literature_reference="No. 9",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="AlK(SO4)2.sdf",
        measured_diamag_sus=-102.33,
        literature_reference="No. 10",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Al2(SO4)3_18H2O.sdf",
        measured_diamag_sus=-335.6,
        literature_reference="No. 12",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Al2O3.sdf",
        measured_diamag_sus=-37.0,
        literature_reference="No. 13",
    ),
    # Antimony compounds
    DataQualityDiamagContrTestsSDF(
        sdf_file="SbBr3.sdf",
        measured_diamag_sus=-111.4,
        literature_reference="No. 16",
    ),
    # TODO How it is correct if there is no Pascal const for Sb(IV)?
    DataQualityDiamagContrTestsSDF(
        sdf_file="(NH4)2[SbBr6].sdf",
        measured_diamag_sus=-249.0,
        literature_reference="No. 19",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Sb(V)(Ph)3Br2.sdf",
        measured_diamag_sus=-232.4,
        literature_reference="No. 22",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Sb(V)(Ph)3Cl2.sdf",
        measured_diamag_sus=-232.4,
        literature_reference="No. 22",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Sb(V)(Ph)3I2.sdf",
        measured_diamag_sus=-261.1,
        literature_reference="No. 24",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Sb(V)(p-MePh)3Br2.sdf",
        measured_diamag_sus=-267.4,
        literature_reference="No. 28",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Sb(V)(p-MePh)3Cl2.sdf",
        measured_diamag_sus=-249.2,
        literature_reference="No. 29",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Sb(V)(o-MePh)3Cl2.sdf",
        measured_diamag_sus=-249.6,
        literature_reference="No. 30",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Sb(V)(p-MePh)3I2.sdf",
        measured_diamag_sus=-295.3,
        literature_reference="No. 31",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Sb(V)(o-MePh)3S.sdf",
        measured_diamag_sus=-233.2,
        literature_reference="No. 33",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Sb(III)(p-MeOPh)3.sdf",
        measured_diamag_sus=-230.1,
        literature_reference="No. 32",
        description="Calculations performed with Sb(III) covalent Pascal constant.",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Sb(3+)(p-MeOPh)3.sdf",
        measured_diamag_sus=-230.1,
        literature_reference="No. 32",
        description="Calculations performed with Sb(3+) ionic Pascal constant.",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Sb(V)(p-MePh)3S.sdf",
        measured_diamag_sus=-231.9,
        literature_reference="No. 34",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Sb(3+)(o-MePh)3.sdf",
        measured_diamag_sus=-217.0,
        literature_reference="No. 35",
        description="Calculations performed with Sb(3+) ionic Pascal constant.",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Sb(III)(o-MePh)3.sdf",
        measured_diamag_sus=-217.0,
        literature_reference="No. 35",
        description="Calculations performed with Sb(III) covalent Pascal constant.",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Sb(V)(1,2-Me2Ph)3Br2.sdf",
        measured_diamag_sus=-300.7,
        literature_reference="No. 37",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Sb(III)(PhOEt)3.sdf",
        measured_diamag_sus=-265.9,
        literature_reference="No. 38",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Sb(3+)(PhOEt)3.sdf",
        measured_diamag_sus=-265.9,
        literature_reference="No. 38",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Sb(III)(1,4-Me2Ph)3.sdf",
        measured_diamag_sus=-251.1,
        literature_reference="No. 39",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Sb(3+)(1,4-Me2Ph)3.sdf",
        measured_diamag_sus=-251.1,
        literature_reference="No. 39",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="SbCl3.sdf",
        measured_diamag_sus=-86.7,
        literature_reference="No. 41",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[Sb3+][Cl-]3.sdf",
        measured_diamag_sus=-86.7,
        literature_reference="No. 41",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[Sb5+][Cl-]5.sdf",
        measured_diamag_sus=-120.5,
        literature_reference="No. 42",
    ),
    # Arsenic compounds
    DataQualityDiamagContrTestsSDF(
        sdf_file="AsBr3.sdf",
        measured_diamag_sus=-106.0,
        literature_reference="No. 57",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="AsCl3.sdf",
        measured_diamag_sus=-72.5,
        literature_reference="No. 60",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="AsI3.sdf",
        measured_diamag_sus=-142.2,
        literature_reference="No. 63",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="As(CH3)2O(OH).sdf",
        measured_diamag_sus=-78.7,
        literature_reference="No. 68",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="As(CH2CH3)O(OH)2.sdf",
        measured_diamag_sus=-81.7,
        literature_reference="No. 69",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="As(CH2CH2CH3)O(OH)2.sdf",
        measured_diamag_sus=-93.19,
        literature_reference="No. 70",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="PhAsH2.sdf",
        measured_diamag_sus=-79.71,
        literature_reference="No. 72",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="PhAs(V)O(OH)2.sdf",
        measured_diamag_sus=-108.8,
        literature_reference="No. 73",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="HOPhAs(V)O(OH)2.sdf",
        measured_diamag_sus=-113.8,
        literature_reference="No. 74",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[1,3-(HO)2Ph]As(V)O(OH)2.sdf",
        measured_diamag_sus=-116.9,
        literature_reference="No. 75",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="{[p-[+H3N]Ph]As(V)O(OH)2.sk2}[Cl-].sdf",
        measured_diamag_sus=-139.8,
        literature_reference="No. 76",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(p-NCPh)As(V)O(OH)2.sdf",
        measured_diamag_sus=-115.7,
        literature_reference="No. 78",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(p-MePh)As(III)H2.sdf",
        measured_diamag_sus=-91.27,
        literature_reference="No. 79",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(p-MePh)As(III)O(OH)2.sdf",
        measured_diamag_sus=-120.0,
        literature_reference="No. 90",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ph2As(III)Cl.sdf",
        measured_diamag_sus=-145.5,
        literature_reference="No. 83",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[(Ph)2As(III)]2.sdf",
        measured_diamag_sus=-144.5,
        literature_reference="No. 84",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="{[(+H3NPh)2As(III)]2}[Cl-]2.sdf",
        measured_diamag_sus=-205.0,
        literature_reference="No. 85",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[(MePh)2As(III)]2.sdf",
        measured_diamag_sus=-165.2,
        literature_reference="No. 92",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(MePh)2(EtO)As(III).sdf",
        measured_diamag_sus=-182.6,
        literature_reference="No. 93",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ph3As(III).sdf",
        measured_diamag_sus=-177.6,
        literature_reference="No. 95",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ph3As(V)O.sdf",
        measured_diamag_sus=-199.0,
        literature_reference="No. 96",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ph3As(V)S.sdf",
        measured_diamag_sus=-193.2,
        literature_reference="No. 98",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ph3As(V)(OH)2.sdf",
        measured_diamag_sus=-211.0,
        literature_reference="No. 99",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(o-MePh)3As(III).sdf",
        measured_diamag_sus=-213.5,
        literature_reference="No. 102",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(p-MePh)3As(III).sdf",
        measured_diamag_sus=-212.1,
        literature_reference="No. 103",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(m-MePh)3As(V)O.sdf",
        measured_diamag_sus=-217.1,
        literature_reference="No. 104",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(p-MeOPh)3As(III).sdf",
        measured_diamag_sus=-225.6,
        literature_reference="No. 105",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(PhCH2O)3As(III).sdf",
        measured_diamag_sus=-244.0,
        literature_reference="No. 106",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(p-MePh)3As(V)S.sdf",
        measured_diamag_sus=-227.9,
        literature_reference="No. 107",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(1,4-MecyO)3As(III).sdf",
        measured_diamag_sus=-278.0,
        literature_reference="No. 108",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[(Ph4)As(III)][Re(VI)OBr4].sdf",
        measured_diamag_sus=-360.0,
        literature_reference="No. 109",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(p-EtOPh)3As(III).sdf",
        measured_diamag_sus=-261.0,
        literature_reference="No. 110",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(Ph-CH=CH-CH2O)3As(III).sdf",
        measured_diamag_sus=-259.0,
        literature_reference="No. 111",
    ),
    # Barium compounds
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba3(AsO3)2.sdf",
        measured_diamag_sus=-183.9,
        literature_reference="No. 112",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="BaBr2_H2O.sdf",
        measured_diamag_sus=-116.6,
        literature_reference="No. 114",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(BrO3)2_H2O.sdf",
        measured_diamag_sus=-117.5,
        literature_reference="No. 115",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="BaBr2_2H2O.sdf",
        measured_diamag_sus=-128.3,
        literature_reference="No. 116",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(BrO3)2.sdf",
        measured_diamag_sus=-105.8,
        literature_reference="No. 117",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="BaCO3.sdf",
        measured_diamag_sus=-58.9,
        literature_reference="No. 118",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(C2O4).sdf",
        measured_diamag_sus=-64.8,
        literature_reference="No. 119",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba[Pd(CN)4].sdf",
        measured_diamag_sus=-125.6,
        literature_reference="No. 120",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba[Pt(CN)4].sdf",
        measured_diamag_sus=-137.3,
        literature_reference="No. 121",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="BaCl2.sdf",
        measured_diamag_sus=-72.6,
        literature_reference="No. 122",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(ClO3)2_H2O.sdf",
        measured_diamag_sus=-99.2,
        literature_reference="No. 123",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(ClO4)2_H2O.sdf",
        measured_diamag_sus=-106.8,
        literature_reference="No. 124",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="BaCl2_2H2O.sdf",
        measured_diamag_sus=-100.0,
        literature_reference="No. 125",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(ClO4)2_2H2O.sdf",
        measured_diamag_sus=-119.5,
        literature_reference="No. 127",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(ClO3)2.sdf",
        measured_diamag_sus=-87.5,
        literature_reference="No. 128",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(ClO4)2.sdf",
        measured_diamag_sus=-94.7,
        literature_reference="No. 129",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="BaF2.sdf",
        measured_diamag_sus=-51.0,
        literature_reference="No. 130",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(IO3)2_H2O.sdf",
        measured_diamag_sus=-135.0,
        literature_reference="No. 131",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(NO2)2_H2O.sdf",
        measured_diamag_sus=-58.7,
        literature_reference="No. 132",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(OH)2.sdf",
        measured_diamag_sus=-53.2,
        literature_reference="No. 133",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="BaI2_2H2O.sdf",
        measured_diamag_sus=-163.0,
        literature_reference="No. 134",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(IO3)2_2H2O.sdf",
        measured_diamag_sus=-163.7,
        literature_reference="No. 135",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(S2O6)_2H2O.sdf",
        measured_diamag_sus=-120.0,
        literature_reference="No. 136",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(OH)2_8H2O.sdf",
        measured_diamag_sus=-157.0,
        literature_reference="No. 139",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="BaI2.sdf",
        measured_diamag_sus=-124.4,
        literature_reference="No. 140",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(NO3)2.sdf",
        measured_diamag_sus=-66.5,
        literature_reference="No. 143",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="BaSO4.sdf",
        measured_diamag_sus=-71.3,
        literature_reference="No. 146",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba[WO4].sdf",
        measured_diamag_sus=-57.4,
        literature_reference="No. 147",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(HCOO)2.sdf",
        measured_diamag_sus=-66.6,
        literature_reference="No. 155",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(OOC-CH2-COO).sdf",
        measured_diamag_sus=-81.3,
        literature_reference="No. 156",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(OOC-CH2-CH2-COO).sdf",
        measured_diamag_sus=-97.6,
        literature_reference="No. 157",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(AcO)2.sdf",
        measured_diamag_sus=-87.0,
        literature_reference="No. 158",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(tart)_H2O.sdf",
        measured_diamag_sus=-117.1,
        literature_reference="No. 159",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba[Pd(CN)4]_4H2O.sdf",
        measured_diamag_sus=-201.48,
        literature_reference="No. 160",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba[Pt(CN)4]_4H2O.sdf",
        measured_diamag_sus=-232.28,
        literature_reference="No. 161",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(n-PrCOOH)2.sdf",
        measured_diamag_sus=-145.6,
        literature_reference="No. 165",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(acac)2.sdf",
        measured_diamag_sus=-130.9,
        literature_reference="No. 168",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(PhCOO)2_2H2O.sdf",
        measured_diamag_sus=-203.2,
        literature_reference="No. 171",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba(ninhydrin_dimer).sdf",
        measured_diamag_sus=-160.0,
        literature_reference="No. 172",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba{Ph-C(=O)-CH=C(Me)-O}.sdf",
        measured_diamag_sus=-207.3,
        literature_reference="No. 173",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ba3[Cu(Ph-C#[C-])3]2.sdf",
        measured_diamag_sus=-538.0,
        literature_reference="No. 176",
        description="metalorganic compound for future ML / no pascal const for Cu(0)",
        skip_test=True,
    ),
    # Berylium compounds
    DataQualityDiamagContrTestsSDF(
        sdf_file="Be(OH)2.sdf",
        measured_diamag_sus=-23.1,
        literature_reference="No. 180",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Be(NO3)2.sdf",
        measured_diamag_sus=-41.0,
        literature_reference="No. 183",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="BeO.sdf",
        measured_diamag_sus=-11.93,
        literature_reference="No. 184",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="BeSO4.sdf",
        measured_diamag_sus=-37.8,
        literature_reference="No. 185",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Be(acac)2.sdf",
        measured_diamag_sus=-107.5,
        literature_reference="No. 187",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[Be4O(AcO)6].sdf",
        measured_diamag_sus=-182.2,
        literature_reference="No. 188",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[Be4O(EtCOO)6].sdf",
        measured_diamag_sus=-252.8,
        literature_reference="No. 189",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Be{Ph-C(=O)-CH=C(Me)-O}.sdf",
        measured_diamag_sus=-184.2,
        literature_reference="No. 190",
    ),
    # Bismuth compounds
    DataQualityDiamagContrTestsSDF(
        sdf_file="BiBr3.sdf",
        measured_diamag_sus=-136.0,
        literature_reference="No. 193",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[Bi3+][Br-]3.sdf",
        measured_diamag_sus=-136.0,
        literature_reference="No. 193",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[Bi3+][O2-][Cl-].sdf",
        measured_diamag_sus=-51.83,
        literature_reference="No. 194",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Bi(NO3)3_5H2O.sdf",
        measured_diamag_sus=-159.0,
        literature_reference="No. 198",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Bi(PO4).sdf",
        measured_diamag_sus=-71.22,
        literature_reference="No. 203",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Bi2O3.sdf",
        measured_diamag_sus=-80.15,
        literature_reference="No. 204",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Bi2(SO4)3.sdf",
        measured_diamag_sus=-149.14,
        literature_reference="No. 205",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Bi2S3.sdf",
        measured_diamag_sus=-122.9,
        literature_reference="No. 206",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Bi(cit).sdf",
        measured_diamag_sus=-120.2,
        literature_reference="No. 209",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[Bi3+](DMAB-diazonium+)[Cl-]4-resonance1.sdf",
        measured_diamag_sus=-265.0,
        literature_reference="No. 210",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[Bi3+](DMAB-diazonium+)[Cl-]4-resonance2.sdf",
        measured_diamag_sus=-265.0,
        literature_reference="No. 210",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="BiPh3.sdf",
        measured_diamag_sus=-194.6,
        literature_reference="No. 211",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[Bi3+][Ph-]3.sdf",
        measured_diamag_sus=-194.6,
        literature_reference="No. 211",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[Bi5+][Ph-]3[Cl-]2.sdf",
        measured_diamag_sus=-222.7,
        literature_reference="No. 212",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Bi(V)Ph3Cl2.sdf",
        measured_diamag_sus=-222.7,
        literature_reference="No. 212",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[Bi5+][Ph-]3[NO3-]2.sdf",
        measured_diamag_sus=-254.5,
        literature_reference="No. 213",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[Bi3+][MePh-]3.sdf",
        measured_diamag_sus=-229.2,
        literature_reference="No. 214",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Bi(PhMe)3.sdf",
        measured_diamag_sus=-229.2,
        literature_reference="No. 214",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Bi(V)(o-MePh)3Cl.sdf",
        measured_diamag_sus=-296.5,
        literature_reference="No. 215",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[Bi5+][o-MePh-]3[Cl-].sdf",
        measured_diamag_sus=-296.5,
        literature_reference="No. 215",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Bi(V)(p-MePh)3Cl.sdf",
        measured_diamag_sus=-263.4,
        literature_reference="No. 216",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[Bi5+][p-MePh-]3[Cl-].sdf",
        measured_diamag_sus=-263.4,
        literature_reference="No. 216",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Bi(2,4-Me2Ph)3.sdf",
        measured_diamag_sus=-262.7,
        literature_reference="No. 217",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[Bi3+](2,4-Me2Ph-)3.sdf",
        measured_diamag_sus=-262.7,
        literature_reference="No. 217",
    ),
    # Boron compounds
    DataQualityDiamagContrTestsSDF(
        sdf_file="BBr3.sdf",
        measured_diamag_sus=-85.5,
        literature_reference="No. 219",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[B3+][Br-]3.sdf",
        measured_diamag_sus=-85.5,
        literature_reference="No. 219",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[B3+][Cl-]3.sdf",
        measured_diamag_sus=-59.9,
        literature_reference="No. 220",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="BCl3.sdf",
        measured_diamag_sus=-59.9,
        literature_reference="No. 220",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="K[BF4].sdf",
        measured_diamag_sus=-54.42,
        literature_reference="No. 221",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="B(OH)3.sdf",
        measured_diamag_sus=-35.72,
        literature_reference="No. 224",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[B3+][OH-]3.sdf",
        measured_diamag_sus=-35.72,
        literature_reference="No. 224",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Rb(BH4).sdf",
        measured_diamag_sus=-41.0,
        literature_reference="No. 225",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Cd(BF4)2.sdf",
        measured_diamag_sus=-100.0,
        literature_reference="No. 226",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="B2O3.sdf",
        measured_diamag_sus=-38.73,
        literature_reference="No. 228",
    ),
    # TODO Add informative description for error with boron hydride clusters parsing
    # TODO We can also think about omitting RDKit errors and parsing the invalid structure anyway, exclusively for boron compounds.
    # TODO Add more tests for boron hydride clusters if the parsing issue will be solved
    DataQualityDiamagContrTestsSDF(
        sdf_file="[Cs+]2[(B10H10)2-].sdf",
        measured_diamag_sus=-52.0,
        literature_reference="No. 230",
        description="Boron hydride clusters cannot be parse properly by RDKit since it doesn't support the 3c-2e bonding.",
        skip_test=True,
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Na[HCOO-_B(OH)3]_2H2O.sdf",
        measured_diamag_sus=-88.9,
        literature_reference="No. 240",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="diazaborole.sdf",
        measured_diamag_sus=-31.5,
        literature_reference="No. 241",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="EtBBr2.sdf",
        measured_diamag_sus=-81.6,
        literature_reference="No. 242",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[Et-][B3+][Br-]2.sdf",
        measured_diamag_sus=-81.6,
        literature_reference="No. 242",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="BF3_MeOOMe.sdf",
        measured_diamag_sus=-59.0,
        literature_reference="No. 243",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="EtNH2_BH3.sdf",
        measured_diamag_sus=-53.1,
        literature_reference="No. 244",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="BF3_CH3CH2COOH.sdf",
        measured_diamag_sus=-72.0,
        literature_reference="No. 251",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="CH3CH2CH2BBr2.sdf",
        measured_diamag_sus=-95.5,
        literature_reference="No. 252",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="CH3CH2CH2B(OH)2.sdf",
        measured_diamag_sus=-58.5,
        literature_reference="No. 253",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="B(OCH3)3.sdf",
        measured_diamag_sus=-63.9,
        literature_reference="No. 254",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[B3+][CH3O-]3.sdf",
        measured_diamag_sus=-63.9,
        literature_reference="No. 254",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(MeO)3P_BH3.sdf",
        measured_diamag_sus=-84.5,
        literature_reference="No. 258",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="n-BuOBCl2.sdf",
        measured_diamag_sus=-97.0,
        literature_reference="No. 260",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="EtBpin.sdf",
        measured_diamag_sus=-72.9,
        literature_reference="No. 261",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Et2NBCl2.sdf",
        measured_diamag_sus=-100.0,
        literature_reference="No. 262",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="n-BuB(OH)2.sdf",
        measured_diamag_sus=-69.6,
        literature_reference="No. 263",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(Me2N)2BCl.sdf",
        measured_diamag_sus=-86.0,
        literature_reference="No. 264",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(n-BuO)3P_BH3.sdf",
        measured_diamag_sus=-185.7,
        literature_reference="No. 265",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="BCl3_py.sdf",
        measured_diamag_sus=-118.0,
        literature_reference="No. 270",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="BF3_py.sdf",
        measured_diamag_sus=-80.0,
        literature_reference="No. 271",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="n-C5H11BCl2.sdf",
        measured_diamag_sus=-99.0,
        literature_reference="No. 272",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Et-CH(Me)-CH2COOH_BF3.sdf",
        measured_diamag_sus=-104.0,
        literature_reference="No. 274",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="boratrane.sdf",
        measured_diamag_sus=-96.6,
        literature_reference="No. 275",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="n-C6H13BCl2.sdf",
        measured_diamag_sus=-112.0,
        literature_reference="No. 276",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="n-BuBpin.sdf",
        measured_diamag_sus=-96.1,
        literature_reference="No. 277",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="n-BuOBpin.sdf",
        measured_diamag_sus=-92.9,
        literature_reference="No. 278",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(n-Pr)2BBr.sdf",
        measured_diamag_sus=-104.6,
        literature_reference="No. 279",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="BF3_O(n-Pr)2.sdf",
        measured_diamag_sus=-107.0,
        literature_reference="No. 280",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(EtO)3B.sdf",
        measured_diamag_sus=-99.2,
        literature_reference="No. 282",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(i-PrO)(Me)(EtNH)P_BH3.sdf",
        measured_diamag_sus=-140.4,
        literature_reference="No. 285",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="n-C5H11OBpin.sdf",
        measured_diamag_sus=-105.8,
        literature_reference="No. 290",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="B(OAc)2]2O.sdf",
        measured_diamag_sus=-145.6,
        literature_reference="No. 291",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="n-C6H13OBpin.sdf",
        measured_diamag_sus=-114.1,
        literature_reference="No. 292",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(n-Bu)2BBr.sdf",
        measured_diamag_sus=-127.3,
        literature_reference="No. 293",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(n-BuO)2BCl.sdf",
        measured_diamag_sus=-132.0,
        literature_reference="No. 294",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(Et2N)2BCl.sdf",
        measured_diamag_sus=-134.0,
        literature_reference="No. 297",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(t-BuNH)2BCl.sdf",
        measured_diamag_sus=-138.0,
        literature_reference="No. 298",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="B(OCH2CH2CH2)3N.sdf",
        measured_diamag_sus=-135.0,
        literature_reference="No. 300",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(n-PrO)3B.sdf",
        measured_diamag_sus=-133.3,
        literature_reference="No. 301",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(i-PrO)3B.sdf",
        measured_diamag_sus=-134.8,
        literature_reference="No. 302",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(n-C5H11)2BCl.sdf",
        measured_diamag_sus=-143.0,
        literature_reference="No. 304",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[(1,2-C6H4)-]2[B3+][K+].sdf",
        measured_diamag_sus=-139.2,
        literature_reference="No. 305",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[(1,2-C6H4)2[B-])[K+].sdf",
        measured_diamag_sus=-139.2,
        literature_reference="No. 305",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[(1,2-C6H4)2[B-])[NH4+].sdf",
        measured_diamag_sus=-131.6,
        literature_reference="No. 306",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[(1,2-C6H4)-]2[B3+][NH4+].sdf",
        measured_diamag_sus=-131.6,
        literature_reference="No. 306",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(n-C6H13)2BCl.sdf",
        measured_diamag_sus=-162.0,
        literature_reference="No. 307",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(n-C6H13O)2BCl.sdf",
        measured_diamag_sus=-178.0,
        literature_reference="No. 308",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="H3C-(CH2)11-NH2_BF3.sdf",
        measured_diamag_sus=-183.0,
        literature_reference="No. 309",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(n-BuO)3B.sdf",
        measured_diamag_sus=-167.6,
        literature_reference="No. 310",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(i-BuO)3B.sdf",
        measured_diamag_sus=-169.9,
        literature_reference="No. 311",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(n-Bu)3N_BH3.sdf",
        measured_diamag_sus=-164.0,
        literature_reference="No. 312",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(t-BuNH)3B.sdf",
        measured_diamag_sus=-175.0,
        literature_reference="No. 313",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(n-Bu)3P_BH3.sdf",
        measured_diamag_sus=-170.9,
        literature_reference="No. 314",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(n-C5H11O)3B.sdf",
        measured_diamag_sus=-202.7,
        literature_reference="No. 317",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(i-C5H11O)3B.sdf",
        measured_diamag_sus=-205.2,
        literature_reference="No. 318",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[(n-Bu)t2N]2BCl.sdf",
        measured_diamag_sus=-224.0,
        literature_reference="No. 319",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="{(t-BuNH)(Cl)B}N(t-Bu){B(NHBu-t)2}.sdf",
        measured_diamag_sus=-253.0,
        literature_reference="No. 320",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="{(t-BuNH)2B}N(t-Bu){B(NHBu-t)2}.sdf",
        measured_diamag_sus=-291.0,
        literature_reference="No. 321",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Na[B(Ph)4].sdf",
        measured_diamag_sus=-221.0,
        literature_reference="No. 322",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="B(1-naphthalene)3.sdf",
        measured_diamag_sus=-239.0,
        literature_reference="No. 323",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[B3+][(1-naphthalene)-]3.sdf",
        measured_diamag_sus=-239.0,
        literature_reference="No. 323",
    ),
    # Source: [2] CRC Handbook of Chemistry and Physics International Standard BookNumber: 978-1-4987-5429-3
    DataQualityDiamagContrTestsSDF(
        sdf_file="acenaphthene.sdf",
        measured_diamag_sus=-109.9,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="acenaphthylene.sdf",
        measured_diamag_sus=-111.6,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="acetaldehyde.sdf",
        measured_diamag_sus=-22.2,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="acetamide.sdf",
        measured_diamag_sus=-33.9,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="acetic_acid.sdf", measured_diamag_sus=-31.8, literature_reference="[2] 3-576", description="exp data = calcd data", skip_test=True
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="acetic_anhydride.sdf",
        measured_diamag_sus=-52.8,
        literature_reference="[2] 3-576",
        description="exp data = calcd data",
        skip_test=True,
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="acetone.sdf",
        measured_diamag_sus=-33.8,
        literature_reference="[2] 3-576",
        description="exp data = calcd data",
        skip_test=True,
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="acetonitrile.sdf",
        measured_diamag_sus=-27.8,
        literature_reference="[2] 3-576",
        description="exp data = calcd data",
        skip_test=True,
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="acetophenone.sdf",
        measured_diamag_sus=-72.5,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="acetyl_chloride.sdf",
        measured_diamag_sus=-39.3,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="acetylene.sdf",
        measured_diamag_sus=-20.8,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="acridine.sdf",
        measured_diamag_sus=-118.8,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="allene.sdf",
        measured_diamag_sus=-25.3,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="allyl_alcohol.sdf",
        measured_diamag_sus=-36.7,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="allylamine.sdf",
        measured_diamag_sus=-40.1,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="aniline.sdf",
        measured_diamag_sus=-62.4,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="anisole.sdf",
        measured_diamag_sus=-72.2,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="anthracene.sdf",
        measured_diamag_sus=-129.8,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="9,10-anthracenedione.sdf",
        measured_diamag_sus=-113.0,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="trans-azobenzene.sdf",
        measured_diamag_sus=-106.8,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="azulene.sdf",
        measured_diamag_sus=-123.7,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="benzaldehyde.sdf",
        measured_diamag_sus=-60.7,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="benzamide.sdf",
        measured_diamag_sus=-72.0,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="benzene.sdf", measured_diamag_sus=-54.8, literature_reference="[2] 3-576", description="exp data = calcd data", skip_test=True
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="benzeneacetic_acid.sdf",
        measured_diamag_sus=-82.4,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="benzeneacetonitrile.sdf",
        measured_diamag_sus=-76.9,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1,2-benzenediamine.sdf",
        measured_diamag_sus=-72.5,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1,3-benzenediamine.sdf",
        measured_diamag_sus=-70.4,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1,4-benzenediamine.sdf",
        measured_diamag_sus=-70.7,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="benzil.sdf",
        measured_diamag_sus=-106.8,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="benzonitrile.sdf", measured_diamag_sus=-65.2, literature_reference="[2] 3-576", description="exp data = calcd data", skip_test=True
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="benzophenone.sdf",
        measured_diamag_sus=-109.6,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="p-benzoquinone.sdf",
        measured_diamag_sus=-36,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="benzyl_acetate.sdf",
        measured_diamag_sus=-93.2,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="benzyl_alcohol.sdf",
        measured_diamag_sus=-71.8,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="benzyl_benzoate.sdf",
        measured_diamag_sus=-132.2,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="biphenyl.sdf",
        measured_diamag_sus=-103.3,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="bromobenzene.sdf",
        measured_diamag_sus=-78.1,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-bromobutane.sdf",
        measured_diamag_sus=-77.1,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="bromochloromethane.sdf",
        measured_diamag_sus=-55.1,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="bromodichloromethane.sdf",
        measured_diamag_sus=-66.3,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="bromoethane.sdf",
        measured_diamag_sus=-54.7,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="bromomethane.sdf",
        measured_diamag_sus=-42.8,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-bromo-2-methylpropane.sdf",
        measured_diamag_sus=-79.9,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-bromonaphthalene.sdf",
        measured_diamag_sus=-115.9,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-bromopropane.sdf",
        measured_diamag_sus=-65.5,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-bromopropane.sdf",
        measured_diamag_sus=-65.1,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="3-bromopropene.sdf",
        measured_diamag_sus=-58.6,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="4-bromotoluene.sdf",
        measured_diamag_sus=-88.7,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="bromotrichloromethane.sdf",
        measured_diamag_sus=-73.2,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1,2-butadiene.sdf",
        measured_diamag_sus=-35.6,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1,3-butadiene.sdf",
        measured_diamag_sus=-32.1,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="butanal.sdf",
        measured_diamag_sus=-45.9,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="butane.sdf",
        measured_diamag_sus=-50.3,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1,3-butanediol.sdf",
        measured_diamag_sus=-61.8,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1,4-butanediol.sdf",
        measured_diamag_sus=-61.8,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="butanenitrile.sdf", measured_diamag_sus=-50.4, literature_reference="[2] 3-576", description="exp data = calcd data", skip_test=True
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-butanethiol.sdf",
        measured_diamag_sus=-70.2,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="butanoic_acid.sdf",
        measured_diamag_sus=-55.1,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-butanol.sdf",
        measured_diamag_sus=-55.9,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-butanol.sdf",
        measured_diamag_sus=-57.6,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-butanone.sdf",
        measured_diamag_sus=-45.6,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-butene.sdf",
        measured_diamag_sus=-41.0,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="cis-2-butene.sdf",
        measured_diamag_sus=-42.6,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="trans-2-butene.sdf",
        measured_diamag_sus=-43.3,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="butylamine.sdf",
        measured_diamag_sus=-58.9,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="butylbenzene.sdf",
        measured_diamag_sus=-100.7,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="tert-butylbenzene.sdf",
        measured_diamag_sus=-101.8,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="butyl_formate.sdf",
        measured_diamag_sus=-65.8,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="4-tert-butylphenol.sdf",
        measured_diamag_sus=-108.0,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="butyl_propanoate.sdf",
        measured_diamag_sus=-89.1,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(+)-camphor.sdf",
        measured_diamag_sus=-103.0,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="carbazole.sdf",
        measured_diamag_sus=-119.9,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="carbonyl_chloride.sdf",
        measured_diamag_sus=-47.9,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-chloroaniline.sdf",
        measured_diamag_sus=-79.5,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="3-chloroaniline.sdf",
        measured_diamag_sus=-76.6,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="4-chloroaniline.sdf",
        measured_diamag_sus=-76.7,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="chlorobenzene.sdf",
        measured_diamag_sus=-69.6,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-chlorobutane.sdf",
        measured_diamag_sus=-67.1,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-chlorobutane.sdf",
        measured_diamag_sus=-67.4,
        literature_reference="[2] 3-576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="chloroethene.sdf",
        measured_diamag_sus=-35.9,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="chloromethane.sdf", measured_diamag_sus=-32.0, literature_reference="[2] 3-577", description="exp data = calcd data", skip_test=True
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(chloromethyl)benzene.sdf",
        measured_diamag_sus=-81.2,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-chloronaphthalene.sdf",
        measured_diamag_sus=-107.6,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-chloro-2-nitrobenzene.sdf",
        measured_diamag_sus=-75.5,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-chloro-3-nitrobenzene.sdf",
        measured_diamag_sus=-77.2,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-chloro-4-nitrobenzene.sdf",
        measured_diamag_sus=-74.7,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-chlorooctane.sdf",
        measured_diamag_sus=-114.9,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-chlorophenol.sdf",
        measured_diamag_sus=-77.3,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="3-chlorophenol.sdf",
        measured_diamag_sus=-77.6,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="4-chlorophenol.sdf",
        measured_diamag_sus=-77.7,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="4-chloropropane.sdf",
        measured_diamag_sus=-56.0,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-chloropropene.sdf",
        measured_diamag_sus=-47.8,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="3-chloropropene.sdf",
        measured_diamag_sus=-47.8,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-chlorotoluene.sdf",
        measured_diamag_sus=-82.4,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="3-chlorotoluene.sdf",
        measured_diamag_sus=-79.7,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="4-chlorotoluene.sdf",
        measured_diamag_sus=-80.3,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="chlorotrifluoroethene.sdf",
        measured_diamag_sus=-49.1,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="chlorotrifluoromethane.sdf",
        measured_diamag_sus=-45.3,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="chrysene.sdf",
        measured_diamag_sus=-148.0,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="o-cresol.sdf",
        measured_diamag_sus=-70.8,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="m-cresol.sdf",
        measured_diamag_sus=-71.9,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="p-cresol.sdf",
        measured_diamag_sus=-71.9,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="cyanamide.sdf",
        measured_diamag_sus=-24.8,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="cyanogen.sdf",
        measured_diamag_sus=-21.6,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="cyanogen_chloride.sdf",
        measured_diamag_sus=-32.4,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="cyclobutane.sdf",
        measured_diamag_sus=-40.0,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="cycloheptane.sdf",
        measured_diamag_sus=-73.9,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1,4-cyclohexadiene.sdf",
        measured_diamag_sus=-48.7,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="cyclohexane.sdf",
        measured_diamag_sus=-66.1,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="cyclohexanol.sdf",
        measured_diamag_sus=-73.4,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="cyclohexanone.sdf",
        measured_diamag_sus=-62.0,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="cyclohexene.sdf",
        measured_diamag_sus=-58.0,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="cyclooctane.sdf",
        measured_diamag_sus=-85.3,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="cyclopentane.sdf",
        measured_diamag_sus=-59.2,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="cyclopentanol.sdf",
        measured_diamag_sus=-64.0,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="cyclopentanone.sdf",
        measured_diamag_sus=-51.6,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="cyclopropane.sdf",
        measured_diamag_sus=-39.2,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="cis-decahydronaphthalene.sdf",
        measured_diamag_sus=-107.0,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="trans-decahydronaphthalene.sdf",
        measured_diamag_sus=-107.6,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="decane.sdf",
        measured_diamag_sus=-119.5,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1,2-dibromoethane.sdf",
        measured_diamag_sus=-78.8,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="dibromomethane.sdf",
        measured_diamag_sus=-65.1,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="dibutylamine.sdf",
        measured_diamag_sus=-103.7,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="dichloroacetyl_chloride.sdf",
        measured_diamag_sus=-69.0,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="o-dichlorobenzene.sdf",
        measured_diamag_sus=-84.4,
        literature_reference="[2] 3-577",
        description="exp data = calcd data",
        skip_test=True,
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="m-dichlorobenzene.sdf",
        measured_diamag_sus=-84.1,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="p-dichlorobenzene.sdf",
        measured_diamag_sus=-81.7,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="dichlorodifluoromethane.sdf",
        measured_diamag_sus=-52.2,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1,1-dichloroethane.sdf",
        measured_diamag_sus=-57.4,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1,2-dichloroethane.sdf",
        measured_diamag_sus=-59.6,
        literature_reference="[2] 3-577",
        description="exp data = calcd data",
        skip_test=True,
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1,1-dichloroethene.sdf",
        measured_diamag_sus=-49.2,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="cis-1,2-dichloroethene.sdf",
        measured_diamag_sus=-51.0,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="trans-1,2-dichloroethene.sdf",
        measured_diamag_sus=-48.9,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="dichloromethane.sdf",
        measured_diamag_sus=-46.6,
        literature_reference="[2] 3-577",
        description="exp data = calcd data",
        skip_test=True,
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1,1-diethoxyethane.sdf",
        measured_diamag_sus=-81.4,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="diethylamine.sdf",
        measured_diamag_sus=-56.8,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="N,N-diethylaniline.sdf",
        measured_diamag_sus=-107.9,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="diethyl_carbonate.sdf",
        measured_diamag_sus=-75.4,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="diethyl_ether.sdf",
        measured_diamag_sus=-55.1,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="diethyl_malonate.sdf",
        measured_diamag_sus=-91.8,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="diethyl_oxalate.sdf",
        measured_diamag_sus=-81.7,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="diethyl_phthalate.sdf",
        measured_diamag_sus=-127.5,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="diethyl_succinate.sdf",
        measured_diamag_sus=-105.0,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="diiodomethane.sdf",
        measured_diamag_sus=-93.1,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="dimethoxymethane.sdf",
        measured_diamag_sus=-47.3,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="N,N-dimethylaniline.sdf",
        measured_diamag_sus=-85.1,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2,2-dimethylbutane.sdf",
        measured_diamag_sus=-76.2,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2,3-dimethylbutane.sdf",
        measured_diamag_sus=-76.2,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2,3-dimethyl-2-butene.sdf",
        measured_diamag_sus=-65.9,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="dimethyl_ether.sdf",
        measured_diamag_sus=-26.3,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2,6-dimethyl-4-heptanone.sdf",
        measured_diamag_sus=-104.3,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="3,4-dimethylhexane.sdf",
        measured_diamag_sus=-99.1,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="dimethyl_oxalate.sdf",
        measured_diamag_sus=-55.7,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2,2-dimethylpentane.sdf",
        measured_diamag_sus=-87.0,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2,3-dimethylpentane.sdf",
        measured_diamag_sus=-87.5,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2,4-dimethylpentane.sdf.sdf",
        measured_diamag_sus=-87.5,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="3,3-dimethylpentane.sdf.sdf",
        measured_diamag_sus=-89.5,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2,4-dimethyl-3-pentanone.sdf",
        measured_diamag_sus=-81.1,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2,4-dimethylpyridine.sdf",
        measured_diamag_sus=-71.3,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2,6-dimethylpyridine.sdf",
        measured_diamag_sus=-72.5,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="dimethyl_sulfide.sdf",
        measured_diamag_sus=-44.9,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="dimethyl_terephthalate.sdf",
        measured_diamag_sus=-101.6,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1,4-dioxane.sdf",
        measured_diamag_sus=-52.2,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="diphenylacetylene.sdf",
        measured_diamag_sus=-116,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="diphenylamine.sdf",
        measured_diamag_sus=-108.4,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1,2-diphenylethane.sdf",
        measured_diamag_sus=-127.8,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="diphenylmethane.sdf",
        measured_diamag_sus=-116.0,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="dipropyl_ether.sdf",
        measured_diamag_sus=-79.4,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="dodecanoic_acid.sdf",
        measured_diamag_sus=-113.0,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1,2-epoxybutane.sdf",
        measured_diamag_sus=-54.8,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="ethane.sdf",
        measured_diamag_sus=-26.8,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1,2-ethanediamine.sdf",
        measured_diamag_sus=-46.5,
        literature_reference="[2] 3-577",
        description="exp data = calcd data",
        skip_test=True,
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1,2-ethanediol.sdf",
        measured_diamag_sus=-38.8,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="ethanethiol.sdf",
        measured_diamag_sus=-47.0,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="ethanol.sdf",
        measured_diamag_sus=-33.6,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="ethoxybenzene.sdf",
        measured_diamag_sus=-84.5,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="ethyl_acetate.sdf",
        measured_diamag_sus=-54.1,
        literature_reference="[2] 3-577",
        description="exp data = calcd data",
        skip_test=True,
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="ethyl_acetoacetate.sdf",
        measured_diamag_sus=-71.7,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="N-ethylaniline.sdf",
        measured_diamag_sus=-85.6,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="ethylbenzene.sdf",
        measured_diamag_sus=-77.2,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="ethyl_benzoate.sdf",
        measured_diamag_sus=-93.8,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="ethyl_carbamate.sdf",
        measured_diamag_sus=-57.0,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="ethyl_cyanoacetate.sdf",
        measured_diamag_sus=-67.3,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="ethylene.sdf",
        measured_diamag_sus=-18.8,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="ethyl_formate.sdf",
        measured_diamag_sus=-43.0,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="3-ethylhexane.sdf",
        measured_diamag_sus=-97.8,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="ethyl_3-methylbutanoate.sdf",
        measured_diamag_sus=-91.1,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="3-ethylpentane.sdf",
        measured_diamag_sus=-86.2,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="ethyl_propanoate.sdf",
        measured_diamag_sus=-66.3,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="ethyl_vinyl_ether.sdf",
        measured_diamag_sus=-47.9,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="fluorobenzene.sdf",
        measured_diamag_sus=-58.4,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="fluoromethane.sdf",
        measured_diamag_sus=-17.8,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="formaldehyde.sdf",
        measured_diamag_sus=-18.6,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="formamide.sdf",
        measured_diamag_sus=-23.0,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="formic_acid.sdf",
        measured_diamag_sus=-19.9,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="fumaric_acid.sdf",
        measured_diamag_sus=-49.1,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="furan.sdf",
        measured_diamag_sus=-43.1,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="furfural.sdf",
        measured_diamag_sus=-47.2,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="furfuryl_alcohol.sdf",
        measured_diamag_sus=-61.0,
        literature_reference="[2] 3-577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="D-glucitol.sdf",
        measured_diamag_sus=-107.8,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="glycerol.sdf",
        measured_diamag_sus=-57.1,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="glycine.sdf",
        measured_diamag_sus=-39.6,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="heptanal.sdf",
        measured_diamag_sus=-81.0,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="heptane.sdf",
        measured_diamag_sus=-85.2,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="heptanoic_acid.sdf",
        measured_diamag_sus=-86.6,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-heptanol.sdf",
        measured_diamag_sus=-91.7,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="4-heptanol.sdf",
        measured_diamag_sus=-92.1,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-heptanone.sdf",
        measured_diamag_sus=-80.5,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="3-heptanone.sdf",
        measured_diamag_sus=-80.7,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="4-heptanone.sdf",
        measured_diamag_sus=-80.5,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-heptene.sdf",
        measured_diamag_sus=-77.8,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="hexachlorobenzene.sdf",
        measured_diamag_sus=-147.0,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="hexachloroethane.sdf",
        measured_diamag_sus=-112.8,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="hexadecane.sdf",
        measured_diamag_sus=-187.6,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="hexadecanoic_acid.sdf",
        measured_diamag_sus=-198.6,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-hexadecanol.sdf",
        measured_diamag_sus=-183.5,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1,5-hexadiene.sdf",
        measured_diamag_sus=-55.1,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="hexamethylbenzene.sdf",
        measured_diamag_sus=-122.5,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="hexanal.sdf",
        measured_diamag_sus=-69.4,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="hexane.sdf",
        measured_diamag_sus=-74.1,
        literature_reference="[2] 3-578",
        description="exp data = calcd data",
        skip_test=True,
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1,6-hexanediol.sdf",
        measured_diamag_sus=-84.3,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="hexanoic_acid.sdf",
        measured_diamag_sus=-78.1,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-hexanol.sdf",
        measured_diamag_sus=-79.2,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-hexanone.sdf",
        measured_diamag_sus=-69.2,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="3-hexanone.sdf",
        measured_diamag_sus=-69.0,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-hexene.sdf",
        measured_diamag_sus=-66.4,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="hexyl_acetate.sdf",
        measured_diamag_sus=-100.9,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-hexyne.sdf",
        measured_diamag_sus=-64.5,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="p-hydroquinone.sdf",
        measured_diamag_sus=-64.7,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-hydroxybenzoic_acid.sdf",
        measured_diamag_sus=-75,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="indene.sdf",
        measured_diamag_sus=-83,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1H-indole.sdf",
        measured_diamag_sus=-85.0,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="iodobenzene.sdf",
        measured_diamag_sus=-92.0,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-iodobutane.sdf",
        measured_diamag_sus=-93.6,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="iodoethane.sdf",
        measured_diamag_sus=-69.1,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="iodomethane.sdf",
        measured_diamag_sus=-57.2,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-iodopropane.sdf",
        measured_diamag_sus=-84.3,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="isobutane.sdf",
        measured_diamag_sus=-50.5,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="isobutene.sdf",
        measured_diamag_sus=-40.8,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="isobutyl_acetate.sdf",
        measured_diamag_sus=-78.7,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="isobutylamine.sdf",
        measured_diamag_sus=-59.8,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="isobutylbenzene.sdf",
        measured_diamag_sus=-101.7,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="isobutyl_formate.sdf",
        measured_diamag_sus=-66.8,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="isopentane.sdf",
        measured_diamag_sus=-64.4,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="isopentyl_acetate.sdf",
        measured_diamag_sus=-89.4,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="isopentyl_formate.sdf",
        measured_diamag_sus=-78.4,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="isophthalic_acid.sdf",
        measured_diamag_sus=-84.6,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="isopropenylbenzene.sdf",
        measured_diamag_sus=-80.0,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="isopropyl_acetate.sdf",
        measured_diamag_sus=-67.0,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="isopropylbenzene.sdf",
        measured_diamag_sus=-89.5,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-isopropyl-4-methylbenzene.sdf",
        measured_diamag_sus=-102.8,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="isoquinoline.sdf",
        measured_diamag_sus=-83.9,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="D-limonene.sdf",
        measured_diamag_sus=-98.0,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="maleic_acid.sdf",
        measured_diamag_sus=-49.6,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="maleic_anhydride.sdf",
        measured_diamag_sus=-35.8,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="methane.sdf",
        measured_diamag_sus=-17.4,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="methanol.sdf",
        measured_diamag_sus=-21.4,
        literature_reference="[2] 3-578",
        description="exp data = calcd data",
        skip_test=True,
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-methoxyaniline.sdf",
        measured_diamag_sus=-79.1,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="methylamine.sdf",
        measured_diamag_sus=-27.0,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-methylaniline.sdf",
        measured_diamag_sus=-74.9,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="3-methylaniline.sdf",
        measured_diamag_sus=-74.6,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="4-methylaniline.sdf",
        measured_diamag_sus=-72.5,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="N-methylaniline.sdf",
        measured_diamag_sus=-74.1,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="methyl_benzoate.sdf",
        measured_diamag_sus=-81.6,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-methyl-1,3-butadiene.sdf",
        measured_diamag_sus=-46.0,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="3-methylbutanoic_acid.sdf",
        measured_diamag_sus=-67.7,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-methyl-2-butene.sdf",
        measured_diamag_sus=-54.7,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="methylcyclohexane.sdf",
        measured_diamag_sus=-78.9,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="methylcyclopentane.sdf",
        measured_diamag_sus=-70.2,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="methyl_formate.sdf",
        measured_diamag_sus=-31.1,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="4-methylheptane.sdf",
        measured_diamag_sus=-97.3,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="methyl_methacrylate.sdf",
        measured_diamag_sus=-57.3,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-methylnaphthalene.sdf",
        measured_diamag_sus=-102.9,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-methylnaphthalene.sdf",
        measured_diamag_sus=-102.7,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="methyloxirane.sdf",
        measured_diamag_sus=-42.5,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-methylpentane.sdf",
        measured_diamag_sus=-75.3,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="3-methylpentane.sdf",
        measured_diamag_sus=-75.5,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="4-methyl-2-pentanol.sdf",
        measured_diamag_sus=-80.4,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="4-methyl-2-pentanone.sdf",
        measured_diamag_sus=-69.7,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="methyl_propanoate.sdf",
        measured_diamag_sus=-54.5,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-methylpropanoic_acid.sdf",
        measured_diamag_sus=-56.1,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-methyl-1-propanol.sdf",
        measured_diamag_sus=-57.6,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-methyl-2-propanol.sdf",
        measured_diamag_sus=-56.6,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="4-methylpyridine.sdf",
        measured_diamag_sus=-59.8,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="methyl_salicylate.sdf",
        measured_diamag_sus=-86.3,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="morpholine.sdf",
        measured_diamag_sus=-55.0,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="naphthalene.sdf",
        measured_diamag_sus=-91.6,
        literature_reference="[2] 3-578",
        description="exp data = calcd data",
        skip_test=True,
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-naphthol.sdf",
        measured_diamag_sus=-96.2,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-naphthol.sdf",
        measured_diamag_sus=-96.8,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-naphthylamine.sdf",
        measured_diamag_sus=-92.5,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-naphthylamine.sdf",
        measured_diamag_sus=-98.0,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="neopentane.sdf",
        measured_diamag_sus=-63.0,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-nitroaniline.sdf",
        measured_diamag_sus=-67.4,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="3-nitroaniline.sdf",
        measured_diamag_sus=-69.7,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="4-nitroaniline.sdf",
        measured_diamag_sus=-68.0,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="nitrobenzene.sdf",
        measured_diamag_sus=-61.8,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="nitroethane.sdf",
        measured_diamag_sus=-35.4,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="nitromethane.sdf",
        measured_diamag_sus=-21.0,
        literature_reference="[2] 3-578",
        description="exp data = calcd data",
        skip_test=True,
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-nitrophenol.sdf",
        measured_diamag_sus=-68.9,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="3-nitrophenol.sdf",
        measured_diamag_sus=-65.9,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="4-nitrophenol.sdf",
        measured_diamag_sus=-66.9,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-nitropropane.sdf",
        measured_diamag_sus=-45.0,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-nitropropane.sdf",
        measured_diamag_sus=-45.4,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2-nitrotoluene.sdf",
        measured_diamag_sus=-72.2,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="3-nitrotoluene.sdf",
        measured_diamag_sus=-72.7,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="4-nitrotoluene.sdf",
        measured_diamag_sus=-73.3,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="nonane.sdf",
        measured_diamag_sus=-108.1,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-nonene.sdf",
        measured_diamag_sus=-100.1,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="cis-9-octadecenoic_acid.sdf",
        measured_diamag_sus=-208.5,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="octane.sdf",
        measured_diamag_sus=-96.6,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="octanoic_acid.sdf",
        measured_diamag_sus=-99.5,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-octanol.sdf",
        measured_diamag_sus=-101.6,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1-octene.sdf",
        measured_diamag_sus=-88.8,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="oxirane.sdf",
        measured_diamag_sus=-30.5,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="paraldehyde.sdf",
        measured_diamag_sus=-86.1,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="pentachloroethane.sdf",
        measured_diamag_sus=-99.1,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="pentanal.sdf",
        measured_diamag_sus=-57.5,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="pentane.sdf",
        measured_diamag_sus=-63.1,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="1,5-pentanediol.sdf",
        measured_diamag_sus=-73.5,
        literature_reference="[2] 3-578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="2,4-pentanedione.sdf",
        measured_diamag_sus=-54.9,
        literature_reference="[2] 3-579",
    ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # Platinum compounds
    DataQualityDiamagContrTestsSDF(
        sdf_file="[Pt((NH2)2CS}4]Cl2.sdf",
        measured_diamag_sus=-246.5,
        literature_reference="No. 1845",
    ),
    # Niobium compounds
    DataQualityDiamagContrTestsSDF(
        sdf_file="[NbCp2]Br3.sdf",
        measured_diamag_sus=-240.0,
        literature_reference="No. 1503",
    ),
    # Nickel compounds
    DataQualityDiamagContrTestsSDF(
        sdf_file="[Ni(imam)2](BF4)2.sdf",
        measured_diamag_sus=-111.0,
        literature_reference="No. 1349",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Ni(L1).sdf",
        measured_diamag_sus=-56.0,
        literature_reference="No. 1361",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[Ni(EtS)2].sdf",
        measured_diamag_sus=-77.8,
        literature_reference="No. 1299",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[Ni{P(Et)(OH)S2}2].sdf",
        measured_diamag_sus=-247.0,
        literature_reference="No. 1301",
    ),
    # Zinc compounds
    DataQualityDiamagContrTestsSDF(
        sdf_file="[Zn{Ph(NO3)(NHNH2)}]Br2_5H2O.sdf",
        measured_diamag_sus=-444.2,
        literature_reference="No. 2929",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Zn3(cit)3_2H2O.sdf",
        measured_diamag_sus=-246.0,
        literature_reference="No. 2923",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Zn(AcO)2_2H2O.sdf",
        measured_diamag_sus=-100.9,
        literature_reference="No. 2900",
    ),
    # Silicon compounds
    DataQualityDiamagContrTestsSDF(
        sdf_file="HSiPr3.sdf",
        measured_diamag_sus=-130.0,
        literature_reference="No. 2313",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="K2SiO3.sdf",
        measured_diamag_sus=-59.0,
        literature_reference="No. 2048",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="MeSiBr3.sdf",
        measured_diamag_sus=-115.5,
        literature_reference="No. 2229",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Si_N_heterocycle.sdf",
        measured_diamag_sus=-81.8,
        literature_reference="No. 2247",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Me3SiOAc.sdf",
        measured_diamag_sus=-86.09,
        literature_reference="No. 2255",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="PhSiCl3.sdf",
        measured_diamag_sus=-120.4,
        literature_reference="No. 2262",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Si(AcO)4.sdf",
        measured_diamag_sus=-129.25,
        literature_reference="No. 2295",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Me2Si(OEt){ON=C(Pr)NH2}.sdf",
        measured_diamag_sus=-135.8,
        literature_reference="No. 2301",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="BrPh+N_S_Si_cycle.sdf",
        measured_diamag_sus=-199.37,
        literature_reference="No. 2329",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(Ph2SiO)4.sdf",
        measured_diamag_sus=-485.3,
        literature_reference="No. 2369",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Me3Si-NH-C(Ph)=N-O-SiMe3.sdf",
        measured_diamag_sus=-199.5,
        literature_reference="No. 2344",
    ),
    # Nitrogen compounds
    DataQualityDiamagContrTestsSDF(
        sdf_file="HNO3.sdf",
        measured_diamag_sus=-19.91,
        literature_reference="No. 1559",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="NH4NO3.sdf",
        measured_diamag_sus=-32.6,
        literature_reference="No. 1565",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(NH4)3(cit).sdf",
        measured_diamag_sus=-109.5,
        literature_reference="No. 1534",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(Ph-C=C-COO)(NH4).sdf",
        measured_diamag_sus=-98.5,
        literature_reference="No. 1537",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[HOC](AsF6)2.sdf",
        measured_diamag_sus=-334.0,
        literature_reference="No. 1539",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[HOC](PF6)2.sdf",
        measured_diamag_sus=-277.0,
        literature_reference="No. 1542",
    ),
    # Test fails due to lack of pascal constant for Sb(V) oxidation state
    # TODO - resolve fails for cases with no data by taking first availbale, most relevant Pascal constant
    DataQualityDiamagContrTestsSDF(
        sdf_file="[HOC](SbF6)2.sdf",
        measured_diamag_sus=-430.0,
        literature_reference="No. 1545",
        skip_test=True,
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[HOC].sdf",
        measured_diamag_sus=-190.0,
        literature_reference="No. 1546",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[HOC](CF3SO3)2.sdf",
        measured_diamag_sus=-344.0,
        literature_reference="No. 1548",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[HOC][C(CN)3]2.sdf",
        measured_diamag_sus=-266.0,
        literature_reference="No. 1550",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(NH4)2(CO3)_2H2O.sdf",
        measured_diamag_sus=-68.62,
        literature_reference="No. 1520",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[NMe4]Br.sdf",
        measured_diamag_sus=-87.2,
        literature_reference="No. 1530",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[NMe4]I.sdf",
        measured_diamag_sus=-105.0,
        literature_reference="No. 1531",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(PhCOO)(NH4).sdf",
        measured_diamag_sus=-77.98,
        literature_reference="No. 1535",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(HOPhCOO)(NH4).sdf",
        measured_diamag_sus=-86.49,
        literature_reference="No. 1536",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="NH4Cl.sdf",
        measured_diamag_sus=-36.7,
        literature_reference="No. 1551",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[NH3OH]Cl.sdf",
        measured_diamag_sus=-42.4,
        literature_reference="No. 1552",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(NH4)(ClO3).sdf",
        measured_diamag_sus=-42.1,
        literature_reference="No. 1553",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(NH4)(ClO4).sdf",
        measured_diamag_sus=-46.3,
        literature_reference="No. 1554",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(NH4)MgCl3.sdf",
        measured_diamag_sus=-82.97,
        literature_reference="No. 1556",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="NH4F.sdf",
        measured_diamag_sus=-23.5,
        literature_reference="No. 1558",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(NH4)(IO3).sdf",
        measured_diamag_sus=-62.3,
        literature_reference="No. 1562",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(NH4)MgI3.sdf",
        measured_diamag_sus=-171.14,
        literature_reference="No. 1563",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(NHS)4.sdf",
        measured_diamag_sus=-88.0,
        literature_reference="No. 1566",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(NH4)(H2PO4).sdf",
        measured_diamag_sus=-61.0,
        literature_reference="No. 1567",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(NH4)2(S2O3).sdf",
        measured_diamag_sus=-75.1,
        literature_reference="No. 1568",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(NH4)2(SO4).sdf",
        measured_diamag_sus=-67.0,
        literature_reference="No. 1569",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(NH4)2(TeO4).sdf",
        measured_diamag_sus=-80.15,
        literature_reference="No. 1570",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(NH4)2(S2O8).sdf",
        measured_diamag_sus=-103.8,
        literature_reference="No. 1571",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(NH4)2(HPO4).sdf",
        measured_diamag_sus=-71.0,
        literature_reference="No. 1572",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(NH4)2(SO3)_H2O.sdf",
        measured_diamag_sus=-70.3,
        literature_reference="No. 1573",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="(NH4)MgI3_6H2O.sdf",
        measured_diamag_sus=-250.9,
        literature_reference="No. 1575",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="N2.sdf",
        measured_diamag_sus=-12.04,
        literature_reference="No. 1576",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="[-N]=[N+]=O_resonance_form_of_N2O.sdf",
        measured_diamag_sus=-18.9,
        literature_reference="No. 1577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="N#[N+]-[O-]_resonance_form_of_N2O.sdf",
        measured_diamag_sus=-18.9,
        literature_reference="No. 1577",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="N2O2.sdf",
        measured_diamag_sus=-25.4,
        literature_reference="No. 1578",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="N2O3.sdf",
        measured_diamag_sus=-23.2,
        literature_reference="No. 1579",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="N2O4.sdf",
        measured_diamag_sus=-25.2,
        literature_reference="No. 1580",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="N2O5.sdf",
        measured_diamag_sus=-35.6,
        literature_reference="No. 1581",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="N4S4.sdf",
        measured_diamag_sus=-102.0,
        literature_reference="No. 1582",
    ),
    # Osmium compounds
    DataQualityDiamagContrTestsSDF(
        sdf_file="K4[Os(CN6)]_3H2O.sdf",
        measured_diamag_sus=-223.8,
        literature_reference="No. 1589",
    ),
    DataQualityDiamagContrTestsSDF(
        sdf_file="Os(cp)2.sdf",
        measured_diamag_sus=-193.0,
        literature_reference="No. 1591",
    ),
    # TODO No Os(0) constant available - use Os(II) constant instead
    DataQualityDiamagContrTestsSDF(
        sdf_file="[Os(CO)4]3.sdf",
        measured_diamag_sus=-293.0,
        literature_reference="No. 1592",
        skip_test=True,
    ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
    # DataQualityDiamagContrTestsSDF(
    #     sdf_file="",
    #     measured_diamag_sus=,
    #     literature_reference="",
    # ),
]
