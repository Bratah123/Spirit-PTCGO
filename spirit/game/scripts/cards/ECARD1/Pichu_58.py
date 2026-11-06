from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import energy_patch


card = PokemonCardDef(
    guid="2b7952e2-b398-5b76-af60-d08fca591c35",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pichu.Name",
    display_name="Pichu",
    searchable_by=["Pichu", "Baby", "Pichu"],
    subtypes=["Baby"],
    collector_number=58,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=172,
    abilities=[
        Attack(
            title="Energy Patch",
            game_text="Take a basic Energy card attached to 1 of your Pok\u00e9mon and attach it to another of your Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=energy_patch,
        ),
    ],
)
