from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_bench


async def _doom_decree(ctx):
    """Flip 2 coins. If both are heads, the Defending Pokemon is Knocked Out."""
    results = await ctx.flip_coins(2, "Doom Decree")
    if len(results) == 2 and all(results) and ctx.defender is not None \
            and not ctx.effects_blocked(ctx.defender):
        await ctx.knock_out(ctx.defender)


card = PokemonCardDef(
    guid="e1f605ef-dfb9-515a-9d0d-53a5e4324a93",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothitelle.Name",
    display_name="Gothitelle",
    searchable_by=["Gothitelle", "Stage 2", "Gothitelle"],
    subtypes=["Stage 2"],
    collector_number=57,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gothorita.Name",
    family_id=574,
    abilities=[
        Attack(
            title="Doom Decree",
            game_text="Flip 2 coins. If both of them are heads, the Defending Pok\u00e9mon is Knocked Out.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=_doom_decree,
        ),
        Attack(
            title="Black Magic",
            game_text="Does 20 more damage for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=damage_per(count_bench('opponent'), 20, base=40),
        ),
    ],
)