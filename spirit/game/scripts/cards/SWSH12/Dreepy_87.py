from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(
    guid="500a69fb-1abb-5c66-80b3-a60b4e1a52b2",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dreepy.Name",
    display_name="Dreepy",
    searchable_by=["Dreepy", "Basic", "Dreepy"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="SWSH12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=885,
    abilities=[
        Attack(
            title="Reckless Charge",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=recoil_attack(10),
        ),
    ],
)