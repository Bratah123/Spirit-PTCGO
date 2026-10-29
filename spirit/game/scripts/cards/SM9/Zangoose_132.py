from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm9 import (
    head_hunt,
)

card = PokemonCardDef(
    guid="845c743e-7f31-5e26-8869-586f36daea1d",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zangoose.Name",
    display_name="Zangoose",
    searchable_by=["Zangoose", "Basic", "Zangoose"],
    subtypes=["Basic"],
    collector_number=132,
    set_code="SM9",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=335,
    abilities=[
        Attack(
            title="Head Hunt",
            game_text="Look at the top 6 cards of your deck, reveal any number of Pok\u00e9mon you find there, and put them into your hand. Discard the other cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=head_hunt,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)