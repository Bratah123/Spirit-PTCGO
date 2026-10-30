"""STUB: effect not implemented — do not guess mechanics.
Ho-Oh ex (EX10 #104): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import golden_wing_on_ko_passive, rainbow_burn

card = PokemonCardDef(
    guid="859d24e5-fd07-5e1e-9e6b-5fff8463f0c7",
    key="POP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOhex.Name",
    display_name="Ho-Oh ex",
    searchable_by=["Ho-Oh ex", "Basic", "ex", "HoOhex"],
    subtypes=["Basic", "ex"],
    collector_number=17,
    set_code="POP3",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=250,
    abilities=[
        Ability(
            title="Golden Wing",
            game_text="If Ho-Oh ex would be Knocked Out by damage from an opponent's attack, you may move up to 2 Energy attached to Ho-Oh ex to your Pok\u00e9mon in any way you like.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            passive=golden_wing_on_ko_passive(2),
        ),
        Attack(
            title="Rainbow Burn",
            game_text="Does 10 damage plus 20 more damage for each type of basic Energy card attached to Ho-Oh ex.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=rainbow_burn(10, 20),
        ),
    ],
)