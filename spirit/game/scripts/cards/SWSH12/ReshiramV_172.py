from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.attacks_common import lock_all_attacks


async def white_blaze(ctx):
    """Flip a coin. If tails, during your next turn, this Pokémon can't attack."""
    await ctx.deal_damage()
    heads = (await ctx.flip_coins(1, ctx.ability.title))[0]
    if not heads:
        lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="e58f4ccb-e15c-5eb5-a0fa-3be90a37ce39",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ReshiramV.Name",
    display_name="Reshiram V",
    searchable_by=["Reshiram V", "Basic", "V", "ReshiramV"],
    subtypes=["Basic", "V"],
    collector_number=172,
    set_code="SWSH12",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=643,
    abilities=[
        Attack(
            title="Sparkling Wing",
            game_text="Search your deck for up to 2 basic Energy cards and attach them to 1 of your Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=search_attach_energy(is_basic_energy_card, count=2, distribute=False),
        ),
        Attack(
            title="White Blaze",
            game_text="Flip a coin. If tails, during your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=white_blaze,
        ),
    ],
)