from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm10 import (
    hypnotic_pendulum,
    stir_the_brain,
)

card = PokemonCardDef(
    guid="2e7a4809-2123-5799-abd2-5e0b562a923e",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hypno.Name",
    display_name="Hypno",
    searchable_by=["Hypno", "Stage 1", "Hypno"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    family_id=96,
    abilities=[
        Ability(
            title="Hypnotic Pendulum",
            game_text="When your opponent's Active Pok\u00e9mon is Knocked Out, flip a coin. If heads, choose which of your opponent's Benched Pok\u00e9mon becomes their new Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_OPPONENT_KNOCKED_OUT,
            effect=hypnotic_pendulum
        ),
        Attack(
            title="Stir the Brain",
            game_text="This attack does 10 more damage for each card in your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=stir_the_brain
        ),
    ],
)