from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.card_effects.trainers import is_basic_energy_card


def _is_psychic_energy(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_basic_energy_card(card) and PokemonTypes.PSYCHIC.value in types


async def _supernatural_orb(ctx):
    discarded = await ctx.discard_from_hand(
        1, prompt="Discard a Psychic Energy card for Supernatural Orb",
        predicate=_is_psychic_energy,
    )
    if not discarded:
        return
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="322b0073-6630-5cfb-9494-ed708adfb6d9",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianTyphlosion.Name",
    display_name="Hisuian Typhlosion",
    searchable_by=["Hisuian Typhlosion", "Stage 2", "HisuianTyphlosion"],
    subtypes=["Stage 2"],
    collector_number=52,
    set_code="SWSH10",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name",
    family_id=155,
    abilities=[
        Ability(
            title="Supernatural Orb",
            game_text="You must discard a Psychic Energy card from your hand in order to use this Ability. Once during your turn, you may make your opponent's Active Pok\u00e9mon Burned and Confused.",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_hand(_is_psychic_energy, n=1),
            effect=_supernatural_orb,
        ),
        Attack(
            title="Shadow Bind",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)