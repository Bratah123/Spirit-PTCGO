from spirit.game.card_effects.passives_common import protect_next_turn
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="af74c701-807f-58fb-9f1f-2901acbebed0",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name",
    display_name="Scraggy",
    searchable_by=["Scraggy", "Basic", "Scraggy"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="SWSH7",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=559,
    abilities=[
        Attack(
            title="Hard Head",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 10 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=protect_next_turn(reduce=10),
        ),
    ],
)