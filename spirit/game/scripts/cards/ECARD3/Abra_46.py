from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import PsychoflowPassive


card = PokemonCardDef(
    guid="4c489076-6601-5535-806a-2a30f7b9a287",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Abra.Name",
    display_name="Abra",
    searchable_by=["Abra", "Basic", "Abra"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=63,
    abilities=[
        Ability(
            title="Psychoflow",
            game_text="As long as there is a Psychic Energy card attached to Abra, its Retreat Cost is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=PsychoflowPassive(),
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
