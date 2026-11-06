from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import is_in_active_spot


def _cursed_shadow_condition(board, player_id, pokemon):
    return is_in_active_spot(pokemon)


async def cursed_shadow(ctx):
    """Put 3 damage counters on opponent's Pokémon in any way you like."""
    await ctx.place_damage_counters(3)


card = PokemonCardDef(
    guid="840f1dba-c328-5be3-806c-163223d43666",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chandelure.Name",
    display_name="Chandelure",
    searchable_by=["Chandelure", "Stage 2", "Chandelure"],
    subtypes=["Stage 2"],
    collector_number=101,
    set_code="BW4",
    rarity=Rarities.RareSecret,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    family_id=607,
    abilities=[
        Ability(
            title="Cursed Shadow",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is your Active Pok\u00e9mon, you may put 3 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=_cursed_shadow_condition,
            effect=cursed_shadow,
        ),
        Attack(
            title="Eerie Glow",
            game_text="The Defending Pok\u00e9mon is now Burned and Confused.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=condition_attack(SpecialConditions.BURNED, SpecialConditions.CONFUSED),
        ),
    ],
)