"""STUB: effect not implemented — do not guess mechanics.
Beautifly (EX8 #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.ex import hunch_low_hp_boost, luring_antenna


card = PokemonCardDef(
    guid="3a485514-8657-5197-80cc-e09ddbf39c17",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beautifly.Name",
    display_name="Beautifly",
    searchable_by=["Beautifly", "Stage 2", "Beautifly"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Silcoon.Name",
    family_id=265,
    abilities=[
        Ability(
            title="Hunch",
            game_text="As long as Beautifly's remaining HP is 40 or less, Beautifly does 40 more damage to the Defending Pok\u00e9mon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=hunch_low_hp_boost(),
        ),
        Attack(
            title="Luring Antenna",
            game_text="Before doing damage, you may choose 1 of your opponent's Benched Pok\u00e9mon and switch it with 1 of the Defending Pok\u00e9mon. If you do, this attack does 20 damage to the new Defending Pok\u00e9mon. Your opponent chooses the Defending Pok\u00e9mon to switch.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=luring_antenna(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Cutting Wind",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)