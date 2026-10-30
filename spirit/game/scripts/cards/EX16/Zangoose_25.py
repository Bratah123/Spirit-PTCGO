"""STUB: effect not implemented — do not guess mechanics.
Zangoose (EX16 #25): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import call_for_family_basic_n, thick_skin_passive
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="6f0e1f26-214c-5caf-a31d-652f9dc739bf",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zangoose.Name",
    display_name="Zangoose",
    searchable_by=["Zangoose", "Basic", "Zangoose"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="EX16",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=335,
    abilities=[
        Ability(
            title="Thick Skin",
            game_text="Zangoose can't be affected by any Special Conditions.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=thick_skin_passive(),
        ),
        Attack(
            title="Call for Family",
            game_text="Search your deck for up to 2 Basic Pok\u00e9mon and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=call_for_family_basic_n(2),
        ),
        Attack(
            title="Sharp Claws",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_bonus(20),
        ),
    ],
)