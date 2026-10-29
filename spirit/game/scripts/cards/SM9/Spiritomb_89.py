from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm9 import (
    spirit_compressor,
)

card = PokemonCardDef(
    guid="1df63159-b445-5e30-8634-2f284739a8be",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=89,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=442,
    abilities=[
        Attack(
            title="Spirit Compressor",
            game_text="Search your deck for up to 4 Pok\u00e9mon and discard them. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=spirit_compressor,
        ),
        Attack(
            title="Spooky Shot",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)