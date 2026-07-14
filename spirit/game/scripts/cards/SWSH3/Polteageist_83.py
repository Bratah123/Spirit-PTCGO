from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.card_effects.attacks_common import count_discard, damage_per, has_attack_titled

_HAS_MAD_PARTY = has_attack_titled("Mad Party")


async def tea_break(ctx):
    """Discard a Pokémon with the Mad Party attack from hand to use this
    Ability. Once during your turn, you may draw 2 cards."""
    picks = await ctx.discard_from_hand(
        1, predicate=_HAS_MAD_PARTY,
        prompt="Discard a Pokémon that has the Mad Party attack.",
    )
    if not picks:
        return
    if await ctx.ask_yes_no("Draw 2 cards?"):
        await ctx.draw_cards(2)


card = PokemonCardDef(
    guid="607b8809-852a-5dd7-bd38-305fb7069c68",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Polteageist.Name",
    display_name="Polteageist",
    searchable_by=["Polteageist", "Stage 1", "Polteageist"],
    subtypes=["Stage 1"],
    collector_number=83,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sinistea.Name",
    family_id=854,
    abilities=[
        Ability(
            title="Tea Break",
            game_text="You must discard a Pokémon that has the Mad Party attack from your hand in order to use this Ability. Once during your turn, you may draw 2 cards.",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_hand(_HAS_MAD_PARTY),
            effect=tea_break,
        ),
        Attack(
            title="Mad Party",
            game_text="This attack does 20 damage for each Pokémon in your discard pile that has the Mad Party attack.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=damage_per(count_discard("mine", _HAS_MAD_PARTY), 20),
        ),
    ],
)
