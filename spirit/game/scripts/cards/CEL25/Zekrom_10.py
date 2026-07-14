from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, named_in_play


async def field_crush(ctx):
    """30 damage; if your opponent has a Stadium in play, discard it."""
    await ctx.deal_damage()
    stadium = ctx.stadium_in_play()
    if stadium is not None and stadium.owning_player_id == ctx.opponent_id:
        await ctx.discard_stadium()


card = PokemonCardDef(
    guid="09b5c42b-c34c-54dc-a807-f4049b33d6dc",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zekrom.Name",
    display_name="Zekrom",
    searchable_by=["Zekrom", "Basic", "Zekrom"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="CEL25",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=644,
    abilities=[
        Attack(
            title="Field Crush",
            game_text="If your opponent has a Stadium in play, discard it.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=field_crush,
        ),
        Attack(
            title="White Thunder",
            game_text="If Reshiram is on your Bench, this attack does 80 more damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=bonus_if(named_in_play("Reshiram"), 80),
        ),
    ],
)