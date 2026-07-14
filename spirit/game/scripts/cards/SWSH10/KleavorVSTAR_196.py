from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_discard
from spirit.game.session.effects import is_pokemon_card


async def axe_break(ctx):
    """120 damage; also 60 to 1 opposing Benched Pokemon V (no W/R)."""
    await ctx.deal_damage()
    bench = [p for p in ctx.opponent_bench() if is_pokemon_v(p.archetype_id)]
    if bench:
        target = await ctx.choose_pokemon(
            bench, "Choose 1 of your opponent's Benched Pokémon V"
        )
        if target is not None:
            await ctx.deal_damage(60, target=target, apply_modifiers=False)


card = PokemonCardDef(
    guid="51cf594f-bd24-5bf1-9da5-7815dae5be1e",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KleavorVSTAR.Name",
    display_name="Kleavor VSTAR",
    searchable_by=["Kleavor VSTAR", "VSTAR", "KleavorVSTAR"],
    subtypes=["VSTAR"],
    collector_number=196,
    set_code="SWSH10",
    rarity=Rarities.RareRainbow,
    hp=270,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.KleavorV.Name",
    family_id=900,
    abilities=[
        Attack(
            title="Axe Break",
            game_text="This attack also does 60 damage to 1 of your opponent's Benched Pok\u00e9mon V. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=axe_break,
        ),
        Attack(
            title="Rampaging Star",
            game_text="This attack does 30 damage for each Pok\u00e9mon in your discard pile. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="x",
            vstar=True,
            effect=damage_per(count_discard("mine", pred=is_pokemon_card), 30),
        ),
    ],
)