from spirit.game.card_effects.passives_common import protect_next_turn
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ba01dfd9-08f0-5a35-906c-e7d3bbb06475",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ScizorVMAX.Name",
    display_name="Scizor VMAX",
    searchable_by=["Scizor VMAX", "VMAX", "ScizorVMAX"],
    subtypes=["VMAX"],
    collector_number=193,
    set_code="SWSH3",
    rarity=Rarities.RareRainbow,
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
            effect=protect_next_turn(reduce=30),
        ),
        Attack(
            title="Max Steelspike",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
        ),
    ],
)