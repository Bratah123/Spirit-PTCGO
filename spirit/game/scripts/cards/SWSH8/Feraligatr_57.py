from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def rowdy(ctx):
    heads = (await ctx.flip_coins(1, "Rowdy"))[0]
    pid = ctx.opponent_id if heads else ctx.player_id
    await ctx.discard_cards(ctx.deck_top(5, player_id=pid))

card = PokemonCardDef(
    guid="8086bf87-3cf4-5202-87fe-46958d1663b6",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feraligatr.Name",
    display_name="Feraligatr",
    searchable_by=["Feraligatr", "Stage 2", "Feraligatr"],
    subtypes=["Stage 2"],
    collector_number=57,
    set_code="SWSH8",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    family_id=158,
    abilities=[
        Ability(
            title="Rowdy",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you must flip a coin. If heads, discard the top 5 cards of your opponent's deck. If tails, discard the top 5 cards of your deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=rowdy,
        ),
        Attack(
            title="Crunch",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
            effect=discard_opponent_energy_attack(),
        ),
    ],
)