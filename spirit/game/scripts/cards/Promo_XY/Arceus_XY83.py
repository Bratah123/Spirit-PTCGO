from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.card_effects.trainers import is_basic_energy_card


def _basic_energy_types_count(ctx):
    types = set()
    for e in ctx.attached_energies(ctx.attacker):
        if is_basic_energy_card(e):
            for t in (e.get_attribute(AttrID.POKEMON_TYPES) or []):
                types.add(t)
    return len(types)


async def _gather_light(ctx):
    """Move as many Energy as you like from your Benched Pokemon to this Pokemon."""
    sources = [p for p in ctx.my_bench() if ctx.attached_energies(p)]
    if sources:
        await ctx.move_energy_freely(sources, [ctx.attacker])


card = PokemonCardDef(
    guid="f73eeedd-5823-59a6-84c2-1a0a55e3979e",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arceus.Name",
    display_name="Arceus",
    searchable_by=["Arceus", "Basic", "Arceus"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=493,
    abilities=[
        Attack(
            title="Gather Light",
            game_text="Move as many Energy as you like from your Benched Pok\u00e9mon to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_gather_light,
        ),
        Attack(
            title="Judgment Blast",
            game_text="This attack does 30 more damage for each different type of basic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="+",
            effect=damage_per(_basic_energy_types_count, 30, base=10),
        ),
    ],
)