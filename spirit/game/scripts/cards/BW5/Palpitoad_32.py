from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="608d7ec1-b595-588b-9c1c-73ebbf6472b0",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name",
    display_name="Palpitoad",
    searchable_by=["Palpitoad", "Stage 1", "Palpitoad"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tympole.Name",
    family_id=535,
    abilities=[
        Attack(
            title="Bubble Beam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)