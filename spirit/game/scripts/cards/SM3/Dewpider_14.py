from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="72e220be-7b09-517c-b975-417bc53c7e25",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dewpider.Name",
    display_name="Dewpider",
    searchable_by=["Dewpider", "Basic", "Dewpider"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="SM3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=751,
    abilities=[
        Attack(
            title="Ambush",
            game_text="Flip a coin. If heads, this attack does 10 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_bonus(10),
        ),
    ],
)
