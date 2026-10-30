"""STUB: effect not implemented — do not guess mechanics.
Cresselia (DPP #DP51): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="fd333c04-9a6d-5078-8b67-48d0b704e6d3",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cresselia.Name",
    display_name="Cresselia",
    searchable_by=["Cresselia", "Basic", "Cresselia"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=488,
    abilities=[
        Ability(
            title="Lunar Aura",
            game_text="If you have Darkrai in play, remove 1 damage counter from Cresselia between turns.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Lunar Flight",
            game_text="Does 80 damage minus 10 damage for each damage counter on Cresselia.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="-",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)