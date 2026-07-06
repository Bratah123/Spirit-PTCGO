from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9fb82859-0659-57eb-b00c-89c6d8215c99",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RadiantHawlucha.Name",
    display_name="Radiant Hawlucha",
    searchable_by=["Radiant Hawlucha", "Basic", "Radiant", "RadiantHawlucha"],
    subtypes=["Basic", "Radiant"],
    collector_number=81,
    set_code="SWSH10",
    rarity=Rarities.RareRadiant,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=701,
    abilities=[
        Ability(
            title="Big Match",
            game_text="As long as this Pok\u00e9mon is on your Bench, your Pok\u00e9mon's attacks do 30 more damage to your opponent's Active Pok\u00e9mon VMAX (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Spiral Kick",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)