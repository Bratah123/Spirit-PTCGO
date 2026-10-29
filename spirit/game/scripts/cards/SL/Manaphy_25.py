"""STUB: effect not implemented — do not guess mechanics.
Manaphy (SL #25): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sl import blessings_condition, blessings_of_the_deep

card = PokemonCardDef(
    guid="c0724aab-3868-52c0-9ac9-f5730d22f50d",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name",
    display_name="Manaphy",
    searchable_by=["Manaphy", "Basic", "Manaphy"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="SL",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=490,
    abilities=[
        Ability(
            title="Blessings of the Deep",
            game_text="Once during your turn (before your attack), you may heal 20 damage from 1 of your Pok\u00e9mon that has any Water Energy attached to it.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=blessings_condition,
            effect=blessings_of_the_deep,
        ),
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)