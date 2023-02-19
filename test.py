class Category:

    def __init__(self, name, facing, width, height, thickness, price, weight):
        self.name = name
        self.facing = facing
        self.width = width
        self.height = height
        self.thickness = thickness
        self.price = price
        self.weight = weight

    def __str__(self):
        return self.name


class EnterDoors(Category):

    def __init__(self, side, noise_reduction, temperature_reduction, thermo, layer, peephole, lock, name, facing, width,
                 height, thickness, price, weight):
        super().__init__(name, facing, width, height, thickness, price, weight)
        self.side = side
        self.noise_reduction = noise_reduction
        self.temperature_reduction = temperature_reduction
        self.thermo = thermo
        self.layer = layer
        self.peephole = peephole
        self.lock = lock


class InteriorDoors(Category):
    pass
    # def __init__(self, name, side, facing, noise_reduction):
    #     super().__init__(name)
    #     self.side = side
    #     self.facing = facing
    #     self.noise_reduction = noise_reduction
    #     self.temperature_reduction = temperature_reduction
    #     self.thermo = thermo
    #     self.layer = layer
    #     self.peephole = peephole
    #     self.lock = lock


class Furniture(Category):
    furniture = Category('Фурнитура')


class MeterProducts(Category):
    meter_products = Category('Погонажные изделия')


class Factory:

    def __init__(self, name, *category: Category.__class__):
        self.name = name
        self.category = category

    def __str__(self):
        return self.name


class FactoriesList(Factory):
    kd = Factory('Краснодеревщик', EnterDoors, InteriorDoors)
    sofia = Factory('Sofia', InteriorDoors, MeterProducts, Furniture)
    guardian = Factory('Гардиан', EnterDoors)
    gran = Factory('Грань', EnterDoors)
    mezzo_porte = Factory('Mezzo Porte', InteriorDoors, MeterProducts)
    vell_doris = Factory('Vell Doris', InteriorDoors, MeterProducts)
    synergy = Factory('Synergy', InteriorDoors, MeterProducts)
    morelli = Factory('Morelli', Furniture)
    ruchetti = Factory('Ruchetti', Furniture)
    punto = Factory('Punto', Furniture)
    fuaro = Factory('Fuaro', Furniture)


class ModelLine:

    def __init__(self, name, factory: Factory):
        self.name = name
        self.factory = factory

    def __str__(self):
        return self.name


class ModelLineList(ModelLine):
    # KdModels:
    kd_200 = ModelLine('200', FactoriesList.kd)
    kd_500 = ModelLine('500', FactoriesList.kd)
    kd_700 = ModelLine('700', FactoriesList.kd)
    kd_3000 = ModelLine('3000', FactoriesList.kd)
    kd_5000 = ModelLine('5000', FactoriesList.kd)
    kd_6000 = ModelLine('6000', FactoriesList.kd)
    kd_7000 = ModelLine('7000', FactoriesList.kd)

    # SofiaModels:
    sofia_original = ModelLine('Original', FactoriesList.sofia)
    sofia_bridge = ModelLine('Bridge', FactoriesList.sofia)
    sofia_classic = ModelLine('Classic', FactoriesList.sofia)
    sofia_smart = ModelLine('Smart', FactoriesList.sofia)
    sofia_skyline = ModelLine('Skyline', FactoriesList.sofia)
    sofia_rain = ModelLine('Rain', FactoriesList.sofia)
    sofia_light = ModelLine('Light', FactoriesList.sofia)

    # SynergyModels:
    synergy_hi_tech = ModelLine('Хай тек', FactoriesList.synergy)
    synergy_modern = ModelLine('Модерн', FactoriesList.synergy)
    synergy_loft = ModelLine('Лофт', FactoriesList.synergy)
    synergy_english_classic = ModelLine('Английская классика', FactoriesList.synergy)

    # VellDorisModels:
    vell_doris_S = ModelLine('S', FactoriesList.vell_doris)
    vell_doris_F = ModelLine('F', FactoriesList.vell_doris)
    vell_doris_R = ModelLine('R', FactoriesList.vell_doris)
    vell_doris_X = ModelLine('X', FactoriesList.vell_doris)

    # MezzoPorteModels:
    mezzo_porte_focus = ModelLine('Focus', FactoriesList.mezzo_porte)
    mezzo_porte_elegant = ModelLine('Elegant', FactoriesList.mezzo_porte)
    mezzo_porte_design = ModelLine('Design', FactoriesList.mezzo_porte)

    # GuardianModels:
    guardian_ds1 = ModelLine('ДС1', FactoriesList.guardian)
    guardian_ds2 = ModelLine('ДС2', FactoriesList.guardian)
    guardian_ds3 = ModelLine('ДС3', FactoriesList.guardian)
    guardian_ds6 = ModelLine('ДС6', FactoriesList.guardian)
    guardian_ds9 = ModelLine('ДС9', FactoriesList.guardian)

    # GranModels:
    gran_100 = ModelLine('100', FactoriesList.gran)
    gran_110 = ModelLine('110', FactoriesList.gran)


class Model:

    def __init__(self, name, model_line: ModelLine):
        self.name = name
        self.model_line = model_line

    def __str__(self):
        return self.name


