from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type


async def soak_in_water(ctx):
    """Attach a Water Energy card from your hand to this Pokemon."""
    water = [c for c in ctx.hand() if energy_provides_type(c, PokemonTypes.WATER.value)]
    if not water:
        return
    picks = await ctx.choose_cards(water, 1, prompt="Choose a Water Energy card to attach.")
    for card in picks:
        await ctx.attach_energy(card, ctx.source)


card = PokemonCardDef(
    guid="291c4d11-37f9-5734-8245-3492ebc97898",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    display_name="Staryu",
    searchable_by=["Staryu", "Basic", "Rapid Strike", "Staryu"],
    subtypes=["Basic", "Rapid Strike"],
    collector_number=52,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=120,
    abilities=[
        Attack(
            title="Soak in Water",
            game_text="Attach a Water Energy card from your hand to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=soak_in_water,
        ),
        Attack(
            title="Spinning Attack",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)