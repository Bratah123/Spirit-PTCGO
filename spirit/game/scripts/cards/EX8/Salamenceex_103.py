"""STUB: effect not implemented — do not guess mechanics.
Salamence ex (EX8 #103): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import bright_flame_discard2, dragon_lift_retreat, flame_jet_snipe


card = PokemonCardDef(
    guid="a2a345fb-4776-5a14-8e9c-1f40f22bad98",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salamenceex.Name",
    display_name="Salamence ex",
    searchable_by=["Salamence ex", "Stage 2", "ex", "Salamenceex"],
    subtypes=["Stage 2", "ex"],
    collector_number=103,
    set_code="EX8",
    rarity=Rarities.RareHoloEX,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    family_id=371,
    abilities=[
        Ability(
            title="Dragon Lift",
            game_text="The Retreat Cost for each of your Pok\u00e9mon (excluding Pok\u00e9mon-ex and Baby Pok\u00e9mon) is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=dragon_lift_retreat(),
        ),
        Attack(
            title="Flame Jet",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 40 damage to that Pok\u00e9mon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=flame_jet_snipe(),
        ),
        Attack(
            title="Bright Flame",
            game_text="Discard 2 Energy attached to Salamence ex.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            # STUB: attack effect not implemented
            effect=bright_flame_discard2(),
        ),
    ],
)