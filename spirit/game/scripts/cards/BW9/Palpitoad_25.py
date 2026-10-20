from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="60434926-375b-5f24-b662-32c7b98e4f67",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name",
    display_name="Palpitoad",
    searchable_by=["Palpitoad", "Stage 1", "Palpitoad"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tympole.Name",
    family_id=535,
    abilities=[
        Attack(
            title="Vibration",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Suspicious Soundwave",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)