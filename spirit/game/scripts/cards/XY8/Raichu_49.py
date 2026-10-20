"""STUB: effect not implemented — do not guess mechanics.
Raichu (XY8 #49): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.content.definitions import def_for


def _is_ex(p):
    return "EX" in (getattr(def_for(p.archetype_id), "subtypes", None) or [])


async def _thunderclap_shot(ctx):
    """50 to each of your opponent's Pokemon-EX."""
    for p in list(ctx.opponent_pokemon_in_play()):
        if _is_ex(p):
            await ctx.deal_damage(50, target=p)


card = PokemonCardDef(
    guid="58fe1615-9c6d-516d-8141-16f4cc1dc751",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name",
    display_name="Raichu",
    searchable_by=["Raichu", "Stage 1", "Raichu"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=25,
    abilities=[
        Attack(
            title="Thunderclap Shot",
            game_text="This attack does 50 damage to each of your opponent's Pok\u00e9mon-EX. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=_thunderclap_shot,
        ),
        Attack(
            title="Electrosmash",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_bonus(20),
        ),
    ],
)