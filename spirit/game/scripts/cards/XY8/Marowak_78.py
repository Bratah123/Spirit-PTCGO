"""STUB: effect not implemented — do not guess mechanics.
Marowak (XY8 #78): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.content.definitions import def_for


def _is_ex(p):
    return "EX" in (getattr(def_for(p.archetype_id), "subtypes", None) or [])


async def _bone_windmill(ctx):
    """60; if the opponent's Active is a Pokemon-EX, switch this Pokemon with 1 of your Benched Pokemon."""
    await ctx.deal_damage()
    d = ctx.opponent_active()
    bench = ctx.my_bench()
    if d is not None and _is_ex(d) and bench and ctx.attacker is ctx.my_active():
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(bench, "Switch with which Benched Pokémon?")
        await ctx.switch_active(ctx.player_id, target or bench[0])


card = PokemonCardDef(
    guid="5e8b00c1-5e70-53a0-b592-ec57cc1a36ff",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marowak.Name",
    display_name="Marowak",
    searchable_by=["Marowak", "Stage 1", "Marowak"],
    subtypes=["Stage 1"],
    collector_number=78,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    family_id=104,
    abilities=[
        Attack(
            title="Sharpshooting",
            game_text="This attack does 30 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            # STUB: attack effect not implemented
            effect=snipe_attack(30, pool='any', count=1),
        ),
        Attack(
            title="Bone Windmill",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon-EX, switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=_bone_windmill,
        ),
    ],
)