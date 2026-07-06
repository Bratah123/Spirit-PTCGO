from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fa5391b4-9541-5280-9740-959adc2c715a",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WobbuffetV.Name",
    display_name="Wobbuffet V",
    searchable_by=["Wobbuffet V", "Basic", "V", "WobbuffetV"],
    subtypes=["Basic", "V"],
    collector_number=191,
    set_code="SWSH1",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=202,
    abilities=[
        Attack(
            title="Gritty Comeback",
            game_text="Switch all damage counters on this Pok\u00e9mon with those on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Shadow Bind",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=70,
            effect=unimplemented,
        ),
    ],
)