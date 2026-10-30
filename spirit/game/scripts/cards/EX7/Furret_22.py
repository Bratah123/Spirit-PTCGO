from spirit.game.card_effects.ex import quick_change, quick_tail_smash
"""STUB: effect not implemented — do not guess mechanics.
Furret (EX7 #22): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3e4bec41-2e0f-5ba4-8d7d-55260b5665d3",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Furret.Name",
    display_name="Furret",
    searchable_by=["Furret", "Stage 1", "Furret"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="EX7",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sentret.Name",
    family_id=161,
    abilities=[
        Attack(
            title="Quick Change",
            game_text="Choose up to 3 cards in your hand and put them on top of your deck. Then, search your deck for that many cards and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=quick_change(),
        ),
        Attack(
            title="Quick Tail Smash",
            game_text="Before doing damage, you may flip a coin. If heads, this attack does 80 damage instead. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=quick_tail_smash(),
        ),
    ],
)