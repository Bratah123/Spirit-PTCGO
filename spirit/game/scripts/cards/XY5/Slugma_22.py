from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_grass_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.GRASS.value)


async def _grass_fire(ctx):
    """Discard a Grass Energy attached to your opponent's Active Pokemon."""
    await ctx.deal_damage()
    d = ctx.defender
    if d is not None and not ctx.effects_blocked(d) and any(
            _is_grass_energy(e) for e in ctx.attached_energies(d)):
        await ctx.discard_energy_from(d, 1, predicate=_is_grass_energy, minimum=1,
                                      prompt="Discard a Grass Energy")


card = PokemonCardDef(
    guid="add8a5fb-2bf2-580c-a167-7bc2687f2448",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    display_name="Slugma",
    searchable_by=["Slugma", "Basic", "Slugma"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="XY5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=218,
    abilities=[
        Attack(
            title="Grass Fire",
            game_text="Discard a Grass Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            effect=_grass_fire,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)