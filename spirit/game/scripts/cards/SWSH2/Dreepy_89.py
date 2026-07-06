from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9f342c97-65f3-5071-ab8a-23a9c056669d",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dreepy.Name",
    display_name="Dreepy",
    searchable_by=["Dreepy", "Basic", "Dreepy"],
    subtypes=["Basic"],
    collector_number=89,
    set_code="SWSH2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=885,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 more damage.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)