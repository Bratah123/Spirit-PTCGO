from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.card_effects.trainers import is_basic_energy_card


async def tri_recharge(ctx):
    heads = await ctx.flip_coins(3, "Tri Recharge")
    count = sum(1 for h in heads if h)
    bench = ctx.my_bench()
    energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if count <= 0 or not bench or not energy:
        return
    picks = await ctx.choose_cards(
        energy, count, minimum=1,
        prompt=f"Choose up to {count} basic Energy to attach to your Benched Pokémon.",
    )
    if picks:
        await distribute_energy(ctx, picks, bench)

card = PokemonCardDef(
    guid="2e3d360d-1824-5683-a6dd-f783b5d47288",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sigilyph.Name",
    display_name="Sigilyph",
    searchable_by=["Sigilyph", "Basic", "Sigilyph"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=561,
    abilities=[
        Attack(
            title="Tri Recharge",
            game_text="Flip 3 coins. Attach a number of basic Energy cards up to the number of heads from your discard pile to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=tri_recharge,
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 30, base=10),
        ),
    ],
)