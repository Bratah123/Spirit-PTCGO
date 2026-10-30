from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.card_effects.ecard import flipper_stroke, special_energy_on_defender


card = PokemonCardDef(
    guid="0a59ac17-614c-59d5-ad47-ba01c09a6858",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightGolduck.Name",
    display_name="Light Golduck",
    searchable_by=["Light Golduck", "Stage 1", "LightGolduck"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    family_id=54,
    abilities=[
        Attack(
            title="Flipper Stroke",
            game_text="Your opponent looks at the top 3 cards of his or her deck. If any of them are basic Energy cards, he or she may show any number of them to you and put them into his or her hand. You do the same. Either way, each player shuffles his or her deck.",
            cost={PokemonTypes.WATER: 1},
            effect=flipper_stroke,
        ),
        Attack(
            title="Core Blast",
            game_text="This attack does 30 damage plus 20 more damage for each Special Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=damage_per(special_energy_on_defender, 20, base=30),
        ),
    ],
)
