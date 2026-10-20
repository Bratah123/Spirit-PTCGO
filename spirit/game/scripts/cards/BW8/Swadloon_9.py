from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn
from spirit.game.card_effects.attacks_common import flip_or_nothing


card = PokemonCardDef(
    guid="b4e4e520-99ba-5265-91ab-030067dd8069",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swadloon.Name",
    display_name="Swadloon",
    searchable_by=["Swadloon", "Stage 1", "Swadloon"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sewaddle.Name",
    family_id=540,
    abilities=[
        Attack(
            title="Swaddle Guard",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is reduced by 40 (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 1},
            effect=protect_next_turn(reduce=40),
        ),
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=flip_or_nothing(),
        ),
    ],
)