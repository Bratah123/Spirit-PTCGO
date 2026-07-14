from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack, discard_random_from_hand


async def bully_of_the_sands(ctx):
    """On evolve, or when Active and KO'd by an opponent's attack: you may
    discard a random card from the opponent's hand."""
    if ctx.source in ctx.discard_pile(ctx.player_id) and not ctx.ko_from_attack:
        return
    if ctx.hand_size(ctx.opponent_id) == 0:
        return
    if await ctx.ask_yes_no("Discard a random card from your opponent's hand?"):
        await discard_random_from_hand(ctx, player_id=ctx.opponent_id, count=1)


card = PokemonCardDef(
    guid="8e87fac1-189b-5df0-8b56-e9feab320031",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krookodile.Name",
    display_name="Krookodile",
    searchable_by=["Krookodile", "Stage 2", "Krookodile"],
    subtypes=["Stage 2"],
    collector_number=113,
    set_code="SWSH12",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name",
    family_id=551,
    abilities=[
        Ability(
            title="Bully of the Sands",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may discard a random card from your opponent's hand. If this Pok\u00e9mon is your Active Pok\u00e9mon and is Knocked Out by damage from an opponent's attack, you may discard a random card from your opponent's hand.",
            trigger=(Triggers.ON_EVOLVE, Triggers.ON_KNOCKED_OUT),
            effect=bully_of_the_sands,
        ),
        Attack(
            title="Double-Edge",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=recoil_attack(30),
        ),
    ],
)