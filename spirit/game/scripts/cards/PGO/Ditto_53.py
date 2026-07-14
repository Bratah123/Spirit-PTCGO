from spirit.game.data_utils import PokemonCardDef, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import SuddenTransformationPassive

card = PokemonCardDef(
    guid="b37b1ba4-3f8a-555a-bf98-caaccf0e8dfe",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name",
    display_name="Ditto",
    searchable_by=["Ditto", "Basic", "Ditto"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="PGO",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=132,
    abilities=[
        Ability(
            title="Sudden Transformation",
            game_text="This Pok\u00e9mon can use the attacks of any Basic Pok\u00e9mon in your discard pile, except for Pok\u00e9mon with a Rule Box (Pok\u00e9mon V, Pok\u00e9mon-GX, etc. have Rule Boxes). (You still need the necessary Energy to use each attack.)",
            passive=SuddenTransformationPassive(),
        ),
    ],
)