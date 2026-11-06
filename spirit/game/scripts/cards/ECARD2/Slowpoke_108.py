from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.ecard import is_pokemon_or_basic_energy


card = PokemonCardDef(
    guid="7b95c05f-c148-56a7-9497-e32e09704e1a",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke", "Basic", "Slowpoke"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=79,
    abilities=[
        Attack(
            title="Fishing Tail",
            game_text="Search your discard pile for a Baby Pok\u00e9mon, Basic Pok\u00e9mon, Evolution card, or basic Energy card, show it to your opponent, and then put it into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=recover_from_discard(
                predicate=is_pokemon_or_basic_energy, count=1, minimum=1,
                reveal=True,
                prompt="Choose a Baby Pokémon, Basic Pokémon, Evolution card, or basic Energy card",
            ),
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
