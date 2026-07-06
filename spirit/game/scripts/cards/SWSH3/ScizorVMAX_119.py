from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f820557f-80ef-5cbd-aa08-7aab5accccc8",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ScizorVMAX.Name",
    display_name="Scizor VMAX",
    searchable_by=["Scizor VMAX", "VMAX", "ScizorVMAX"],
    subtypes=["VMAX"],
    collector_number=119,
    set_code="SWSH3",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ScizorV.Name",
    family_id=212,
    abilities=[
        Attack(
            title="Hard Scissors",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=unimplemented,
        ),
        Attack(
            title="Max Steelspike",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
        ),
    ],
)