from sqlalchemy import create_engine, MetaData, Table

from app import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class Factory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.name'), nullable=False)
    category = db.relationship('Category', backref=db.backref('factories', lazy=True))


class ModelLine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    factory_id = db.Column(db.Integer, db.ForeignKey('factory.id'), nullable=False)
    factory = db.relationship('Factory', backref=db.backref('model_lines', lazy=True))


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    facing = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    model_line_id = db.Column(db.Integer, db.ForeignKey('model_line.id'), nullable=False)
    model_line = db.relationship('ModelLine', backref=db.backref('products', lazy=True))


def getName(self):
    return EnterDoors.name


class Categories:
    enter_doors = Category(name='Межкомнатные двери'),
    interior_doors = Category(name='Межкомнатные двери'),
    furniture = Category(name='Фурнитура'),
    meter_products = Category(name='Погонажные изделия')
    categoriesList = [enter_doors, interior_doors, furniture, meter_products]

    def __repr__(self):
        return self.__dict__


class Factories(Categories):
    kd = Factory(name='Краснодеревщик', category=Categories.enter_doors)
    sofia = Factory(name='Sofia', category=Categories.interior_doors)
    guardian = Factory(name='Гардиан', category=Categories.enter_doors)
    gran = Factory(name='Грань', category=Categories.enter_doors)
    mezzo_porte = Factory(name='Mezzo Porte', category=Categories.interior_doors)
    vell_doris = Factory(name='Vell Doris', category=Categories.interior_doors)
    synergy = Factory(name='Synergy', category=Categories.interior_doors)
    morelli = Factory(name='Morelli', category=Categories.furniture)
    ruchetti = Factory(name='Ruchetti', category=Categories.furniture)
    punto = Factory(name='Punto', category=Categories.furniture)
    fuaro = Factory(name='Fuaro', category=Categories.furniture)
    factoriesList = [kd, sofia, guardian, gran, mezzo_porte, vell_doris, synergy, morelli, ruchetti, punto, fuaro]


class ModelLines(Factories):
    # KdModels:
    _200 = ModelLine(name='200', factory=Factories.kd)
    _700 = ModelLine(name='700', factory=Factories.kd)
    _3000 = ModelLine(name='3000', factory=Factories.kd)
    _5000 = ModelLine(name='5000', factory=Factories.kd)
    _6000 = ModelLine(name='6000', factory=Factories.kd)
    _7000 = ModelLine(name='7000', factory=Factories.kd)
    kdModelsList = [_200, _700, _3000, _5000, _6000, _7000]

    # SofiaModels:
    original = ModelLine(name='Original', factory=Factories.sofia)
    classic = ModelLine(name='Classic', factory=Factories.sofia)
    bridge = ModelLine(name='Bridge', factory=Factories.sofia)
    skyline = ModelLine(name='Skyline', factory=Factories.sofia)
    light = ModelLine(name='Light', factory=Factories.sofia)
    rain = ModelLine(name='Rain', factory=Factories.sofia)
    sofiaModelsList = [original, classic, bridge, skyline, light, rain]

    # SynergyModels:
    hi_tech = ModelLine(name='Хай тек', factory=Factories.synergy)
    modern = ModelLine(name='Модерн', factory=Factories.synergy)
    loft = ModelLine(name='Лофт', factory=Factories.synergy)
    english_classic = ModelLine(name='Английская классика', factory=Factories.synergy)
    synergyModelsList = [hi_tech, modern, loft, english_classic]

    # VellDorisModels:
    S = ModelLine(name='S', factory=Factories.vell_doris)
    F = ModelLine(name='F', factory=Factories.vell_doris)
    R = ModelLine(name='R', factory=Factories.vell_doris)
    X = ModelLine(name='X', factory=Factories.vell_doris)
    vellDorisModelsList = [S, F, R, X]

    # MezzoPorteModels:
    focus = ModelLine(name='Focus', factory=Factories.mezzo_porte)
    elegant = ModelLine(name='Elegant', factory=Factories.mezzo_porte)
    design = ModelLine(name='Design', factory=Factories.mezzo_porte)
    mezzoPorteModelsList = [focus, elegant, design]

    # GuardianModels:
    ds1 = ModelLine(name='ДС1', factory=Factories.guardian)
    ds2 = ModelLine(name='ДС2', factory=Factories.guardian)
    ds3 = ModelLine(name='ДС3', factory=Factories.guardian)
    ds6 = ModelLine(name='ДС6', factory=Factories.guardian)
    ds9 = ModelLine(name='ДС9', factory=Factories.guardian)
    guardianModelsList = [ds1, ds2, ds3, ds6, ds9]

    # GranModels:
    _100 = ModelLine(name='100', factory=Factories.gran)
    _110 = ModelLine(name='110', factory=Factories.gran)
    granModelsList = [_100, _110]

    allModelLinesList = [kdModelsList, sofiaModelsList, synergyModelsList,
                         vellDorisModelsList, mezzoPorteModelsList, guardianModelsList, granModelsList]
    modelLineList = []
    for i in allModelLinesList:
        for j in i:
            modelLineList.append(j)


class Products(ModelLines):
    Product(name='3352', facing='Белый(CPL)', price=150, model='3352', description="sdfas",
            model_line=ModelLines._200)
    Product(name='701', facing='Выбеленный Дуб(Sincrolam)', price=1700, model='701', description="sdfas",
            model_line=ModelLines._700)
    Product(name='5033', facing='Дуб Шервуд(Sincrolam)', price=800, model='5033', description="sdfas",
            model_line=ModelLines._5000)
    Product(name='58.01', facing='Венге', price=900, model='01', description="sdfas", model_line=ModelLines.original)
    Product(name='49.01', facing='Юта', price=120, model='01', description="sdfas", model_line=ModelLines.original)
    Product(name='11.03', facing='Белый шёлк', price=100, model='03', description="sdfas",
            model_line=ModelLines.original)
    Product(name='ДС1', facing='Коричневый баклажан', price=50, model='ДС1', description="sdfas",
            model_line=ModelLines.ds1)
    Product(name='110', facing='Шагрень чёрная', price=70, model='110', description="sdfas", model_line=ModelLines._110)


def clear_db():
    engine = create_engine('sqlite:///shop.db')
    metadata = MetaData(bind=engine)

    category_table = Table('Category', metadata, autoload=True)
    factory_table = Table('Factory', metadata, autoload=True)
    modelLine_table = Table('ModelLine', metadata, autoload=True)
    product_table = Table('Product', metadata, autoload=True)

    category_table.delete().execute()
    factory_table.delete().execute()
    modelLine_table.delete().execute()
    product_table.delete().execute()


def delete_db():
    db.create_all()
    for i in Categories.categoriesList:
        db.session.add(i)
    for i in Factories.factoriesList:
        db.session.add(i)
    for i in ModelLines.modelLineList:
        db.session.add(i)
        db.session.commit()


def add_db():
    db.create_all()
    for i in Categories.categoriesList:
        db.session.add(i)
    for i in Factories.factoriesList:
        db.session.add(i)
    for i in ModelLines.modelLineList:
        db.session.add(i)
        db.session.commit()


if __name__ == "__main__":
    add_db()
