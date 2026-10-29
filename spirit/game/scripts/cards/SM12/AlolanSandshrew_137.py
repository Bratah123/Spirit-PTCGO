from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import switch_self_attack


card = PokemonCardDef(
    guid="6f5651e3-d4e0-531a-ad4b-59320c69d812",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanSandshrew.Name",
    display_name="Alolan Sandshrew",
    searchable_by=["Alolan Sandshrew", "Basic", "AlolanSandshrew"],
    subtypes=["Basic"],
    collector_number=137,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=27,
    abilities=[
        Attack(
            title="Run Around",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={},
            effect=switch_self_attack(),
        ),
        Attack(
            title="Metal Claw",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)