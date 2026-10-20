from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage, lock_defender_attacks
from spirit.game.content.definitions import def_for


def _is_pokemon_ex(pokemon):
    d = def_for(pokemon.archetype_id) if pokemon is not None else None
    return bool(d) and "EX" in (getattr(d, "subtypes", None) or [])


async def _electri_defuse(ctx):
    """Printed damage; if the Defending Pokemon is a Pokemon-EX, it can't
    attack during your opponent's next turn."""
    await ctx.deal_damage()
    if _is_pokemon_ex(ctx.defender):
        lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="8168e223-f384-5b6e-b8e4-ae62a5c3bae9",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jolteon.Name",
    display_name="Jolteon",
    searchable_by=["Jolteon", "Stage 1", "Team Plasma", "Jolteon"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=34,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Pin Missile",
            game_text="Flip 4 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=20),
        ),
        Attack(
            title="Electri-Defuse",
            game_text="If the Defending Pok\u00e9mon is a Pok\u00e9mon-EX, that Pok\u00e9mon can't attack during your opponent's next turn.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=_electri_defuse,
        ),
    ],
)