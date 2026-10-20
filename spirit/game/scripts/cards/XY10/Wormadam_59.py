"""STUB: effect not implemented — do not guess mechanics.
Wormadam (XY10 #59): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="d538b433-219e-521f-b942-3794e892ff1a",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wormadam.Name",
    display_name="Wormadam",
    searchable_by=["Wormadam", "Stage 1", "Wormadam"],
    subtypes=["Stage 1"],
    collector_number=59,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Burmy.Name",
    family_id=412,
    abilities=[
        Attack(
            title="Strike Back",
            game_text="This attack does 20 damage times the number of damage counters on this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Iron Head",
            game_text="Flip a coin until you get tails. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_damage(until_tails=True, bonus_per_heads=20),
        ),
    ],
)