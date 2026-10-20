from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if


async def ember(ctx):
    """20 damage. Flip a coin. If tails, discard an Energy from this Pokémon."""
    await ctx.deal_damage()
    heads = (await ctx.flip_coins(1, "Ember"))[0]
    if not heads:
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            prompt="Discard an Energy attached to this Pokémon",
        )


card = PokemonCardDef(
    guid="8896dccd-a58b-572f-9d97-f60971220d7a",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TornadusEX.Name",
    display_name="Tornadus-EX",
    searchable_by=["Tornadus-EX", "Basic", "EX", "TornadusEX"],
    subtypes=["Basic", "EX"],
    collector_number=96,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=641,
    abilities=[
        Attack(
            title="Blow Through",
            game_text="If there is any Stadium card in play, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.stadium_in_play() is not None, 30),
        ),
        Attack(
            title="Power Blast",
            game_text="Flip a coin. If tails, discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=ember,
        ),
    ],
)