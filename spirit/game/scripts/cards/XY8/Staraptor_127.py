from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack


async def _cyclone_slash(ctx):
    """Before damage, your opponent switches their Active with 1 of their Benched Pokemon; 70."""
    bench = ctx.opponent_bench()
    if bench and not ctx.effects_blocked(ctx.opponent_active()):
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
            bench, "Choose your new Active Pokémon", player_id=ctx.opponent_id)
        await ctx.switch_active(ctx.opponent_id, target or bench[0])
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="1d7c40a5-013f-5a21-8825-cfcd540ea519",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Staraptor.Name",
    display_name="Staraptor",
    searchable_by=["Staraptor", "Stage 2", "Staraptor"],
    subtypes=["Stage 2"],
    collector_number=127,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staravia.Name",
    family_id=396,
    abilities=[
        Attack(
            title="Cyclone Slash",
            game_text="Before doing damage, have your opponent switch his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=_cyclone_slash,
        ),
        Attack(
            title="Brave Bird",
            game_text="This Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=recoil_attack(20),
        ),
    ],
)