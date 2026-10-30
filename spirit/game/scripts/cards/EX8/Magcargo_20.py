"""STUB: effect not implemented — do not guess mechanics.
Magcargo (EX8 #20): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import may_discard_stadium_then_damage, smooth_over_top


card = PokemonCardDef(
    guid="b9b6da80-826e-58d5-b8bb-080294359681",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magcargo.Name",
    display_name="Magcargo",
    searchable_by=["Magcargo", "Stage 1", "Magcargo"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="EX8",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    family_id=218,
    abilities=[
        Ability(
            title="Smooth Over",
            game_text="Once during your turn (before your attack), you may search your deck for a card. Shuffle your deck, then put that card on top of your deck. This power can't be used if Magcargo is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=smooth_over_top(),
        ),
        Attack(
            title="Knock Over",
            game_text="You may discard any Stadium card in play.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=may_discard_stadium_then_damage(),
        ),
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)