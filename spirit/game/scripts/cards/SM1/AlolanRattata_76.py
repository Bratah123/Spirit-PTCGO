from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0577cdea-28d0-59ad-af91-7380f1136ec3",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanRattata.Name",
    display_name="Alolan Rattata",
    searchable_by=["Alolan Rattata", "Basic", "AlolanRattata"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="SM1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=19,
    abilities=[
        Attack(
            title="Gnaw",
            cost={},
            damage=20,
        ),
    ],
)