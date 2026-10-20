from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="edbe0ea0-1406-52dc-97c7-d035128e328a",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torkoal.Name",
    display_name="Torkoal",
    searchable_by=["Torkoal", "Basic", "Torkoal"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=324,
    abilities=[
        Attack(
            title="Flame Cloak",
            game_text="Flip a coin. If heads, attach a Fire Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)