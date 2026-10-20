"""STUB: effect not implemented — do not guess mechanics.
Tranquill (XY6 #79): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="477fcd87-fe0d-554b-9a06-a9284d3df0fe",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tranquill.Name",
    display_name="Tranquill",
    searchable_by=["Tranquill", "Stage 1", "Tranquill"],
    subtypes=["Stage 1"],
    collector_number=79,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidove.Name",
    family_id=519,
    abilities=[
        Attack(
            title="Fly",
            game_text="Flip a coin. If tails, this attack does nothing. If heads, prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)