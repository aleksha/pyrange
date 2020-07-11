# (file_name, normal density, list of aliases)
from collections import namedtuple
material_tuple = namedtuple('material_tuple','filename density names')

registry = [
    ("Hydrogen.txt", 0.0000899, ["H", "H2", "Hydrogen", "Водород", "Wasserstoff", "Hydrogène", "Idrogeno", "Hidrógeno"]),
    ("Helium.txt", 0.0001753, ["He", "Helium", "Гелий", "Hélium", "Elio", "Helio"]),
    ("Beryllium.txt", 1.848, ["Be", "Beryllium", "Бериллий", "Béryllium", "Berilio", "Berillio"]),
    ("Aluminum.txt", 2.70, ["Al", "Aluminum", "Aluminium", "Алюминий", "Aluminio", "Alluminio"]),
    ("Argon.txt", 1.784e-3, ["Ar", "Argon", "Аргон", "Argo", "Argón"]),
    ("Carbon Amorphous (density20gcm3).txt", 2.0, ["C", "Carbon", "Углерод", "Kohlenstoff", "Carbono", "Carbonio"]),
    ("Copper.txt", 8.96, ["Cu", "Copper", "Медь", "Kupfer", "Cobre", "Rame"]),
    ("Gadolinium.txt", 7.9, ["Gd", "Gadolinium", "Гадолиний", "Gadolinio"]),
    ("Germanium.txt", 5.323, ["Ge", "Germanium", "Германий", "Germanio"]),
    ("Gold.txt", 19.30, ["Au", "Gold", "Золото", "Oro"]),
    ("Graphite (density 17 gcm3).txt", 1.7, ["Graphite", "Графит", "Graphit", "Grafit", "Grafito", "Grafite"]),
    ("Iron.txt", 7.874, ["Fe", "Iron", "Железо", "Eisen", "Ferro", "Hierro", "Fierro"]),
    ("Krypton.txt", 0.003749, ["Kr", "Krypton", "Криптон", "Kripton", "Kripto", "Cripto", "Kriptón", "Criptón"]),
    ("Lead.txt", 11.34, ["Pb", "Lead", "Свинец", "Blei", "Plomo", "Piombo"]),
    ("Molybdenum.txt", 10.28, ["Mo", "Molybdenum", "Молибден", "Molybdän", "Molibdeno"]),
    ("Neon.txt", 0.9002e-3, ["Ne", "Neon", "Неон", "Neo", "Neón"]),
    ("Nitrogen.txt", 0.0012506, ["N","Nitrogen", "Азот", "Stickstoff", "Azoto", "Nitrógeno"]),
    ("Oxygen.txt", 1.429e-3, ["O", "Oxygen", "Кислород", "Sauerstoff", "Oxígeno", "Ossigeno"]),
    ("Platinum.txt", 21.45, ["Pt", "Platinum", "Платина", "Platin", "Platino"]),
    ("Silicon.txt", 2.33, ["Si", "Silicon", "Кремний", "Silicium", "Silizium", "Silicio"]),
    ("Silver.txt", 10.49, ["Ag", "Silver", "Серебро", "Silber", "Argento", "Plata"]),
    ("Tin.txt", 7.265, ["Sn", "Tin", "Олово", "Zinn", "Stagno", "Estaño"]),
    ("Titanium.txt", 4.506, ["Ti", "Titanium", "Титан", "Titanio"]),
    ("Tungsten.txt", 19.3, ["W", "Tungsten", "Wolfram", "Вольфрам", "Tungsteno", "Wolframio", "Volframio", "Wólfram"]),
    ("Uranium.txt", 19.1, ["U", "Uranium", "Уран", "Uran", "Uranio"]),
    ("Xenon.txt", 0.005894, ["Xe", "Xenon", "Ксенон", "Xeno", "Xenón"]),


    ("Polyethylene Terephthalate (Mylar).txt", 1.4, ["Mylar","Polyethylene terephthalate","Майлар","Полиэтилентерефталат", "Лавсан"]),
    ("Methane.txt", 0.000667151, ["Methane", "Метан"]),
    ("Polystyrene.txt", 1.06, ["Polystyrene", "Полистирол"]),
    ("Polyvinyl Chloride.txt", 1.3, ["Polyvinyl chloride", "PVC", "Поливинилхлорид", "Полихлорвинил", "ПВХ"]),
    ("Cellulose Nitrate.txt", 1.49, ["Cellulose nitrate", "Nitrocellulose", "Нитроцеллюлоза"]),
    ("Aluminum Oxide.txt", 3.97, ["Aluminum oxide", "Aluminium Oxide", "Оксид алюминия"]),
    ("Acetylene.txt", 0.0010967, ["Acetylene", "Ацетилен"]),
    ("Carbon Dioxide.txt", 0.00184212, ["Carbon dioxide", "Диоксид углерода", "Двуокись углерода"]),
    ("Propane.txt", 0.00187939, ["Propane", "Пропан"]),
    ("Sodium Iodide.txt", 3.667, ["Sodium iodide", "Иодид натрия", "Иодистый натрий"]),
    ("Ethylene.txt", 0.00117497, ["Ethylene", "Этилен", "Этен"]),
    ("Calcium Fluoride.txt", 3.18, ["Calcium fluoride", "Фторид кальция"]),
    ("Polypropylene.txt", 0.9, ["Polypropylene", "Полипропилен"]),
    ("Polytetrafluoroethylene (Teflon).txt", 2.2, ["Polytetrafluoroethylene", "Teflon", "Тефлон", "Политетрафторэтилен", "Фторопласт-4"]),
    ("Paraffin Wax.txt", 0.93, ["Paraffin wax", "Petroleum wax", "Парафин"]),
    ("Silicon Dioxide.txt", 2.32, ["Silicon dioxide","Silica","Диоксид кремния"]),
    ("Kapton Polyimide Film.txt", 1.42, ["Kapton", "Каптон"]),
    ("Stilbene.txt", 0.9707, ["Stilbene","Стильбен"]),
    ("Photographic Emulsion.txt", 1.2914, ["Photographic emulsion", "Фотоэмульсия"]),
    ("Toluene.txt", 0.8669, ["Toluene", "Toluol", "Толуол"]),
    ("Lithium Fluoride.txt", 2.635, ["Lithium fluoride", "Фторид лития", "Фтористый литий"]),
    ("Cesium Iodide.txt", 4.51, ["Cesium iodide", "Caesium iodide", "Иодид цезия"]),
    ("Water Liquid.txt", 1, ["Water", "Вода"]),
    ("Air Dry (near sea level).txt", 0.00120479, ["Air", "Воздух"]),
    ("Water Vapor.txt", 0.000756182, ["Water vapor", "Водяной пар"]),
    ("Lithium Tetraborate.txt", 2.44, ["Lithium tetraborate", "Тетраборат лития"]),
    ("Polyethylene.txt", 0.94, ["Polyethylene", "Полиэтилен"]),


    ("Muscle Striated.txt", 1.04, ["Muscle, striated"]),
    ("Muscle Skeletal.txt", 1.05, ["Muscle, skeletal"]),
    ("Muscle-Equivalent Liquid without Sucrose.txt", 1.07, ["Muscle-equivalent liquid, without sucrose"]),
    ("Muscle-Equivalent Liquid with Sucrose.txt", 1.11, ["Muscle-equivalent liquid, with sucrose"]),
    ("Bone Cortical (ICRP).txt", 1.92, ["Bone, cortical (ICRP)"]),
    ("Bone Compact (ICRU).txt", 1.85, ["Bone, compact (ICRU)"]),
    ("MS20 Tissue Substitute.txt", 1, ["MS20 tissue substitute"]),
    ("A-150 Tissue-Equivalent Plastic.txt", 1.127, ["A-150 tissue-equivalent plastic"]),
    ("C-552 Air-Equivalent Plastic.txt", 1.76, ["C-552 air-equivalent plastic"]),
    ("B-100 Bone-Equivalent Plastic.txt", 1.45, ["B-100 bone-equivalent plastic"]),
    ("Tissue-Equivalent GAS (Propane based).txt", 0.00182628, ["Tissue-equivalent gas (propane based)"]),
    ("Tissue-Equivalent GAS (Methane based).txt", 0.00106409, ["Tissue-equivalent gas (methane based)"]),
    ("Adipose Tissue (ICRP).txt", 0.95, ["Adipose tissue (ICRP)"]),
    
    ("Glass Pyrex.txt", 2.23 , ["Glass, Pyrex"]),
    ("M3 Wax.txt", 1.05, ["M3 wax"]),
    ("Ferrous Sulfate Dosimeter Solution.txt", 1.024, ["Ferrous sulfate dosimeter solution"]),
    ("Ceric Sulfate Dosimeter Solution.txt", 1.03, ["Ceric sulfate dosimeter solution"]),
    ("Polycarbonate (Makrolon Lexan).txt", 1.2, ["Polycarbonate (Makrolon, Lexan)"]),
    ("Polymethyl Methacralate (Lucite Perspex).txt", 1.19, ["Polymethyl methacralate (Lucite, Perspex)"]),
    ("Plastic Scintillator (Vinyltoluene based).txt", 1.032, ["Plastic scintillator (Vinyltoluene based)"]),
    ("Nylon type 6 and type 66.txt", 1.14 ["Nylon, type 6 and type 6/6"]),

]

# convert tuples to named tuples
for i in range(len(registry)):
    registry[i] = material_tuple(*registry[i])

    # make sure all entries are valid
    entry_is_ok = True
    entry_is_ok = entry_is_ok and type(registry[i].filename) == type(str())
    entry_is_ok = entry_is_ok and type(registry[i].density) == type(float())
    entry_is_ok = entry_is_ok and type(registry[i].names) == type(list())
    entry_is_ok = entry_is_ok and len(registry[i]) > 0
    assert entry_is_ok, f'Registry entry {i} is broken'
