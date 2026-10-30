"""STUB: effect not implemented — do not guess mechanics.
Jirachi (EX8 #9): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import metallic_blow_body_bonus, wishing_star_look5


card = PokemonCardDef(
    guid="fd1179f0-b3f9-501a-928d-a8ced9ae0bd6",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name",
    display_name="Jirachi",
    searchable_by=["Jirachi", "Basic", "Jirachi"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=385,
    abilities=[
        Ability(
            title="Wishing Star",
            game_text="Once during your turn (before your attack), if Jirachi is your Active Pok\u00e9mon, you may look at the top 5 cards of your deck, choose 1 of them, and put it into your hand. Shuffle your deck afterward. Jirachi and your other Active Pok\u00e9mon, if any, are now Asleep. This power can't be used if Jirachi is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=wishing_star_look5(),
        ),
        Attack(
            title="Metallic Blow",
            game_text="If the Defending Pok\u00e9mon has any Pok\u00e9-Bodies, this attack does 20 damage plus 30 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=metallic_blow_body_bonus(),
        ),
    ],
)