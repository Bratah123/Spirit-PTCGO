from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack


async def _sand_flap(ctx):
    """Choose either player: they shuffle their hand into their deck and draw 4."""
    idx = await ctx.choose("Choose a player", ["You", "Your opponent"])
    pid = ctx.opponent_id if idx == 1 else ctx.player_id
    await ctx.shuffle_into_deck(list(ctx.hand(pid)), pid)
    await ctx.draw_cards(4, pid)


card = PokemonCardDef(
    guid="e509c516-da73-534b-841e-dee37e5a451b",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flygon.Name",
    display_name="Flygon",
    searchable_by=["Flygon", "Stage 2", "Flygon"],
    subtypes=["Stage 2"],
    collector_number=110,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=328,
    abilities=[
        Ability(
            title="Sand Flap",
            game_text="Once during your turn (before your attack), you may choose either player. That player shuffles his or her hand into his or her deck and draws 4 cards.",
            activation=Activations.ONCE_PER_TURN,
            effect=_sand_flap,
        ),
        Attack(
            title="Sand Tomb",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)