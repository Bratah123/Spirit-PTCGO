from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, defender_has_condition
from spirit.game.attributes import SpecialConditions


card = PokemonCardDef(
    guid="cc917d85-89a6-5a4a-b080-669a414a0932",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venipede.Name",
    display_name="Venipede",
    searchable_by=["Venipede", "Basic", "Venipede"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="SM3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=543,
    abilities=[
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title="Venoshock",
            game_text="If your opponent's Active Pok\u00e9mon is Poisoned, this attack does 40 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=bonus_if(defender_has_condition(SpecialConditions.POISONED), 40),
        ),
    ],
)
