from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.session.passives import TurnDamageModifier


def is_fire_energy_card(card) -> bool:
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def heat_boost(ctx):
    """Discard a Fire Energy from hand: your Fire Pokémon's attacks do +30
    to the opponent's Active this turn (before applying W/R)."""
    discarded = await ctx.discard_from_hand(
        1, predicate=is_fire_energy_card,
        prompt="Discard a Fire Energy card for Heat Boost",
    )
    if not discarded:
        return
    ctx.add_turn_damage_modifier(TurnDamageModifier(
        30, ctx.player_id,
        source_predicate=lambda p: PokemonTypes.FIRE.value in (
            p.get_attribute(AttrID.POKEMON_TYPES) or []),
    ))


card = PokemonCardDef(
    guid="47de76c5-1287-5f18-8b29-4641ab1a0801",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rapidash.Name",
    display_name="Rapidash",
    searchable_by=["Rapidash", "Stage 1", "Rapidash"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="SWSH12",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name",
    family_id=77,
    abilities=[
        Ability(
            title="Heat Boost",
            game_text="Once during your turn, you may discard a Fire Energy card from your hand in order to use this Ability. During this turn, your Fire Pok\u00e9mon's attacks do 30 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_hand(is_fire_energy_card),
            effect=heat_boost,
        ),
        Attack(
            title="Fire Mane",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)