from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card


async def _wrapped_in_wind(ctx):
    """Attach up to 2 basic Energy cards from your hand to this Pokemon."""
    pool = [c for c in ctx.hand() if is_basic_energy_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Attach up to 2 basic Energy")
    for energy in picks or []:
        await ctx.attach_energy(energy, ctx.attacker)


card = PokemonCardDef(
    guid="b1a47c7a-7e4f-5d82-9d8b-4c7fe71c6343",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name",
    display_name="Dragonite",
    searchable_by=["Dragonite", "Stage 2", "Dragonite"],
    subtypes=["Stage 2"],
    collector_number=52,
    set_code="XY6",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=147,
    abilities=[
        Attack(
            title="Wrapped in Wind",
            game_text="Attach up to 2 basic Energy cards from your hand to this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=_wrapped_in_wind,
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=150,
        ),
    ],
)