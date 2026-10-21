from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.content.definitions import def_for


def _is_ex(p):
    return "EX" in (getattr(def_for(p.archetype_id), "subtypes", None) or [])


async def _energy_hunt(ctx):
    """Flip 3 coins; per heads attach a basic Energy from your discard to your
    Benched Pokemon-EX in any way you like."""
    results = await ctx.flip_coins(3, ctx.ability.title)
    heads = sum(1 for r in results if r)
    targets = [p for p in ctx.my_bench() if _is_ex(p)]
    for _ in range(heads):
        pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        if not pool or not targets:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Choose a basic Energy card to attach")
        if not picks:
            return
        target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(targets, "Choose a Benched Pokémon-EX")
        await ctx.attach_energy(picks[0], target or targets[0])


card = PokemonCardDef(
    guid="f4ade1c1-abc9-54e9-b7dc-8c3d688e1bc1",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name",
    display_name="Sableye",
    searchable_by=["Sableye", "Basic", "Sableye"],
    subtypes=["Basic"],
    collector_number=92,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=302,
    abilities=[
        Attack(
            title="Energy Hunt",
            game_text="Flip 3 coins. For each heads, attach a basic Energy card from your discard pile to your Benched Pok\u00e9mon-EX in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_energy_hunt,
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)