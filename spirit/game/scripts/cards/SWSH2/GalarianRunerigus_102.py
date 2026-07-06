from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9f2f2067-61a3-526f-bc46-dc8cc38e2d1d",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianRunerigus.Name",
    display_name="Galarian Runerigus",
    searchable_by=["Galarian Runerigus", "Stage 1", "GalarianRunerigus"],
    subtypes=["Stage 1"],
    collector_number=102,
    set_code="SWSH2",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianYamask.Name",
    family_id=562,
    abilities=[
        Attack(
            title="Spreading Spite",
            game_text="For each damage counter on this Galarian Runerigus, put 2 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Mad Hammer",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)