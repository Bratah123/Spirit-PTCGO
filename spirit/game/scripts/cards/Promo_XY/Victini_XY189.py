from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.trainers import is_basic_energy_card


async def _energy_assist(ctx):
    """Flip a coin. If heads, attach a basic Energy card from your discard pile
    to 1 of your Benched Pokemon."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    bench = ctx.my_bench()
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not (results and results[0]) or not bench or not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a basic Energy card to attach")
    if not picks:
        return
    target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(bench, "Choose a Benched Pokémon")
    await ctx.attach_energy(picks[0], target or bench[0])


card = PokemonCardDef(
    guid="b43b69f9-2232-517f-8ce8-1fb2d429ea58",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name",
    display_name="Victini",
    searchable_by=["Victini", "Basic", "Victini"],
    subtypes=["Basic"],
    collector_number=189,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Attack(
            title="Energy Assist",
            game_text="Flip a coin. If heads, attach a basic Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_energy_assist,
        ),
        Attack(
            title="Victory Ball",
            game_text="Discard a Fire Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=self_energy_discard_attack(count=1, energy_type=PokemonTypes.FIRE),
        ),
    ],
)