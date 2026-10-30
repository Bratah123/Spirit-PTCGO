"""STUB: effect not implemented — do not guess mechanics.
Vibrava (EX3 #46): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import levitate_passive

card = PokemonCardDef(
    guid="2cbb9273-cb96-5319-9f4a-6417e141ccbc",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    display_name="Vibrava",
    searchable_by=["Vibrava", "Stage 1", "Vibrava"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name",
    family_id=328,
    abilities=[
        Ability(
            title="Levitate",
            game_text="If Vibrava has any basic Energy cards attached to it, Vibrava's Retreat Cost is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=levitate_passive(),
        ),
        Attack(
            title="Razor Wing",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)