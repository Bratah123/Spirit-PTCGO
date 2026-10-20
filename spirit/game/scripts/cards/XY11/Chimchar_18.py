from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


async def _ember(ctx):
    """20; flip: tails discard a Fire Energy attached to this Pokemon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title)
    if not (results and results[0]) and any(_is_fire_energy(e) for e in ctx.attached_energies(ctx.attacker)):
        await ctx.discard_energy_from(ctx.attacker, 1, predicate=_is_fire_energy, minimum=1,
                                      prompt="Discard a Fire Energy")


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


card = PokemonCardDef(
    guid="0d6baa4c-bd56-5fa1-8259-76c8d1d81764",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chimchar.Name",
    display_name="Chimchar",
    searchable_by=["Chimchar", "Basic", "Chimchar"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="XY11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=390,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Ember",
            game_text="Flip a coin. If tails, discard a Fire Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_ember,
        ),
    ],
)