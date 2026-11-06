from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import ignore_effects_attack, mill_attack


card = PokemonCardDef(
    guid="10c27635-b490-5b69-a02c-fb4602cae60b",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiratinaEX.Name",
    display_name="Giratina-EX",
    searchable_by=["Giratina-EX", "Basic", "EX", "GiratinaEX"],
    subtypes=["Basic", "EX"],
    collector_number=124,
    set_code="BW6",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DRAGON,
    family_id=487,
    abilities=[
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=ignore_effects_attack(),
        ),
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top 3 cards of your deck.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=mill_attack(3, opponent=False),
        ),
    ],
)