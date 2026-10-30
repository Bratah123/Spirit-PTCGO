"""STUB: effect not implemented — do not guess mechanics.
Burmy Sandy Cloak (DP3 #79): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="6b2c124b-a2d6-51c1-b0eb-6df466286914",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BurmySandyCloak.Name",
    display_name="Burmy Sandy Cloak",
    searchable_by=["Burmy Sandy Cloak", "Basic", "BurmySandyCloak"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="DP3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=412,
    abilities=[
        Ability(
            title="Wear Cloak",
            game_text="Once during your turn (before your attack), if Burmy Sandy Cloak is your Active Pok\u00e9mon, you may search your discard for a basic Fighting Energy card and attach it to Burmy Sandy Cloak.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sandy Cloak Tackle",
            game_text="If Burmy Sandy Cloak has any Fighting Energy attached to it, this attack does 10 damage plus 10 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)