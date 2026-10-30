from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn
from spirit.game.card_effects.ex import nap_heal


card = PokemonCardDef(
    guid="3c673a28-4ab5-53f3-af47-f24f523dc070",
    key="POP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name",
    display_name="Wobbuffet",
    searchable_by=["Wobbuffet", "Basic", "Wobbuffet"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="POP4",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=202,
    abilities=[
        Attack(
            title="Nap",
            game_text="Remove 2 damage counters from Wobbuffet.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=nap_heal(2),
        ),
        Attack(
            title="Expand",
            game_text="During your opponent's next turn, any damage done to Wobbuffet is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=protect_next_turn(reduce=20),
        ),
    ],
)
