from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, AttrID
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.content.definitions import def_for


async def _heavy_bullet(ctx):
    """Printed damage; flip, heads 20 to 1 of the opponent's Benched Pokémon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Heavy Bullet")
    if results and results[0]:
        await _bullet_snipe(ctx)


_bullet_snipe = snipe_attack(20)


def _is_pokemon_ex(pokemon):
    d = def_for(pokemon.archetype_id) if pokemon is not None else None
    return bool(d) and "EX" in (getattr(d, "subtypes", None) or [])


def _plasma_steel(calc, carrier):
    """Prevent all damage done to your Metal Pokemon by attacks from your
    opponent's Pokemon-EX."""
    target = calc.target
    return (target is not None and target.owning_player_id == carrier.owning_player_id
            and PokemonTypes.METAL.value in (target.get_attribute(AttrID.POKEMON_TYPES) or [])
            and _is_pokemon_ex(calc.attacker))


card = PokemonCardDef(
    guid="9339bc7d-5a33-5b24-8b21-e4556decd011",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klinklang.Name",
    display_name="Klinklang",
    searchable_by=["Klinklang", "Stage 2", "Team Plasma", "Klinklang"],
    subtypes=["Stage 2", "Team Plasma"],
    collector_number=90,
    set_code="BW8",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Klang.Name",
    family_id=599,
    abilities=[
        Ability(
            title="Plasma Steel",
            game_text="Prevent all damage done to your Metal Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon-EX.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=prevent_damage_when(_plasma_steel),
        ),
        Attack(
            title="Heavy Bullet",
            game_text="Flip a coin. If heads, this attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=_heavy_bullet,
        ),
    ],
)