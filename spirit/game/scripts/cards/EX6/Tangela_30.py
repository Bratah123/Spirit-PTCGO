from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import vine_tease, wiggle

card = PokemonCardDef(
    guid="1ca08030-0c8e-505d-9e92-6bfbbc7a1cb1",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name",
    display_name="Tangela",
    searchable_by=["Tangela", "Basic", "Tangela"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="EX6",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=114,
    abilities=[
        Attack(
            title="Vine Tease",
            game_text="Look at your Prize cards without showing your opponent. Choose 1 of the Prize cards and switch it with the top card of your deck without looking at the top card of your deck. If you have no cards in your deck, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=vine_tease(),
        ),
        Attack(
            title="Wiggle",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused. If tails, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=wiggle(),
        ),
    ],
)