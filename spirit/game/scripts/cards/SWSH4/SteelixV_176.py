from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="747509a6-bb64-564b-8ca4-8cc89a2de072",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SteelixV.Name",
    display_name="Steelix V",
    searchable_by=["Steelix V", "Basic", "V", "SteelixV"],
    subtypes=["Basic", "V"],
    collector_number=176,
    set_code="SWSH4",
    rarity=Rarities.RareUltra,
    hp=250,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=208,
    abilities=[
        Attack(
            title="Raging Hammer",
            game_text="This attack does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Iron Tackle",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 4},
            damage=210,
            effect=unimplemented,
        ),
    ],
)