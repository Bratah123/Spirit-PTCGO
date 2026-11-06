from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.attacks_common import discard_for_bonus


async def _bust_in(ctx):
    """When played from hand to the Bench: you may move any number of basic
    Energy from your Pokemon to this Pokemon. If you do, switch it with your
    Active Pokemon."""
    me = ctx.source
    others = [p for p in ctx.my_pokemon_in_play() if p is not me
              and any(is_basic_energy_card(e) for e in ctx.attached_energies(p))]
    if not others or not await ctx.ask_yes_no(
            "Move basic Energy from your Pokémon to this Pokémon?"):
        return
    moved = await ctx.move_energy_freely(others, [me], predicate=is_basic_energy_card,
                                         max_count=99,
                                         prompt="Choose basic Energy to move")
    if moved and ctx.my_active() is not me:
        await ctx.switch_active(ctx.player_id, me)


card = PokemonCardDef(
    guid="eb07f4ae-8d61-5224-971d-1f1c414bb5e0",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteEX.Name",
    display_name="Dragonite-EX",
    searchable_by=["Dragonite-EX", "Basic", "EX", "DragoniteEX"],
    subtypes=["Basic", "EX"],
    collector_number=108,
    set_code="XY3",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=149,
    abilities=[
        Ability(
            title="Bust In",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench, you may move any number of basic Energy attached to your Pok\u00e9mon to this Pok\u00e9mon. If you do, switch this Pok\u00e9mon with your Active Pok\u00e9mon.",
            trigger=Triggers.ON_PLAY,
            effect=_bust_in,
        ),
        Attack(
            title="Jet Sonic",
            game_text="You may discard an Energy attached to this Pok\u00e9mon. If you do, this attack does 40 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.LIGHTNING: 1},
            damage=80,
            damage_operator="+",
            effect=discard_for_bonus(source='self-energy', flat=40,
                prompt='You may discard an Energy for 40 more damage'),
        ),
    ],
)