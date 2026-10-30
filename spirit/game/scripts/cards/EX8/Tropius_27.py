"""STUB: effect not implemented — do not guess mechanics.
Tropius (EX8 #27): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import miracle_powder, tropical_motion_no_resist
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="0ee3a9bc-8c09-51ea-acd3-d31862683c15",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tropius.Name",
    display_name="Tropius",
    searchable_by=["Tropius", "Basic", "Tropius"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="EX8",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=357,
    abilities=[
        Ability(
            title="Tropical Motion",
            game_text="As long as Tropius is your Active Pok\u00e9mon, your opponent's Active Pok\u00e9mon have no Resistance.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=tropical_motion_no_resist(),
        ),
        Attack(
            title="Miracle Blow",
            game_text="Flip a coin. If heads, choose 1 Special Condition. The Defending Pok\u00e9mon is now affected by that Special Condition.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=miracle_powder(),
        ),
        Attack(
            title="Stomp",
            game_text="Flip a coin. If heads, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_bonus(20),
        ),
    ],
)