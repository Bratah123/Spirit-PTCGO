from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bd327d1b-180d-503a-a96b-6473ebcabf0c",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SerperiorV.Name",
    display_name="Serperior V",
    searchable_by=["Serperior V", "Basic", "V", "SerperiorV"],
    subtypes=["Basic", "V"],
    collector_number=170,
    set_code="SWSH12",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=497,
    abilities=[
        Attack(
            title="Noble Light",
            game_text="Heal 30 damage from each Pok\u00e9mon (both yours and your opponent's).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)