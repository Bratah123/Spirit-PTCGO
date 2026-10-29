from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def pry(ctx):
    """10 damage. Your opponent reveals their hand."""
    await ctx.deal_damage()
    await ctx.reveal_hand(of_player=ctx.opponent_id)


card = PokemonCardDef(
    guid="54b3d5cf-8c64-5528-a14f-b7127ea6fd13",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name",
    display_name="Hoothoot",
    searchable_by=["Hoothoot", "Basic", "Hoothoot"],
    subtypes=["Basic"],
    collector_number=106,
    set_code="SM3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=163,
    abilities=[
        Attack(
            title="See Through",
            game_text="Your opponent reveals their hand.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=pry,
        ),
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
