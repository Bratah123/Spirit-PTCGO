from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.card_effects.trainers import is_basic_energy_card


def _is_water_energy_card(card):
    return is_basic_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER.value)


async def _double_jet(ctx):
    """Discard up to 2 Water Energy cards from your hand; 60 per card."""
    discarded = await ctx.discard_from_hand(
        2, minimum=0, predicate=_is_water_energy_card,
        prompt="Discard up to 2 Water Energy cards")
    await ctx.deal_damage(60 * len(discarded))


card = PokemonCardDef(
    guid="68285aaa-31e3-551a-8e30-29885d49015a",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golduck.Name",
    display_name="Golduck",
    searchable_by=["Golduck", "Stage 1", "Golduck"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="SM1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    family_id=54,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Double Jet",
            game_text="Discard up to 2 Water Energy cards from your hand. This attack does 60 damage for each card you discarded in this way.",
            cost={PokemonTypes.WATER: 1},
            damage=60,
            damage_operator="x",
            effect=_double_jet,
        ),
    ],
)