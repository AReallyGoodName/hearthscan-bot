# mapped alternative names
alternative_names = {
    'drboom' : 'drbalance',
    'fierywaraxe' : 'fierywinaxe',
    'lordjaraxxus' : 'jaraxxus',
    'alexstrasza' : 'alex',
    'auchenaisoulpriest' : ['auchenai', 'soulpriest'],
    'malygos' : 'maly',
    'pyroblast' : 'pyro',
    'mysteriouschallenger' : 'mc',
    'ragnarosthefirelord' : ['ragnaros', 'rag'],
    'tirionfordring' : 'tirion',
    'archmageantonidas' : 'antonidas',
    'ancientofwar' : 'aow',
    'ancientoflore' : 'aol',
    'prophetvelen' : 'velen',
    'emperorthaurissan' : ['emperor', 'thaurissan'],
    'illidanstormrage' : 'illidan',
    'sylvanaswindrunner' : 'sylvanas',
    'antiquehealbot' : 'healbot',
    'grimpatron' : 'patron',
    'sludgebelcher' : 'belcher',
    'truesilverchampion' : 'truesilver',
    'polymorph' : 'sheep',
    'hex' : 'frog',
    'kezanmystic' : 'kezan',
    'biggamehunter' : 'bgh',
    'mindcontroltech' : 'mct',
    'lorewalkercho' : 'cho',
    'millhousemanastorm' : 'millhouse',
    'shieldedminibot' : 'minibot',
    'sorcerersapprentice' : 'apprentice',
    'northshirecleric' : 'northshire',
    'defenderofargus' : 'argus',
    'pilotedshredder' : 'shredder',
    'hemetnesingwary' : 'hemet',
    'ironbeakowl' : 'owl',
    'sunfuryprotector' : 'sunfury',
    'senjinshieldmasta' : 'tazdingo',
    'preparation' : 'prep',
    'theblackknight' : ['tbk', 'blackknight'],
    'elitetaurenchieftain' : 'etc',
    'harrisonjones' : ['harrison', 'jones'],
    'flamewaker' : 'flamewalker',
    'kelthuzad' : 'kel',
    'eydisdarkbane' : ['darkbane', 'eydis'],
    'fjolalightbane' : ['lightbane', 'fjola'],
    'velenschosen' : 'velens',
    'varianwrynn' : 'varian',
    'polymorphboar' : 'boar',
    'themistcaller' : 'mistcaller',
    'confessorpaletress' : ['confessor', 'paletress'],
    'theskeletonknight' : 'skeletonknight',
    'nexuschampionsaraad' : ['sarad', 'saraad'],
    'edwinvancleef' : ['edwin', 'vancleef'],
    'gormoktheimpaler' : 'gormok',
    'eadricthepure' : 'eadric',
    'anubarak' : 'anub',
    'wilfredfizzlebang' : ['wilfred', 'fizzlebang'],
    'summoningportal' : 'portal',
    'cairnebloodhoof' : 'cairne',
    'draeneitotemcarver' : 'totemcarver',
    'justicartrueheart' : ['justicar', 'trueheart'],
    'sneedsoldshredder' : 'sneeds',
    'alakirthewindlord' : 'alakir',

    'archthiefrafaam' : 'rafaam',
    'renojackson' : ['reno', 'jackson'],
    'djinniofzephyrs' : ['genie', 'djinni'],
    'elisestarseeker' : ['elise', 'starseeker'],
    'brannbronzebeard' : 'brann',
    'forgottentorch' : 'torch',
    'explorershat' : 'hat',
    'maptothegoldenmonkey' : 'map',
    'sirfinleymrrgglton' : ['sirfinley', 'finley'],

    'hallazealtheascended' : 'hallazeal',
    'tentacleofnzoth' : 'tentacle',
    'nzoththecorruptor' : 'nzoth',
    'theboogeymonster' : 'boogeymonster',
    'xarilpoisonedmind' : 'xaril',
    'muklatyrantofthevale' : 'muklatyrant',
    'yshaarjrageunbound' : 'yshaarj',
    'yoggsaronhopesend' : ['yogg', 'yoggsaron', 'rngesus'],

    'medivhtheguardian' : 'medivh',
    'princemalchezaar' : 'malchezaar',
    'thecurator': 'curator'
}

# reverse dict
translations = {}
for org, alts in alternative_names.items():
    if isinstance(alts, list):
        for alt in alts:
            translations[alt] = org
    else:
        translations[alts] = org
