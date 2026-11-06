from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack


card = PokemonCardDef(
    guid="0cc6d501-63d5-5bd3-8db4-cc58ac9ca6bf",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name",
    display_name="Karrablast",
    searchable_by=["Karrablast", "Basic", "Karrablast"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="BW5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=588,
    abilities=[
        Attack(
            title="Beat",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Reckless Charge",
            game_text="This Pok\u00e9mon does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=recoil_attack(10),
        ),
    ],
)