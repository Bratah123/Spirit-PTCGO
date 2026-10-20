from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card


async def _energy_present(ctx):
    """Attach up to 2 Energy cards from your hand to 1 of your Benched Pokemon."""
    bench = ctx.my_bench()
    pool = [c for c in ctx.hand() if is_energy_card(c)]
    if not bench or not pool:
        return
    target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(bench, "Attach to which Benched Pokémon?")
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Choose up to 2 Energy cards")
    for energy in picks or []:
        await ctx.attach_energy(energy, target or bench[0])


card = PokemonCardDef(
    guid="aacbf7a7-9ef4-521f-bfb0-55604c150ddb",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowstic.Name",
    display_name="Meowstic",
    searchable_by=["Meowstic", "Stage 1", "Meowstic"],
    subtypes=["Stage 1"],
    collector_number=59,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Espurr.Name",
    family_id=677,
    abilities=[
        Attack(
            title="Energy Present",
            game_text="Attach up to 2 Energy cards from your hand to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_energy_present,
        ),
        Attack(
            title="Psyshot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)