from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import discard_all_self_energy_on_tails, super_removal


card = PokemonCardDef(
    guid="0e0a43f4-8ba6-59e0-bc8f-c3af58ad685c",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysGolduck.Name",
    display_name="Misty's Golduck",
    searchable_by=["Misty's Golduck", "Stage 1", "MistysGolduck"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MistysPsyduck.Name",
    family_id=54,
    abilities=[
        Attack(
            title="Electro Beam",
            game_text="Flip a coin. If tails, discard all Energy cards attached to Misty's Golduck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=discard_all_self_energy_on_tails(),
        ),
        Attack(
            title="Super Removal",
            game_text="Flip a coin. If heads, choose 1 Energy card attached to each of your opponent's Pok\u00e9mon that has any Energy cards and discard those Energy cards.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=super_removal,
        ),
    ],
)
