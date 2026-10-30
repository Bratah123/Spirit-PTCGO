"""STUB: effect not implemented — do not guess mechanics.
Beautifly (POP1 #6): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import blot_heal
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack


card = PokemonCardDef(
    guid="3e0f10c3-bea4-5202-8493-800dd0a747dc",
    key="POP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beautifly.Name",
    display_name="Beautifly",
    searchable_by=["Beautifly", "Stage 2", "Beautifly"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="POP1",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Silcoon.Name",
    family_id=267,
    abilities=[
        Attack(
            title="Blot",
            game_text="Remove 1 damage counter from Beautifly.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=blot_heal(1),
        ),
        Attack(
            title="Whirlwind",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            # STUB: attack effect not implemented
            effect=gust_attack(opponent_chooses=True),
        ),
    ],
)