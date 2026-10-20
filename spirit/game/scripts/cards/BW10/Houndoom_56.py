from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.effects import is_team_plasma_pokemon


async def _blazing_claws(ctx):
    """If the Defending Pokemon is a Team Plasma Pokemon, 60 more damage and
    the Defending Pokemon is now Burned."""
    d = ctx.defender
    plasma = d is not None and is_team_plasma_pokemon(d)
    await ctx.deal_damage(ctx.ability.damage + (60 if plasma else 0))
    if plasma and not ctx.effects_blocked(d):
        await ctx.apply_special_condition(d, SpecialConditions.BURNED)


card = PokemonCardDef(
    guid="1769730c-9294-5d22-9066-6be18244f1f5",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndoom.Name",
    display_name="Houndoom",
    searchable_by=["Houndoom", "Stage 1", "Houndoom"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="BW10",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    family_id=228,
    abilities=[
        Attack(
            title="Dark Clamp",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Blazing Claws",
            game_text="If the Defending Pok\u00e9mon is a Team Plasma Pok\u00e9mon, this attack does 60 more damage, and the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=_blazing_claws,
        ),
    ],
)