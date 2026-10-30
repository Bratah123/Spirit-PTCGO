"""STUB: effect not implemented — do not guess mechanics.
Dusclops (DP7 #34): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="7f029b94-4bd6-5310-9c79-8febfdb667da",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name",
    display_name="Dusclops",
    searchable_by=["Dusclops", "Stage 1", "Dusclops"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Duskull.Name",
    family_id=355,
    abilities=[
        Attack(
            title="Dark One-eye",
            game_text="You may discard a card from your hand. If you do, your opponent discards a card from his or her hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Ambush",
            game_text="Flip a coin. If heads, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_bonus(20),
        ),
    ],
)