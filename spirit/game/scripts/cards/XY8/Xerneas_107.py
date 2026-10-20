from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import bonus_if


def _healed_this_turn(ctx):
    return ctx.attacker.entity_id in ctx.session.turn_state.healed_entities


async def _rainbow_force(ctx):
    """10+; 30 more for each different type of Pokemon on your Bench."""
    types = set()
    for p in ctx.my_bench():
        types.update(p.get_attribute(AttrID.POKEMON_TYPES) or [])
    await ctx.deal_damage(ctx.ability.damage + 30 * len(types))


card = PokemonCardDef(
    guid="36915c51-45df-59d5-ad00-d3e59eead2c0",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xerneas.Name",
    display_name="Xerneas",
    searchable_by=["Xerneas", "Basic", "Xerneas"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="XY8",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=716,
    abilities=[
        Attack(
            title="Rainbow Force",
            game_text="This attack does 30 more damage for each different type of Pok\u00e9mon on your Bench.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=_rainbow_force,
        ),
        Attack(
            title="Power Creation",
            game_text="If this Pok\u00e9mon was healed during this turn, this attack does 80 more damage.",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=bonus_if(_healed_this_turn, 80),
        ),
    ],
)