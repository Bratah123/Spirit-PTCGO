"""STUB: effect not implemented — do not guess mechanics.
Drifloon (DP7 #SH1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="d2a9cf58-ef8b-5b00-98c9-4584ffd11ddf",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    display_name="Drifloon",
    searchable_by=["Drifloon", "Basic", "Drifloon"],
    subtypes=["Basic"],
    collector_number=104,
    set_code="DP7",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    family_id=425,
    abilities=[
        Ability(
            title="Unburden",
            game_text="If Drifloon has a Pok\u00e9mon Tool card attached to it, Drifloon's Retreat Cost is ColorlessColorless more.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Big Explosion",
            game_text="Drifloon does 50 damage to itself.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)