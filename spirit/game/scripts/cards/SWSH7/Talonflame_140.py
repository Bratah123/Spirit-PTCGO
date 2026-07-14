from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, count_energy

_FIRE_ENERGY_ON_SELF = count_energy("self", energy_type=PokemonTypes.FIRE)


async def _clutch(ctx):
    await ctx.deal_damage()
    target = ctx.defender
    if target is not None and not ctx.effects_blocked(target):
        ctx.lock_retreat(target)


card = PokemonCardDef(
    guid="d720b952-a2c6-5466-a2de-8e61bf8f9775",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Talonflame.Name",
    display_name="Talonflame",
    searchable_by=["Talonflame", "Stage 2", "Talonflame"],
    subtypes=["Stage 2"],
    collector_number=140,
    set_code="SWSH7",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name",
    family_id=661,
    abilities=[
        Attack(
            title="Clutch",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=_clutch,
        ),
        Attack(
            title="Nitro Dive",
            game_text="If this Pok\u00e9mon has any Fire Energy attached, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=bonus_if(lambda ctx: _FIRE_ENERGY_ON_SELF(ctx) > 0, 80),
        ),
    ],
)