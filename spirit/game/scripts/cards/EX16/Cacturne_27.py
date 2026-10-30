"""STUB: effect not implemented — do not guess mechanics.
Cacturne (EX16 #27): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import pin_missile, poison_structure_sidney
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="832252af-121d-5948-9f7d-a143ca01f498",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cacturne.Name",
    display_name="Cacturne",
    searchable_by=["Cacturne", "Stage 1", "Cacturne"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name",
    family_id=331,
    abilities=[
        Ability(
            title="Poison Structure",
            game_text="Once during your turn (before your attack), if Sidney's Stadium is in play, you may choose 1 of the Defending Pok\u00e9mon. That Pok\u00e9mon is now Poisoned. This power can't be used if Cacturne is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=poison_structure_sidney(),
        ),
        Attack(
            title="Pin Missile",
            game_text="Flip 4 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=pin_missile(4, 20),
        ),
    ],
)