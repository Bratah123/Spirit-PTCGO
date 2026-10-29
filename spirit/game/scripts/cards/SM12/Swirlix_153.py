from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn


card = PokemonCardDef(
    guid="c815f0f8-0fbd-55b0-a9dd-556f8fb642f8",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swirlix.Name",
    display_name="Swirlix",
    searchable_by=["Swirlix", "Basic", "Swirlix"],
    subtypes=["Basic"],
    collector_number=153,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=684,
    abilities=[
        Attack(
            title="Cotton Guard",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 10 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
            effect=protect_next_turn(reduce=10),
        ),
    ],
)