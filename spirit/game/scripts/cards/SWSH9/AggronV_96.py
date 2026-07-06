from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="048c0848-edc8-5b3e-8dad-f3588c2994be",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AggronV.Name",
    display_name="Aggron V",
    searchable_by=["Aggron V", "Basic", "V", "AggronV"],
    subtypes=["Basic", "V"],
    collector_number=96,
    set_code="SWSH9",
    rarity=Rarities.RareHoloV,
    hp=230,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=306,
    abilities=[
        Attack(
            title="Rock Slide",
            game_text="This attack also does 30 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=unimplemented,
        ),
        Attack(
            title="Merciless Strike",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 150 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 4},
            damage=150,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)