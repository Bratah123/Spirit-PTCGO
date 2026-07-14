from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def synchro_kinesis(ctx):
    """Each player reveals their hand; +90 if a name is shared."""
    await ctx.reveal_hand(ctx.player_id, ctx.opponent_id)
    await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
    mine = {c.card_obj.display_name for c in ctx.hand(ctx.player_id)}
    theirs = {c.card_obj.display_name for c in ctx.hand(ctx.opponent_id)}
    bonus = 90 if mine & theirs else 0
    await ctx.deal_damage(30 + bonus)


card = PokemonCardDef(
    guid="d6b0e441-098d-5018-8652-b61b66cc4365",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Malamar.Name",
    display_name="Malamar",
    searchable_by=["Malamar", "Stage 1", "Malamar"],
    subtypes=["Stage 1"],
    collector_number=78,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    family_id=686,
    abilities=[
        Attack(
            title="Synchro Kinesis",
            game_text="Each player reveals their hand. If a card in your opponent's hand has the same name as a card in your hand, this attack does 90 more damage.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="+",
            effect=synchro_kinesis,
        ),
        Attack(
            title="Psychic Sphere",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)