from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def _ember(ctx):
    """20; flip: tails discard a Fire Energy attached to this Pokemon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title)
    if not (results and results[0]) and any(_is_fire_energy(e) for e in ctx.attached_energies(ctx.attacker)):
        await ctx.discard_energy_from(ctx.attacker, 1, predicate=_is_fire_energy, minimum=1,
                                      prompt="Discard a Fire Energy")


card = PokemonCardDef(
    guid="f6010dac-e612-534b-b387-4e0c10ebf7f1",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torchic.Name",
    display_name="Torchic",
    searchable_by=["Torchic", "Basic", "Torchic"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=255,
    abilities=[
        Attack(
            title="Ember",
            game_text="Flip a coin. If tails, discard a Fire Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=_ember,
        ),
    ],
)