from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.pokemon import is_energy_card
from spirit.game.card_effects.attacks_common import lock_all_attacks


def _is_water_energy(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.WATER.value in types


async def crystal_breath(ctx):
    """During your next turn, this Pokemon can't attack."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="b93b22e8-efed-509d-a3d8-058ff11c3084",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Froslass.Name",
    display_name="Froslass",
    searchable_by=["Froslass", "Stage 1", "Froslass"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    family_id=361,
    abilities=[
        Ability(
            title="Frost Over",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may attach a Water Energy card from your discard pile to 1 of your Pok\u00e9mon.",
            trigger=Triggers.ON_EVOLVE,
            effect=attach_from_discard(
                predicate=_is_water_energy, count=1, minimum=0, target="choice",
                prompt="Choose a Water Energy card to attach",
            ),
        ),
        Attack(
            title="Crystal Breath",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=crystal_breath,
        ),
    ],
)