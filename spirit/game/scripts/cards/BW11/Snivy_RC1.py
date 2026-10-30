from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_grass_energy_card


async def _growth(ctx):
    """Attach a Grass Energy from your hand to this Pokemon."""
    pool = [c for c in ctx.hand() if is_grass_energy_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Grass Energy to attach")
    if picks:
        await ctx.attach_energy(picks[0], ctx.attacker)


card = PokemonCardDef(
    guid="810263e7-4950-558d-b82d-75a10f17f0a3",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snivy.Name",
    display_name="Snivy",
    searchable_by=["Snivy", "Basic", "Snivy"],
    subtypes=["Basic"],
    collector_number=116,
    set_code="BW11",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=495,
    abilities=[
        Attack(
            title="Growth",
            game_text="Attach a Grass Energy from your hand to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_growth,
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)