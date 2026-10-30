from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import aqua_lift_passive

card = PokemonCardDef(
    guid="299c9016-79da-50ac-af25-fe6660accefa",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lotad.Name",
    display_name="Lotad",
    searchable_by=["Lotad", "Basic", "Lotad"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="EX14",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=270,
    abilities=[
        Ability(
            title="Aqua Lift",
            game_text="If Lotad has any Water Energy attached to it, the Retreat Cost for Lotad is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=aqua_lift_passive(),
            effect=None,
        ),
        Attack(
            title="Rolling Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)