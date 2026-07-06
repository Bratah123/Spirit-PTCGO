from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b9e39666-3332-5c20-89e8-e460ed95c0b0",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name",
    display_name="Wimpod",
    searchable_by=["Wimpod", "Basic", "Wimpod"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="PGO",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=767,
    abilities=[
        Ability(
            title="Punk Out",
            game_text="If your opponent has any Pok\u00e9mon V in play, this Pok\u00e9mon has no Retreat Cost.",
            effect=unimplemented,
        ),
        Attack(
            title="Gnaw",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)