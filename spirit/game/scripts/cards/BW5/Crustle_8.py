from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


_bullet_snipe = snipe_attack(20)


async def _heavy_bullet(ctx):
    """Printed damage; flip, heads 20 to 1 of the opponent's Benched Pokémon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Heavy Bullet")
    if results and results[0]:
        await _bullet_snipe(ctx)


card = PokemonCardDef(
    guid="8a467df7-1146-59bd-be0b-1fecb56b766c",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crustle.Name",
    display_name="Crustle",
    searchable_by=["Crustle", "Stage 1", "Crustle"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dwebble.Name",
    family_id=557,
    abilities=[
        Attack(
            title="Cut",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Heavy Bullet",
            game_text="Flip a coin. If heads, this attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=_heavy_bullet,
        ),
    ],
)