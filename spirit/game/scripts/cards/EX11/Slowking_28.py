"""STUB: effect not implemented — do not guess mechanics.
Slowking (EX11 #28): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from spirit.game.card_effects.ex import poke_power_condition, prize_shift, psychic_option_water_psychic
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="f342d939-91d1-514d-a6a5-f7b7117fe18a",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowking.Name",
    display_name="Slowking",
    searchable_by=["Slowking", "Stage 1", "Slowking"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="EX11",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Ability(
            title="Prize Shift",
            game_text="Once during your turn (before your attack), you may choose a card from your hand and put it as a Prize card face up. If you do, choose 1 of your face-down Prize cards without looking and put it into your hand. This power can't be used if Slowking is affected by a Special Condition or if all of your Prize cards are face up.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(),
            effect=prize_shift(),
        ),
        Attack(
            title="Psychic Option",
            game_text="If Slowking has a Water Energy card attached to it, this attack does 20 damage plus 20 more damage. If Slowking has a Psychic Energy card attached to it, discard a Special Energy card attached to the Defending Pok\u00e9mon, if any.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=psychic_option_water_psychic(20, 20),
        ),
    ],
)