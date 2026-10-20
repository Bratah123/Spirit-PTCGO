"""STUB: effect not implemented — do not guess mechanics.
Blaziken (XY3 #14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="fdbacd4c-c1aa-548b-ae06-022060a67687",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blaziken.Name",
    display_name="Blaziken",
    searchable_by=["Blaziken", "Stage 2", "Blaziken"],
    subtypes=["Stage 2"],
    collector_number=14,
    set_code="XY3",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name",
    family_id=255,
    abilities=[
        Attack(
            title="Clutch",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Burning Shot",
            game_text="Discard 2 Energy attached to this Pok\u00e9mon. This attack does 150 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)