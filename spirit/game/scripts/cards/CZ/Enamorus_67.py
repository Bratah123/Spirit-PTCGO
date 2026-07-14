from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if


async def draining_kiss(ctx):
    """20. Heal 20 damage from this Pokémon."""
    await ctx.deal_damage()
    await ctx.heal(20, ctx.attacker)


def _same_hand_size(ctx):
    return ctx.hand_size() == ctx.hand_size(ctx.opponent_id)


card = PokemonCardDef(
    guid="fa3103ab-be3e-5b66-a8f1-ea0e4e94d521",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Enamorus.Name",
    display_name="Enamorus",
    searchable_by=["Enamorus", "Basic", "Enamorus"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="CZ",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=905,
    abilities=[
        Attack(
            title="Draining Kiss",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=draining_kiss,
        ),
        Attack(
            title="Loving Sympathy",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 70 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="+",
            effect=bonus_if(_same_hand_size, 70),
        ),
    ],
)