class ModelList(Model):
    # Kd200:
    kd_200 = Model('200', ModelLineList.kd_200)
    kd_201 = Model('201', ModelLineList.kd_200)
    kd_204 = Model('204', ModelLineList.kd_200)
    kd_206 = Model('206', ModelLineList.kd_200)
    kd_208 = Model('208', ModelLineList.kd_200)

    # Kd700:
    kd_700 = Model('700', ModelLineList.kd_700)
    kd_700m = Model('700m', ModelLineList.kd_700)
    kd_701 = Model('701', ModelLineList.kd_700)
    kd_703 = Model('703', ModelLineList.kd_700)
    kd_703m = Model('703m', ModelLineList.kd_700)
    kd_705 = Model('705', ModelLineList.kd_700)

    # Kd3000:
    kd_3323 = Model('3323', ModelLineList.kd_3000)
    kd_3324 = Model('3324', ModelLineList.kd_3000)
    kd_3340 = Model('3340', ModelLineList.kd_3000)
    kd_3342 = Model('3342', ModelLineList.kd_3000)
    kd_3343 = Model('3343', ModelLineList.kd_3000)
    kd_3344 = Model('3344', ModelLineList.kd_3000)
    kd_3350 = Model('3350', ModelLineList.kd_3000)
    kd_3352 = Model('3352', ModelLineList.kd_3000)

    # Kd5000:
    kd_5066 = Model('5066', ModelLineList.kd_5000)
    kd_5033 = Model('5033', ModelLineList.kd_5000)
    kd_5002 = Model('5002', ModelLineList.kd_5000)
    kd_5004 = Model('5004', ModelLineList.kd_5000)

    # Kd6000:
    kd_6323 = Model('6323', ModelLineList.kd_6000)
    kd_6324 = Model('6324', ModelLineList.kd_6000)
    kd_6339 = Model('6339', ModelLineList.kd_6000)
    kd_6340 = Model('6340', ModelLineList.kd_6000)
    kd_6342 = Model('6342', ModelLineList.kd_6000)
    kd_6343 = Model('6343', ModelLineList.kd_6000)
    kd_6344 = Model('6344', ModelLineList.kd_6000)

    # Kd7000:
    kd_7000 = Model('7000', ModelLineList.kd_7000)
    kd_7002 = Model('7002', ModelLineList.kd_7000)
    kd_7004 = Model('7004', ModelLineList.kd_7000)

    # SofiaOriginal:
    sofia_01 = Model('.01', ModelLineList.sofia_original)
    sofia_02 = Model('.02', ModelLineList.sofia_original)
    sofia_03 = Model('.03', ModelLineList.sofia_original)
    sofia_04 = Model('.04', ModelLineList.sofia_original)
    sofia_07 = Model('.07', ModelLineList.sofia_original)

    # SofiaBridge:
    sofia_71 = Model('.71', ModelLineList.sofia_bridge)
    sofia_72 = Model('.72', ModelLineList.sofia_bridge)
    sofia_75 = Model('.75', ModelLineList.sofia_bridge)

    # SofiaBridge:
    sofia_51 = Model('.51', ModelLineList.sofia_classic)
    sofia_52 = Model('.52', ModelLineList.sofia_classic)
    sofia_53 = Model('.53', ModelLineList.sofia_classic)

    # SofiaSmart:
    sofia_31 = Model('.31', ModelLineList.sofia_smart)
    sofia_32 = Model('.32', ModelLineList.sofia_smart)

    # SofiaSkyline:
    sofia_94 = Model('.94', ModelLineList.sofia_skyline)
    sofia_102 = Model('.102', ModelLineList.sofia_skyline)
    sofia_103 = Model('.103', ModelLineList.sofia_skyline)
    sofia_104 = Model('.104', ModelLineList.sofia_skyline)

    # SofiaRain:
    sofia_21 = Model('.21', ModelLineList.sofia_rain)
    sofia_22 = Model('.22', ModelLineList.sofia_rain)
    sofia_23 = Model('.23', ModelLineList.sofia_rain)

    # SofiaLight:
    sofia_10 = Model('.10', ModelLineList.sofia_light)
    sofia_105 = Model('.105', ModelLineList.sofia_light)
    sofia_106 = Model('.106', ModelLineList.sofia_light)

    # SynergyLoft:
    synergy_skandinavia_1 = Model('Скандинавия 1', ModelLineList.synergy_loft)
    synergy_skandinavia_2 = Model('Скандинавия 2', ModelLineList.synergy_loft)
    synergy_skandinavia_3 = Model('Скандинавия 3', ModelLineList.synergy_loft)

    # SynergyEnglishClassic:
    synergy_verona_1 = Model('Верона 1', ModelLineList.synergy_english_classic)
    synergy_verona_3 = Model('Верона 2', ModelLineList.synergy_english_classic)
    synergy_verona_2 = Model('Верона 3', ModelLineList.synergy_english_classic)

    # SynergyHiTech:
    synergy_strong_1 = Model('Стронг 1', ModelLineList.synergy_hi_tech)
    synergy_strong_2 = Model('Стронг 2', ModelLineList.synergy_hi_tech)
    synergy_lira_1 = Model('Лира', ModelLineList.synergy_hi_tech)

    # SynergyHiTech:
    synergy_legro = Model('Легро', ModelLineList.synergy_modern)
    synergy_kianty = Model('Кьянти', ModelLineList.synergy_modern)
    synergy_trio = Model('Трио', ModelLineList.synergy_modern)


if __name__ == "__main__":
    i = ("df", "dsaf")
    print(i)
    print(FactoriesList.kd.category.__getitem__(0).__str__())
    print(CategoriesList.enter_doors)
