from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.card_effects.pokemon import (
    is_pokemon_vmax, stance_change, stance_change_condition,
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def gigaton_bash(ctx):
    """70; next turn, prevent all damage done to this Pokemon by VMAX attacks."""
    await ctx.deal_damage()
    shield = prevent_damage_when(
        lambda calc, c: calc.target is c and calc.attacker is not None
        and is_pokemon_vmax(calc.attacker.archetype_id)
    )
    ctx.add_passive_through_opponents_turn(ctx.attacker, shield)

card = PokemonCardDef(
    guid="e280a8c7-5005-5e52-ac53-e88293377075",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aegislash.Name",
    display_name="Aegislash",
    searchable_by=["Aegislash", "Stage 2", "Aegislash"],
    subtypes=["Stage 2"],
    collector_number=108,
    set_code="SWSH5",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name",
    family_id=679,
    abilities=[
        Ability(
            title="Stance Change",
            game_text="Once during your turn, you may switch this Pok\u00e9mon with an Aegislash in your hand. Any attached cards, damage counters, Special Conditions, turns in play, and any other effects remain on the new Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=stance_change_condition,
            effect=stance_change,
        ),
        Attack(
            title="Gigaton Bash",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Pok\u00e9mon VMAX.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=gigaton_bash,
        ),
    ],
)