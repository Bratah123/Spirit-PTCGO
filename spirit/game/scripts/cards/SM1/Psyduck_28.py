from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="2fb73769-7332-505e-af51-7a30100f5b25",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    display_name="Psyduck",
    searchable_by=["Psyduck", "Basic", "Psyduck"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="SM1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=54,
    abilities=[
        Attack(
            title="Confusion Wave",
            game_text="Both Active Pok\u00e9mon are now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.CONFUSED, both_actives=True),
        ),
    ],
)