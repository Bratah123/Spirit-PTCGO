from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, defender_has_condition
from spirit.game.attributes import SpecialConditions


card = PokemonCardDef(
    guid="2c443318-45f3-506e-8f97-f0dd6b756fb5",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name",
    display_name="Salandit",
    searchable_by=["Salandit", "Basic", "Salandit"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="SM2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=757,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.FIRE: 1},
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