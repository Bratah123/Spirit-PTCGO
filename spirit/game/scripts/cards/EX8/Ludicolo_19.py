"""STUB: effect not implemented — do not guess mechanics.
Ludicolo (EX8 #19): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import happy_dance_heal_all, water_punch


card = PokemonCardDef(
    guid="1e4db9b2-ca86-5b7c-a6c5-6aedd5afe955",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ludicolo.Name",
    display_name="Ludicolo",
    searchable_by=["Ludicolo", "Stage 2", "Ludicolo"],
    subtypes=["Stage 2"],
    collector_number=19,
    set_code="EX8",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name",
    family_id=270,
    abilities=[
        Ability(
            title="Happy Dance",
            game_text="Once during your turn (before your attack), you may remove 1 damage counter from each of your Pok\u00e9mon. You can't use more than 1 Happy Dance Pok\u00e9-Power each turn. This power can't be used if Ludicolo is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=happy_dance_heal_all(),
        ),
        Attack(
            title="Water Punch",
            game_text="Flip a coin for each Water Energy attached to Ludicolo. This attack does 40 damage plus 20 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=water_punch(40, 20),
        ),
    ],
)