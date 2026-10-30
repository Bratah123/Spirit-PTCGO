"""STUB: effect not implemented — do not guess mechanics.
Swampert (EX9 #11): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import breaking_sound, water_cyclone, water_cyclone_condition


async def puncture(ctx):
    """This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="3405b653-9144-512c-b91f-ab50220813cd",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swampert.Name",
    display_name="Swampert",
    searchable_by=["Swampert", "Stage 2", "Swampert"],
    subtypes=["Stage 2"],
    collector_number=11,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marshtomp.Name",
    family_id=258,
    abilities=[
        Ability(
            title="Water Cyclone",
            activation=Activations.UNLIMITED,
            condition=water_cyclone_condition(),
            game_text="As often as you like during your turn (before your attack), you may move a Water Energy attached to 1 of your Active Pok\u00e9mon to 1 of your Benched Pok\u00e9mon. This power can't be used if Swampert is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
                        effect=water_cyclone(),
        ),
        Attack(
            title="Spinning Tail",
            game_text="Does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=breaking_sound(10),
        ),
        Attack(
            title="Aqua Sonic",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=puncture,
        ),
    ],
)