"""STUB: effect not implemented — do not guess mechanics.
Aegislash (XY9 #62): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


async def lunar_pain(ctx):
    """Double the number of damage counters on each of your opponent's Pokemon."""
    for pokemon in ctx.opponent_pokemon_in_play():
        current = (ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10
        if current > 0:
            await ctx.deal_damage(current * 10, target=pokemon, as_counters=True)


card = PokemonCardDef(
    guid="40b36eb4-1085-56b7-8142-cb32d5c10d14",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aegislash.Name",
    display_name="Aegislash",
    searchable_by=["Aegislash", "Stage 2", "Aegislash"],
    subtypes=["Stage 2"],
    collector_number=62,
    set_code="XY9",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name",
    family_id=679,
    abilities=[
        Attack(
            title="Painful Sword",
            game_text="Double the number of damage counters on each of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            # STUB: attack effect not implemented
            effect=lunar_pain,
        ),
        Attack(
            title="Megaton Slash",
            game_text="This attack does 10 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)