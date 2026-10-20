from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def _eternal_radiance(ctx):
    """Move all damage counters from this Pokemon to the Defending Pokemon."""
    if ctx.defender is not None:
        await ctx.move_damage_counters(ctx.attacker, ctx.defender)


card = PokemonCardDef(
    guid="a1809b7b-9694-5f8b-ad55-bc5b8ee3e919",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoir.Name",
    display_name="Gardevoir",
    searchable_by=["Gardevoir", "Stage 2", "Gardevoir"],
    subtypes=["Stage 2"],
    collector_number=125,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Attack(
            title="Psybeam",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Eternal Radiance",
            game_text="Move all damage counters from this Pok\u00e9mon to the Defending Pok\u00e9mon. This Pok\u00e9mon can't use Eternal Radiance during your next turn.",
            cost={PokemonTypes.PSYCHIC: 2},
            effect=_eternal_radiance,
            locks_next_turn=True,
        ),
    ],
)