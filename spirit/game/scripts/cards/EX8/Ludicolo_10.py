"""STUB: effect not implemented — do not guess mechanics.
Ludicolo (EX8 #10): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import circular_steps_per_pokemon, healing_steps_discard_heal, swing_dance_draw


card = PokemonCardDef(
    guid="ab24f9c6-48ef-5ba6-8d9d-5e05a7d4cf00",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ludicolo.Name",
    display_name="Ludicolo",
    searchable_by=["Ludicolo", "Stage 2", "Ludicolo"],
    subtypes=["Stage 2"],
    collector_number=10,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name",
    family_id=270,
    abilities=[
        Ability(
            title="Swing Dance",
            game_text="Once during your turn (before your attack), you may draw a card. This power can't be used if Ludicolo is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=swing_dance_draw(),
        ),
        Attack(
            title="Healing Steps",
            game_text="You may discard as many cards as you like from your hand. If you do, remove that many damage counters from Ludicolo.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=healing_steps_discard_heal(),
        ),
        Attack(
            title="Circular Steps",
            game_text="Does 10 damage times the number of Pok\u00e9mon in play (both yours and your opponent's), excluding Ludicolo.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=circular_steps_per_pokemon(),
        ),
    ],
)