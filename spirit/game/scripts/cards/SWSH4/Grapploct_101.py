from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if


async def full_nelson(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        ctx.lock_retreat(defender)


def _used_full_nelson_last_turn(ctx):
    return ctx.attack_used_last_turn(title="Full Nelson", entity=ctx.attacker)


card = PokemonCardDef(
    guid="4df97f55-6696-5c4a-a300-7cc776e9658f",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grapploct.Name",
    display_name="Grapploct",
    searchable_by=["Grapploct", "Stage 1", "Grapploct"],
    subtypes=["Stage 1"],
    collector_number=101,
    set_code="SWSH4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clobbopus.Name",
    family_id=852,
    abilities=[
        Attack(
            title="Full Nelson",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=full_nelson,
        ),
        Attack(
            title="Tentacle Buster",
            game_text="If this Pok\u00e9mon used Full Nelson during your last turn, this attack does 120 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=bonus_if(_used_full_nelson_last_turn, 120),
        ),
    ],
)